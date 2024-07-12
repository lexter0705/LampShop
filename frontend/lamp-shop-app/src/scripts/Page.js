import { useContext } from 'react';
import RouteContext from './RouteContext';

const Page = ({ element, path }) => {
  const { currentPath } = useContext(RouteContext);

  return currentPath === path ? element : null;
};

export default Page;
