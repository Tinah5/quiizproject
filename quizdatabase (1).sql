-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 09, 2022 at 05:45 AM
-- Server version: 8.0.18
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quizdatabase`
--

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `QID` int(11) DEFAULT NULL,
  `qstn` text COLLATE utf8mb4_general_ci,
  `opA` text COLLATE utf8mb4_general_ci,
  `opB` text COLLATE utf8mb4_general_ci,
  `opC` text COLLATE utf8mb4_general_ci,
  `opD` text COLLATE utf8mb4_general_ci,
  `ans` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`QID`, `qstn`, `opA`, `opB`, `opC`, `opD`, `ans`) VALUES
(1, 'What is the key word use to define a function in Python?', 'DEF', 'def', 'Def', 'None of Above', 2),
(2, 'How can we generate random numbers in python using methods?', 'random.uniform ()', 'random.randint()', 'random.random()', 'All of the above', 4),
(3, 'What is the data type use to store decimal numbers in Python ?', 'string', 'Integer', 'float', 'Boolean', 3),
(4, 'What can you see when you run this python statement ?  [1, 2, 3] + [4, 5, 6]', 'error', '\"[1, 2, 3] + [4, 5, 6]\"', '\"[1,2,3,4,5,6]\"', '\"[1,2,3]\"', 3),
(5, 'What is the out put of this statement ?   Hello World * 4', 'Hello World', 'Hello , Hello ', 'Hello World , Hello World ', 'Noe of the above ', 4),
(6, 'What will be the out put of this statement ?  3 in [1, 2, 3]', 'True ', 'False ', 'TRUE', 'FALSE', 1),
(7, 'What is the widget can use to get user inputs in Python GUI programming?', 'Entry  Widget', 'Output Widget', 'Text box Widget', 'Button Widget', 1),
(8, 'Which of the following \"Python\" data type is mutable?', 'Numbers', 'List', 'Tuple', 'String', 2),
(9, 'Which of the followings consist iterable object in \"Python\"?', ' strings', 'lists', 'tuples', 'Number', 4),
(10, 'Which of the following library use in Python GUI? ', 'CSV', 'Random', 'tkinter', 'None of the above', 3),
(11, 'What are the data types of the following Python values respectively? \"Aruna\"    2345', 'String , Integer', 'Integer , String ', 'String , String ', 'None of the above', 1),
(12, 'What is the valid variable name from the followings?', '234_345', 'name', 'float', 'else', 2),
(13, 'What are the  key words use to define loops in Python?', 'else , if', 'for , while', 'for , if ', 'None of Above', 2),
(14, 'Which of the followings give  numbers from 0 to 10 ?', 'range(0,10)', 'range(1,11)', 'range(10)', 'range(11)', 4),
(15, 'What is the data type use to store integer numbers in Python ?', 'string', 'Integer', 'float', 'Boolean', 2),
(16, 'What can you see when you run this python statement ?  Print( \" Python \" + \"  Programming \" )', 'Programming', 'Python', 'Python Programming ', 'Error', 3),
(17, 'What is the out put of this statement ?   Print( \"Hello World \") ', 'Hello World', 'Hello , Hello ', 'Hello World , Hello World ', 'Noe of the above ', 1),
(18, 'What will be the out put of this statement ?  3 in (6,7,8)', 'True ', 'False ', 'TRUE', 'FALSE', 2),
(19, 'What is the widget can use to get radio buttons in Python GUI programming?', 'Radiobutton Widget', 'Radio Widget', 'Text box Widget', 'Button Widget', 1),
(20, 'Which of the following \"Python\" data type is not immutable?', 'Numbers', 'List', 'Tuple', 'String', 2);

-- --------------------------------------------------------

--
-- Table structure for table `reg`
--

CREATE TABLE `register` (
  `Firstname` char(30) DEFAULT NULL,
  `Lastname` char(30) DEFAULT NULL,
  `email` char(30) DEFAULT NULL,
  `uname` char(30) DEFAULT NULL,
  `password` char(100) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `user` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `reg`
--

INSERT INTO `register` (`Firstname`, `Lastname`, `email`, `uname`, `password`, `score`, `user`) VALUES
('wwww', 'aaaa', 'aa@gmail.com', 'wwww', '12345678', 0, NULL),
('eeee', 'qqqq', 'aa@gmail.com', 'gggg', '12345678', 1, 0),
('yyyy', 'ttttt', 'we@gmail.com', 'vvvv', '12345678', 0, 1),
('nimal', 'perera', 'nimal@gmail.com', 'nimal', '12345678', 3, 2),
('Kamal', 'Ekanayaka', 'kamal@gmail.com', 'Kamal', '12345678', 5, 2),
('Damitha', 'Perara', 'damitha@gmail.com', 'damitha', '12345678', 0, 1),
('gayomi', 'Ariyathilaka', 'ga@gmail.com', 'gayomi', '12345678', 0, 1),
('ganga', 'perera', 'ganga@gmail.com', 'ganga', '12345678', 3, 2),
('gayani', 'Perera', 'ga@gmail.com', 'gayani', '12345678', 0, 1),
('namal', 'perara', 'namal@gmail.com', 'namal', '12345678', 2, 2);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
