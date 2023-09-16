import React from 'react';
import ram_tulsi from "../assets/ram_tulsi.jpg"
import { useSpring, animated } from 'react-spring';

const Home = () => {
    const springProps = useSpring({
        opacity: 1,
        transform: 'translateY(0px)',
        from: { opacity: 0, transform: 'translateY(-50px)' },
        delay: 500, // Add a delay to the animation
    });

    return (
        <div className="min-h-screen  flex flex-row items-center sm:justify-end sm:justify-center mb-8">
            <animated.div style={springProps} className="text-center">
                <h1 className="sm:text-5xl text-xl font-bold text-white  mb-4">
                    Want to know about medicinal plants ?
                </h1>
                <h2 className="text-3xl text-gray-700 mb-8">
                    You are in the right place
                </h2>
                
                <img
                    src={ram_tulsi}
                    alt="Medicinal Plant"
                    className="mx-auto h-74 w-[800px] rounded-3xl "
                />
            </animated.div>
        </div>
    );
};

export default Home;
