import React from 'react';
import './styles.css';
import PropTypes from 'prop-types';

const Title = props =>{
    const className = `title title_${props.color}`;
    return(
        <div className={className}>
            My first React App! Some text
        </div>
    )
}

Title.PropTypes = {
    color: PropTypes.oneOf(['blue','red']) // допустимые цвета
};

Title.DefaultProps = {
    color : 'blue'
};


export default Title;