DATA = [
    {
        'SeqID': 12345,
        'SeqVersion': 1,
        'CompleteFragement': 'GUAGGA,--GUCUC,----A,-GA-CGA-UCCUG-AGCU,--AA---CGA',
        'AccessionID': 'GB123456',
        'TaxID': 12345,
        'ScientificName': 'Testus testus',
        'LineageName': 'Undefined \ Testus testus'
    },
    {
        'SeqID': 2188,
        'SeqVersion': 1,
        'CompleteFragement': 'G-G-------------------------A-G--U-A-C-G',
        'AccessionID': 'X74066',
        'TaxID': 435,
        'ScientificName': 'Acetobacter aceti',
        'LineageName': 'root \ cellular organisms \ Bacteria \ Proteobacteria \ Alphaproteobacteria \ Rhodospirillales \ Acetobacteraceae \ Acetobacter \ Acetobacter subgen. Acetobacter \ Acetobacter aceti'
    }
]

LIST_OPTIONS = [
    {
        'description': u'Thermus thermophilus SSU rRNA (Bacterial SSU rRNA Seed Alignment)',
        'chain_id': u'A',
        'model_number': 1,
        'requires_translation': True,
        'pdb': u'1FJG',
        'option': 1
    },
    {
        'description': u'Escherichia coli SSU rRNA (Bacterial SSU rRNA Seed Alignment)',
        'chain_id': u'A',
        'model_number': 1,
        'requires_translation': False,
        'pdb': u'2AW7',
        'option': 1
    },
    {
        'description': u'Escherichia coli FSU rRNA (Bacterial-Chloroplast-Mitochondrial FSU rRNA Alignment)',
        'chain_id': u'A',
        'model_number': 1,
        'requires_translation': False,
        'pdb': u'2QBG',
        'option': 1
    },
    {
        'description': u'TEST Escherichia coli LSU rRNA (Bacterial LSU rRNA Private Alignment)',
        'chain_id': u'B',
        'model_number': 1,
        'requires_translation': False,
        'pdb': u'2QBG',
        'option': 1
    },
    {
        'description': u'Escherichia coli SSU rRNA (Bacterial SSU rRNA Seed Alignment)',
        'chain_id': u'A',
        'model_number': 1,
        'requires_translation': False,
        'pdb': u'4KJA',
        'option': 1
    }
]

LIST_STRUCTURES = [
    {
        'taxonomy': u'Bacteria ',
        'organism': u'Thermus thermophilus ',
        'pdb': u'1FJG',
        'contents': u'30S (small) ribosomal subunit ',
        'model_number': 1
    },
    {
        'taxonomy': u'Bacteria ',
        'organism': u'Escherichia coli ',
        'pdb': u'2AW7',
        'contents': u'30S (small) ribosomal subunit ',
        'model_number': 1
    },
    {
        'taxonomy': u'Bacteria ',
        'organism': u'Escherichia coli ',
        'pdb': u'2QBG',
        'contents': u'50S (large) ribosomal subunit ',
        'model_number': 1
    },
    {
        'taxonomy': u'Bacteria ',
        'organism': u'Escherichia coli ',
        'pdb': u'4KJA',
        'contents': u'30S (small) ribosomal subunit ',
        'model_number': 1
    }
]