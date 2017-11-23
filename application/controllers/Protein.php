<?php
class Protein extends CI_Controller {

        public function __construct()
        {
                parent::__construct();
                $this->load->model('protein_model');
                $this->load->helper('url_helper');
                $this->load->helper('form');
                $this->load->database();
                $this->load->library('table');


        }

        public function index()
		{

				$data['title'] = 'Protein';
				$this->load->view('templates/header', $data);
				$this->load->view('protein/protein_view', $data);
				$this->load->view('templates/footer');
		}

        public function search($protein_code = NULL)
		{


				

				$protein_name = $this->input->post('protein_name');
				$data['title'] = $protein_name;
				
				# Method to ger protein_code from protein_name
				$protein_code = $protein_name;

				$data['results'] = $this->protein_model->get_proteins_in_cluster_by_protein_code($protein_code);
				
				# Enable profiler
				$this->output->enable_profiler(TRUE);

	
				//~ if (empty($results))
				//~ {
						//~ show_404();
				//~ }

			
				$this->load->view('templates/header', $data);
				$this->load->view('protein/protein_go_view', $data);
				$this->load->view('templates/footer');
		}
}
