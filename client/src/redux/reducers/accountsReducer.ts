import { Reducer } from 'redux';
import { UserActionTypes, UserState, UserAction } from './types';

const initialState: UserState = {
    user: null,
    loading: false,
    error: null,
};

const userReducer: Reducer<UserState, UserAction> = (state = initialState, action) => {
    switch (action.type) {
        case UserActionTypes.FETCH_USER_REQUEST:
            return {
                ...state,
                loading: true,
                error: null,
            };
        case UserActionTypes.FETCH_USER_SUCCESS:
            return {
                ...state,
                user: action.payload,
                loading: false,
                error: null,
            };
        case UserActionTypes.FETCH_USER_FAILURE:
            return {
                ...state,
                loading: false,
                error: action.payload,
            };
        default:
            return state;
    }
};

export default userReducer;