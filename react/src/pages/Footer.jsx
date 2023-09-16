import React from 'react';

const Footer = () => {
    return (
        <footer className=" bg-[#008080] py-5 text-white fixed bottom-0 w-full ">
            <div className="container mx-auto text-center ">
                <p className="text-sm">&copy; {new Date().getFullYear()} Yogi's eye . All rights reserved.</p>
            </div>
        </footer>
    );
};

export default Footer;
