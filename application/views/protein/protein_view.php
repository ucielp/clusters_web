	<title><?php echo $title ?></title> 




        <section id="subscribe" >
        <div class="container">
            <div class="row">
                <div class="col-md-12 wow fadeInDown" data-wow-delay=".8s">
                    <div class="block">
                        <div class="title text-center">
                            <h2>Search for protein</h2>
                            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Hic, non!</p>
                        </div>
                        

					  <?php 
					  $attributes = array('class' => 'form-inline text-center col-sm-12 col-xs-12');
					  echo form_open("protein/search/",$attributes);?>   
  
                          

                            <div class="form-group">
								<?php 
								$data = array(
									'name'          => 'protein_name',
									'id'            => 'search-form',
									'class'			=> 'form-control',
									//~ HACK
									//~ 'value'			=> 'PENBR_0004_03810'
									//~ this protein is in 6 cluster
									//~ 'value'			=> 'PESFI_0012_13937'
									'value'			=> 'ASPKA_0062_04984'
								);

							 echo form_input($data);
								
								?>
                            </div>

							 <?php
							  $attributes = array(
									'class' => 'btn btn-default btn-signup',
									'id' => 'submit', 
								);


							  echo form_submit('submit', 'Search',$attributes);

							  
							  ?>
									
									  
                    
                </div>
            </div>
        </div>
    </section>

