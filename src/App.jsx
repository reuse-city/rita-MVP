import React from 'react';
import RITA from './components/RITA';

/**
 * Main application component that renders RITA
 * Uses a responsive layout with a centered design
 */
function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center">
            <div className="flex items-center">
              <img 
                src="/rita-logo.svg" 
                alt="RITA Logo" 
                className="h-8 w-8 mr-2"
                onError={(e) => {
                  e.target.style.display = 'none';
                }} 
              />
              <div>
                <h1 className="text-xl font-bold text-gray-900">ThingData</h1>
                <p className="text-sm text-gray-500">Repair Intelligence & Technical Assistant</p>
              </div>
            </div>
            <nav className="flex space-x-4">
              <a 
                href="https://github.com/reuse-city/rita" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-gray-500 hover:text-gray-700"
              >
                GitHub
              </a>
              <a 
                href="https://reuse.city" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-gray-500 hover:text-gray-700"
              >
                About
              </a>
            </nav>
          </div>
        </div>
      </header>

      {/* Main content */}
      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="flex flex-col space-y-8">
          {/* Introduction section */}
          <section className="text-center max-w-2xl mx-auto">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">
              Welcome to RITA
            </h2>
            <p className="text-gray-600">
              RITA helps you evaluate repair options, connect with repair communities, 
              and make informed decisions about reuse. Upload a photo or describe your 
              item to get started.
            </p>
          </section>

          {/* RITA Chat Interface */}
          <section className="flex justify-center">
            <RITA />
          </section>

          {/* Footer information */}
          <section className="text-center text-sm text-gray-500 max-w-2xl mx-auto">
            <p>
              RITA is part of the ThingData project, an open and collectively governed 
              data solution to help achieve a longer lifetime for goods and materials.
            </p>
            <p className="mt-2">
              Licensed under AGPL-3.0 - Source code available on{' '}
              <a 
                href="https://github.com/reuse-city/rita" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-blue-500 hover:text-blue-700"
              >
                GitHub
              </a>
            </p>
          </section>
        </div>
      </main>
    </div>
  );
}

export default App;
