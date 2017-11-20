--
-- Database: `clusters`
--

-- --------------------------------------------------------

--
-- Table structure for table `cluster_families`
--

CREATE TABLE `cluster_families` (
  `id` int(11) NOT NULL,
  `cluster_code` varchar(10) NOT NULL,
  `specie_code` varchar(10) NOT NULL,
  `protein_code` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cluster_families`
--
ALTER TABLE `cluster_families`
  ADD PRIMARY KEY (`id`),
  ADD KEY `protein_id` (`protein_code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cluster_families`
--
ALTER TABLE `cluster_families`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


-- ~ cluster_families -> 2,250,117 total


--
-- Table structure for table `taxonomy`
--

CREATE TABLE `taxonomy` (
  `id` int(11) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `specie_code` varchar(100) NOT NULL,
  `specie_name` varchar(100) NOT NULL,
  `kingdom` varchar(100) NOT NULL,
  `phylum` varchar(100) NOT NULL,
  `subphylum` varchar(100) NOT NULL,
  `class` varchar(100) NOT NULL,
  `order_tax` varchar(100) NOT NULL,
  `family` varchar(100) NOT NULL,
  `genus` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for table `taxonomy`
--
ALTER TABLE `taxonomy`
  ADD PRIMARY KEY (`id`),
  ADD KEY `specie_code` (`specie_code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `taxonomy`
--
ALTER TABLE `taxonomy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
  
  
  
-- --------------------------------------------------------

--
-- Table structure for table `all_trees`
--

CREATE TABLE `all_trees` (
  `family` int(11) NOT NULL,
  `tree` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `all_trees`
--
--
-- Indexes for dumped tables
--

--
-- Indexes for table `all_trees`
--
ALTER TABLE `all_trees`
  ADD UNIQUE KEY `family` (`family`);

-- --------------------------------------------------------

--
-- Table structure for table `secondary_metabolism`
--

CREATE TABLE `secondary_metabolism` (
  `id` int(11) NOT NULL,
  `cluster_code` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `secondary_metabolism`
--
ALTER TABLE `secondary_metabolism`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `secondary_metabolism`
--
ALTER TABLE `secondary_metabolism`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
