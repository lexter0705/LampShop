import React, { useContext } from 'react';
import RouteContext from './RouteContext';

const Link = ({ path, children }) => {
  const { setCurrentPath } = useContext(RouteContext);

  const handleClick = (e) => {
    e.preventDefault();
    window.history.pushState({}, '', path);
    setCurrentPath(path);
  };

  return (
    <a href={path} onClick={handleClick}>
      {children}
    </a>
  );
};

export default Link;
