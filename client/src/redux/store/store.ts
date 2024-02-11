import { configureStore } from '@reduxjs/toolkit';
import rootReducer from './reducers';

const store = configureStore({
    reducer: rootReducer,
    // Add any middleware or enhancers here
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;