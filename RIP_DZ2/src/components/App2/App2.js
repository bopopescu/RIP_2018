import React from 'react';
import './styles.css';


class App2 extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            titleColor: 'red',
            repos: []
        };
        this.onButtonClick = this.onButtonClick.bind(this);
        this.counter = true


        render()
        {
            return (
                <div>
                    <Title color={this.state.titleColor}/>
                    {this.state.isLoading && <div>Загрузка...</div>}
                    {
                        this.state.repos.map((repo, i) => <ListItem key={i} repo={repo}/>)
                    }
                    <div className="img"/>
                    <div className="button" onClick={this.onButtonClick}>
                        Push
                    </div>
                </div>
            )
        }
    }
}

export default App2;