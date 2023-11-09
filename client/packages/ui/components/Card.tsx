import React, { useState, useEffect } from 'react';
import {
  Spinner,
  Card,
  H2, H1, Paragraph, SizableText, Square
} from '@my/ui';
import { LinearGradient } from '@tamagui/linear-gradient'

function MemoryCard() {
  const [ memoryUsage, setMemoryUsage ] = useState(null);

  useEffect(() => {
    fetchMemory();

    const intervalId = setInterval(() => {
      fetchMemory();
    }, 3000); // make a request every 3 seconds

    return () => clearInterval(intervalId); // clean up the interval on unmount
  }, []);

  const fetchMemory = async () => {
    const response = await fetch('http://localhost:5000/memory');
    if (response.ok) {
      console.log("fetched");
      const data = await response.json();
      let jsonData = JSON.parse(JSON.stringify(data));
      setMemoryUsage(jsonData[ 'memory_usage' ]);
      console.log(memoryUsage);
    } else {
      console.error('Failed to retrieve emote:', response.statusText);
    }
  };

  return (


    <Card space="$1" alignItems="left" padded>
      <Card.Header>
        <H2>        {memoryUsage === null && <Spinner size="large" />}
          {memoryUsage !== null && memoryUsage}</H2>
        <Paragraph theme="alt">Memory Usage</Paragraph>
      </Card.Header>
      <Card.Background>
        {/* <LinearGradient
          opacity={0.7}
          borderRadius="$4"
          colors={[ '$red8', '$green10' ]}
          flex={memoryUsage/100} /> */}
      <Square backgroundColor="$green10"  opacity={1} flex={memoryUsage/100}/>
      </Card.Background>
    </Card>


  );
}

export default MemoryCard;
