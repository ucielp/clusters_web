<?php

class Protein_model extends CI_Model {


	public function __construct()
	{
			parent::__construct();
	}


	//~ public function get_cluster_code($protein_code)
	//~ {

			//~ $query = $this->db->get_where('cluster_families', array('protein_code' => $protein_code));
			//~ foreach ($query->result_array() as $row ) {
					//~ $this->get_proteins_in_cluster($row['cluster_code']);

			//~ }

	//~ }
	
	//~ public function get_proteins_in_cluster($cluster_code)
	//~ {

			//~ $query = $this->db->get_where('cluster_families', array('cluster_code' => $cluster_code));
			//~ return $query->result_array();

	//~ }
	public function get_proteins_in_cluster_by_protein_code($protein_code)
	{


			$this->db->select('a.cluster_code, a.protein_code,a.specie_code');
			$this->db->from('cluster_families AS a');
			$this->db->join('cluster_families as b', 'a.cluster_code = b.cluster_code', 'left');
			$this->db->where('b.protein_code', $protein_code);
			//~ $this->db->order_by('a.cluster_code, a.specie_code,a.protein_code');
			
			$query = $this->db->get();


			$result_array =  $query->result_array();


			foreach ($result_array as $results){
				$prot_array[$results['cluster_code']][$results['specie_code']][] = $results['protein_code'];
			}
				
			return $prot_array;
	}
}
