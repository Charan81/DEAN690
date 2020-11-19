-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Oct 10, 2020 at 07:24 PM
-- Server version: 5.7.26
-- PHP Version: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `business_unit` varchar(4000) DEFAULT NULL,
  `psc_code` varchar(100) DEFAULT NULL,
  `obj_code` varchar(100) DEFAULT NULL,
  `sub_obj_descr` varchar(4000) DEFAULT NULL,
  `order_date` DATETIME,
  'order_title' varchar(4000) DEFAULT NULL,
  'line_description' varchar(4000) DEFAULT NULL,
  `vendor_name` varchar(400) DEFAULT NULL,
  `vendor_country` varchar(400) DEFAULT NULL,
  `cost` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product`
--

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`ID`);
