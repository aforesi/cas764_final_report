import csv
import textdistance

##read csv file with data
dataFile = "";

##export csv file with all similarity scores and orginal data
exportDataFile = "";

with open(dataFile, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter= ',')
    with open(exportDataFile, 'w') as new_file:
        fieldnames = ['name1', 'name2', 'hamming', 'needleman_wunsch', 'gotoh', 'smith_waterman', 'levenshtein', 'damerau_levenshtein', 'jaro', 'strcmp95', 'jaccard', 'bag', 'dice', 'cosine', 'overlap', 'lcsseq', 'lcsstr']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter= ',', lineterminator='\n')
        csv_writer.writeheader()
        for line in csv_reader:
            if len(line):
                name1 = line["name1"]
                name2 = line["name2"]
                damerau_levenshtein = textdistance.damerau_levenshtein.normalized_similarity(line["name1"], line["name2"])
                gotoh = textdistance.gotoh.normalized_similarity(line["name1"], line["name2"])
                hamming = textdistance.hamming.normalized_similarity(line["name1"], line["name2"])
                jaro = textdistance.jaro.normalized_similarity(line["name1"], line["name2"])
                levenshtein = textdistance.levenshtein.normalized_similarity(line["name1"], line["name2"])
                needleman_wunsch = textdistance.needleman_wunsch.normalized_similarity(line["name1"], line["name2"])
                smith_waterman = textdistance.smith_waterman.normalized_similarity(line["name1"], line["name2"])
                strcmp95 = textdistance.strcmp95.normalized_similarity(line["name1"], line["name2"])
                bag = textdistance.bag.normalized_similarity(line["name1"], line["name2"])
                cosine = textdistance.cosine.normalized_similarity(line["name1"], line["name2"])
                dice = textdistance.sorensen.normalized_similarity(line["name1"], line["name2"])
                jaccard = textdistance.jaccard.normalized_similarity(line["name1"], line["name2"])
                overlap = textdistance.overlap.normalized_similarity(line["name1"], line["name2"])
                lcsseq = textdistance.lcsseq.normalized_similarity(line["name1"], line["name2"])
                lcsstr = textdistance.lcsstr.normalized_similarity(line["name1"], line["name2"])
                
                         
                csv_writer.writerow({
                    'name1' : name1, 
                    'name2': name2, 
                    'hamming': hamming, 
                    'needleman_wunsch': needleman_wunsch, 
                    'gotoh': gotoh, 
                    'smith_waterman': smith_waterman, 
                    'levenshtein': levenshtein, 
                    'damerau_levenshtein': damerau_levenshtein, 
                    'jaro': jaro,
                    'strcmp95': strcmp95, 
                    'jaccard': jaccard, 
                    'bag': bag, 
                    'dice': dice, 
                    'cosine': cosine, 
                    'overlap': overlap, 
                    'lcsseq': lcsseq, 
                    'lcsstr': lcsstr

                    })            
