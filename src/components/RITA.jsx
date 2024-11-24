import React, { useState, useRef } from 'react';
import { Send, Camera, Upload, DollarSign, Clock, Recycle, Users, Lightbulb, Scale, ExternalLink } from 'lucide-react';
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from './ui/card';
import { Alert, AlertDescription } from './ui/alert';

/**
 * RITA - Repair Intelligence & Technical Assistant
 * A component of the ThingData project that helps users evaluate repair options.
 *
 * Features:
 * - Chat interface for repair guidance
 * - Image upload for item identification
 * - Value and repair feasibility assessment
 * - Environmental impact awareness
 * - Connection to repair resources
 */

const RITA = () => {
  // State management
  const fileInputRef = useRef(null);
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      type: 'message',
      content: `Hello! I'm RITA, your Repair Intelligence & Technical Assistant. 
                I'm here to help evaluate repair options and connect you with repair resources. 
                You can describe your item or upload a photo to get started.`
    }
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const [analyzing, setAnalyzing] = useState(false);

  /**
   * Sample repair resources database
   * In production, this would be fetched from an API
   */
  const repairResources = {
    'general': [
      { 
        title: 'Find a Repair Café',
        url: 'https://repaircafe.org/en/',
        type: 'community'
      },
      {
        title: 'iFixit Repair Guides',
        url: 'https://www.ifixit.com/Guide',
        type: 'documentation'
      },
      {
        title: 'Restart Project Wiki',
        url: 'https://therestartproject.org/wiki/',
        type: 'documentation'
      }
    ],
    'electronics': [
      {
        title: 'Electronics Repair Safety Guide',
        url: 'https://www.ifixit.com/Safety',
        type: 'safety'
      }
    ]
  };

  /**
   * Handles sending user messages and generating responses
   */
  const handleSendMessage = () => {
    if (!inputMessage.trim()) return;

    // Add user message
    const newMessages = [...messages, { 
      role: 'user', 
      type: 'message', 
      content: inputMessage 
    }];
    setMessages(newMessages);
    setInputMessage('');

    // Generate response
    setTimeout(() => {
      const responses = generateResponse(inputMessage);
      setMessages(prev => [...prev, ...responses]);
    }, 1000);
  };

  /**
   * Generates contextual responses based on user input
   * @param {string} userInput - The user's message
   * @returns {Array} Array of response messages
   */
  const generateResponse = (userInput) => {
    const responses = [
      {
        role: 'assistant',
        type: 'message',
        content: `I understand you're interested in repairing an item. 
                 To provide better guidance, could you tell me:
                 - What's the current condition of the item?
                 - How urgent is the repair?
                 - Do you have repair experience with similar items?`
      },
      {
        role: 'assistant',
        type: 'resources',
        content: repairResources.general
      },
      {
        role: 'assistant',
        type: 'environmental-tip',
        content: `Did you know? Repairing items not only saves money but also significantly 
                 reduces electronic waste. Each repaired device means fewer toxic materials 
                 in landfills and reduced demand for new resource extraction.`
      }
    ];

    return responses;
  };

  /**
   * Handles image upload and analysis
   * @param {Event} event - Upload event
   */
  const handleImageUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    setAnalyzing(true);
    
    // Add image preview
    const imageUrl = URL.createObjectURL(file);
    setMessages(prev => [...prev, {
      role: 'user',
      type: 'image',
      content: imageUrl
    }]);

    // Simulate image analysis
    setTimeout(() => {
      const analysisResponse = [
        {
          role: 'assistant',
          type: 'analysis',
          content: {
            itemType: 'Electronic Device',
            estimatedAge: '2-3 years',
            repairComplexity: 'Medium',
            commonIssues: 'Screen damage, battery issues, charging problems'
          }
        },
        {
          role: 'assistant',
          type: 'value-assessment',
          content: {
            estimatedCurrentValue: '$150-200',
            estimatedRepairedValue: '$300-350',
            commonRepairCosts: '$80-120',
            repairComplexity: 'Medium',
            estimatedRepairTime: '1-2 hours',
            environmentalImpact: 'Repairing this device could prevent about 40kg of CO2 emissions'
          }
        },
        {
          role: 'assistant',
          type: 'resources',
          content: repairResources.electronics
        }
      ];
      
      setMessages(prev => [...prev, ...analysisResponse]);
      setAnalyzing(false);
    }, 2000);
  };

  /**
   * Renders different types of chat messages
   * @param {Object} message - Message object to render
   */
  const renderMessage = (message) => {
    switch (message.type) {
      case 'image':
        return (
          <div className="max-w-[80%]">
            <img 
              src={message.content} 
              alt="Uploaded item" 
              className="rounded-lg max-h-48 object-cover"
            />
          </div>
        );
      
      case 'analysis':
        return (
          <div className="bg-gray-100 rounded-lg p-4 max-w-[80%]">
            <div className="font-semibold mb-2 flex items-center gap-2">
              <Lightbulb className="w-4 h-4" />
              Item Analysis
            </div>
            <ul className="space-y-2">
              {Object.entries(message.content).map(([key, value]) => (
                <li key={key} className="flex items-center gap-2">
                  <span className="font-medium">{key}:</span> {value}
                </li>
              ))}
            </ul>
          </div>
        );
      
      case 'value-assessment':
        return (
          <div className="bg-gray-100 rounded-lg p-4 max-w-[80%]">
            <div className="font-semibold mb-2 flex items-center gap-2">
              <Scale className="w-4 h-4" />
              Repair Value Assessment
            </div>
            <div className="space-y-3">
              <div className="flex items-center gap-2">
                <DollarSign className="w-4 h-4 text-green-600" />
                <div>
                  <div className="font-medium">Current Value: {message.content.estimatedCurrentValue}</div>
                  <div className="font-medium">After Repair: {message.content.estimatedRepairedValue}</div>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <Clock className="w-4 h-4 text-blue-600" />
                <div>
                  <div>Repair Time: {message.content.estimatedRepairTime}</div>
                  <div>Complexity: {message.content.repairComplexity}</div>
                </div>
              </div>
              <div className="mt-2 text-sm text-gray-600">
                <div>Typical repair costs: {message.content.commonRepairCosts}</div>
                <div className="mt-1 text-green-600">
                  🌱 {message.content.environmentalImpact}
                </div>
              </div>
            </div>
          </div>
        );

      case 'resources':
        return (
          <div className="bg-gray-100 rounded-lg p-4 max-w-[80%]">
            <div className="font-semibold mb-2 flex items-center gap-2">
              <ExternalLink className="w-4 h-4" />
              Helpful Resources
            </div>
            <ul className="space-y-2">
              {message.content.map((resource, i) => (
                <li key={i} className="flex items-center gap-2">
                  <ExternalLink className="w-4 h-4 text-blue-500" />
                  <span className="text-blue-500">{resource.title}</span>
                </li>
              ))}
            </ul>
          </div>
        );
      
      case 'environmental-tip':
        return (
          <Alert className="max-w-[80%]">
            <Recycle className="w-4 h-4" />
            <AlertDescription>
              {message.content}
            </AlertDescription>
          </Alert>
        );

      default:
        return (
          <div className={`rounded-lg px-4 py-2 max-w-[80%] ${
            message.role === 'user'
              ? 'bg-blue-500 text-white'
              : 'bg-gray-100 text-gray-900'
          }`}>
            {message.content}
          </div>
        );
    }
  };

  return (
    <Card className="w-full max-w-3xl h-[600px] flex flex-col">
      <CardHeader className="border-b">
        <CardTitle className="flex items-center gap-2">
          <Recycle className="w-6 h-6" />
          RITA - Repair Intelligence & Technical Assistant
        </CardTitle>
      </CardHeader>
      
      <CardContent className="flex-1 overflow-y-auto py-4">
        <div className="space-y-4">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              {renderMessage(message)}
            </div>
          ))}
          {analyzing && (
            <div className="flex justify-start">
              <Alert className="max-w-[80%]">
                <AlertDescription className="flex items-center gap-2">
                  <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-gray-900"></div>
                  Analyzing your image...
                </AlertDescription>
              </Alert>
            </div>
          )}
        </div>
      </CardContent>

      <CardFooter className="border-t p-4">
        <div className="flex w-full gap-2">
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleImageUpload}
            accept="image/*"
            className="hidden"
          />
          <button
            onClick={() => fileInputRef.current?.click()}
            className="p-2 bg-gray-100 text-gray-600 rounded-lg hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
            title="Upload an image"
          >
            <Camera className="w-5 h-5" />
          </button>
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
            placeholder="Describe your item or ask about repair options..."
            className="flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={handleSendMessage}
            className="p-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            title="Send message"
          >
            <Send className="w-5 h-5" />
          </button>
        </div>
      </CardFooter>
    </Card>
  );
};

export default RITA;
