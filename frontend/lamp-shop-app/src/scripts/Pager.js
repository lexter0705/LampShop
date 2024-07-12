import React, { useState, useEffect } from 'react';
import RouteContext from './RouteContext';

const Pager = ({ children }) => {
  const [currentPath, setCurrentPath] = useState(window.location.pathname);

  useEffect(() => {
    const onPopState = () => {
      setCurrentPath(window.location.pathname);
    };

    window.addEventListener('popstate', onPopState);

    return () => {
      window.removeEventListener('popstate', onPopState);
    };
  }, []);

  return (
    <RouteContext.Provider value={{ currentPath, setCurrentPath }}>
      {children}
    </RouteContext.Provider>
  );
};

export default Pager;
