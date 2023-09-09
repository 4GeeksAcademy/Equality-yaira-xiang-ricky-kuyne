import React, { useState, useEffect } from 'react';
import { useParams,useNavigate } from 'react-router';
import { Product } from '../pages/product';


export const SearchBar = () => {
    const [text, setText] = useState('');
    const [data, setData] = useState([]);
    const navigate = useNavigate();
    console.log(text);


    useEffect(() => { 
    async function fetchSearchResults () {  //this is fetching the data for the input
        let info = [];
        const result = await fetch(process.env.BACKEND_URL + 'api/products');
        const data = await result.json();
        data.results.forEach(element => {
            info.push(element)      //pushing the data into the info array
        });

        setData(info)
        console.log(info, 'info')

    }
    
    fetchSearchResults()

    }, [])

   console.log('data', data) 
   
    //fitler all names from the api object array that has the 'text' u typed 
   let filtered = data.filter(ProductTitle => {
        return ProductTitle.title.includes(text)
   })



    return(
    <div className='parentOfInput justify-content-end'>
    <form autoComplete='off'>
        <i class="fas fa-search me-2"></i>
        <input placeholder='search' type='text' value={text} onChange={(e) => setText(e.target.value) }></input>
    </form>
    
    <div className='searchDropdown'>
        {text.length ? filtered.map((item, index) => {
            return(
                <>
                {console.log(item)}

                <p onClick={() => {
                    let url = item.url;
                    let id = item.uid
                    if(url.includes('people')){
                        navigate(`/CharacterDescription/${id}`)
                    }
                    if(url.includes('product')){
                        navigate(`/product/${title}`)
                    }
                }} >{item.name}</p>
                
                </>
            )
        }) : ''}
        
    </div>
    </div>
    )
}

// reduce function can be used instead of mapping and filter