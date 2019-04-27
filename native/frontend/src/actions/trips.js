import axios from 'axios';

import { GET_TRIPS } from './types';

// GET TRIPS
export const getTrips = () => dispatch => {
  axios.get('/api/trips/')
    .then(res => {
      dispatch({
        type: GET_TRIPS,
        payload: res.data
      });
    })
    .catch(err => console.log('err', err));
};
