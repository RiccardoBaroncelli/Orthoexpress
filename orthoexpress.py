#! /usr/bin/python3

import pdb                                          # debugger library
import csv                                          # library for open and reading csv files


#MAIN
if __name__ == '__main__':

    #files
    inpFile_ortho="withsyn.proteinortho"

    deg_files = ["CPHO01_DGE_summary.txt", "CNYM01_DGE_summary.txt", "CHIG01_DGE_summary.txt", "CGRA01_DGE_summary.txt"]

    outfile="output_genes.txt"                 #main file output
    outfile_labeled="output_proteinortho_labeled.txt"     #multiple genes file output

    #open output files
    outfile_h = open(outfile, 'w')
    outfile_labeled_h = open(outfile_labeled, 'w')

    gene_data = dict()
    for file in deg_files:
        file_h = open(file, 'r')
        reader = csv.reader(file_h, delimiter='\t')
        next(reader, None)  # skip the header row
        for row in reader:
            row_name = '_'.join(row[0].split('|')[1:])
            #pdb.set_trace()
            gene_data[row_name] = '\t'.join(row)

    ortho_h = open(inpFile_ortho, 'r')
    reader = csv.reader(ortho_h, delimiter = '\t')
    next(reader, None)
    ortho_id = 0
    for row in reader:
        r3 = row[3].split(',')
        r4 = row[4].split(',')
        r5 = row[5].split(',')
        r6 = row[6].split(',')

        for gene3 in r3:
            for gene4 in r4:
                for gene5 in r5:
                    for gene6 in r6:
                        gene3_data  = gene_data.get(gene3, '\t\t\t\t\t\t\t\t\t')
                        gene4_data  = gene_data.get(gene4, '\t\t\t\t\t\t\t\t\t')
                        gene5_data  = gene_data.get(gene5, '\t\t\t\t\t\t\t\t\t')
                        gene6_data  = gene_data.get(gene6, '\t\t\t\t\t\t\t\t\t')
                        orthogroup_id = 'OG_' + str(ortho_id)
                        line_to_write = '{oid}\t{g3d}\t{g4d}\t{g5d}\t{g6d}\n'.format(oid=orthogroup_id, g3d=gene3_data, g4d=gene4_data, g5d=gene5_data, g6d=gene6_data)
                        outfile_h.write(line_to_write)

        labeled_to_write = '{oid}\t{rowdat}\n'.format(oid=orthogroup_id, rowdat = '\t'.join(row))
        outfile_labeled_h.write(labeled_to_write)
        ortho_id +=1


