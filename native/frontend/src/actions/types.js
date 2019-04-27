export const GET_TRIPS = "GET_TRIPS";

const initialState = {
  leads: []
}

export default function(state = initialState, action) {
  switch(action.type) {
    case GET_TRIPS:
      return {
        ...state,
        trips: action.payload
      };
    default:
      return state;
  }
}
