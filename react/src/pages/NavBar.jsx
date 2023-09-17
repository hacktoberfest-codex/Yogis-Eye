import { useState } from "react";
import { Link } from "react-router-dom";
import yogiseye from "../assets/yogiseye.png"

import close from "../assets/close.svg";
import menu from "../assets/menu.svg";



const NavBar = () => {
    //   const [active, setActive] = useState("Home");
    const [toggle, setToggle] = useState(false);

    return (
        <nav className="w-full flex py-4  justify-between  items-center  sticky top-0  p-4 bg-[#008081] z-20">

            <ul className="list-none sm:flex  hidden justify-around items-center flex-1">
                <li className="flex font-poppins font-normal cursor-pointer text-[18px]    ">
                    <img src={yogiseye}
                        alt="Medicinal Plant"
                        className="mx-auto h-10 w-[80px] rounded-3xl " />
                    <Link className="px-10 hover:text-black text-white " to="/">
                        Home
                    </Link>
                    <Link className="px-10 hover:text-white text-white" to="/upload">
                        Search Plant
                    </Link>
                    <Link className="px-10 hover:text-white text-white" to="/about">
                        About
                    </Link>

                </li>
                <button className="sm:p-4 p-2 text-sm bg-white rounded-md hover:text-white ">Get in touch</button>
            </ul>

            <div className="sm:hidden flex flex-1 justify-end items-center">
                <img
                    src={toggle ? close : menu}
                    alt="menu"
                    className="w-[38px] h-[28px] object-contain text-black"
                    onClick={() => setToggle(!toggle)}
                />

                <div
                    className={`${!toggle ? "hidden" : "flex"
                        } p-2  sm:p-6 bg-black-gradient absolute bg-[#66b2b2] top-0 right-2 mx-2 h-[40%]  sm:h-[70%]  min-w-[100px] w-[50%] rounded-xl `}
                >
                    <ul className="list-none flex justify-center items-center flex-1 flex-col ">
                        <li className="flex flex-col font-poppins font-normal cursor-pointer text-[13px]   ">
                            <Link className="py-10" to="/">
                                Home
                            </Link>
                            <Link className="py-10" to="/doctor">
                                upload your image
                            </Link>

                        </li>
                        <button className="p-4 bg-white rounded-md text-black">Get in touch</button>
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default NavBar;
