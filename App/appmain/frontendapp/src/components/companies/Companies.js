import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import {getCompanies} from '../..actions/companies';
import companies from '../../reducers/companies';


export class Companies extends Component {
    static propTypes {
        companies: PropTypes.array.isRequired
    }

    render() {
        return (
            <div>
                <h1>Company list</h1>
            </div>
        )
    }
};

const mapStateToProps = state => ({
    companies: state.companies.companies
})

export default connect(Companies);
