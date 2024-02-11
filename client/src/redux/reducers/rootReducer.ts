
import { combineReducers } from '@reduxjs/toolkit';
import accountsReducer from './accountsReducer';
import analyticsReducer from './analyticsReducer';
import authenticationReducer from './authenticationReducer';
// Import other reducers as needed

const rootReducer = combineReducers({
  accounts: accountsReducer,
  analytics: analyticsReducer,
  authentication: authenticationReducer,
  // Add other reducers here
});

export default rootReducer;
