//meeting place for all other reducers

import { combineReducers } from 'redux';
import trips from './trips';

export default combineReducers({
  trips
});
