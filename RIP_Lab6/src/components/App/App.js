import React from 'react';
import './styles.css';
import Title from './components/Title/Title';
import ListItem from './components/ListItem/ListItem';
import axios from 'axios';


class App extends React.Component{
    constructor(props){
        super(props);
        this.state={
            titleColor: 'red',
            repos: []
            };
        this.onButtonClick = this.onButtonClick.bind(this);
        this.counter = true
    }
    onButtonClick(){
        if(this.counter) {
            this.setState(
                {
                    titleColor: 'blue'
                }
            );
            this.counter = false;
        }
        else{
            this.setState(
                {
                    titleColor: 'red'
                }
            );
            this.counter = true;
        }
    }
    componentDidMount() {
        this.setState(
            {
                isLoading: true
            }
        );
        axios.get('https://api.github.com/users/AVasilyev1998/repos').then(
            response =>
            {
                this.setState({
                    repos: response.data,
                    isLoading: false
                })
            },
            error => {
                this.setState({
                    isLoading: false
                })
            }
        )
    }

    render(){
        return(
            <div>
                <Title color={this.state.titleColor}/>
                {this.state.isLoading && <div>Загрузка...</div>}
                {
                    this.state.repos.map((repo,i) => <ListItem key={i} repo={repo}/>)
                }
                <div className="img"/>
                <div className="button" onClick={this.onButtonClick}>
                    Push
                </div>
            </div>
        )
    }
}

export default App;