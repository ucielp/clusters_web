	<title><?php echo $title ?></title> 


        <section id="subscribe" >
        <div class="container">
            <div class="row">
                <div class="col-md-12 wow fadeInDown" data-wow-delay=".8s">
                    <div class="block">
                      
                      <?php 
                        $last_specie = '';
						foreach($results as $cluster_code => $specie_protein){
							print $cluster_code . "<br>";
							foreach ($specie_protein as $specie_code => $proteins_code){
								print $specie_code . "<br>";
									foreach($proteins_code as $protein_code){
										print $protein_code . ";";
									}
								print "</br>";

							}
							print "</br>";

							//~ print "<p> " . $row['protein_code'] . "</p>" ;
						}
                      ?>

                </div>
            </div>
        </div>
    </section>

