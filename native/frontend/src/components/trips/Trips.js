import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getTrips } from '../../actions/trips';

export class Trips extends Component {
  static propTypes = {
    trips: PropTypes.array.isRequired
  }

  componentDidMount() {
    this.props.getTrips();
  }

  render() {
    return (
      <Fragment>
        <h1>Trips</h1>
      </Fragment>
    )
  }
}

const mapStateToProps = state => ({
  trips: state.trips.trips
});

export default connect(mapStateToProps, { getTrips })(Trips);
