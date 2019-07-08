import React from 'react';
import './list.css';

export default class extends React.Component{
    render() {
        const repo = this.props.repo;

        return(
            <li className="li_element">
            <a
                href={ repo.html_url}
                target="_blank"
                className="list"
               >
                {repo.name}
            </a>
            </li>

        );
    }
}