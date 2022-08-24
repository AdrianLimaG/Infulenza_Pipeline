# HEADER
PARAM_FILE_NAME="FLU-ref"
PARAM_FILE_AUTHOR="S. Shepard"
PARAM_FILE_VERSION="1.0"
PARAM_FILE_DATE="2015-12-21"

# Alternative reference
CUSTOM_REF_FILE="example.fasta"	# custom ref file

ASSEM_REF=1
MAX_ROUNDS=1
MAX_ITER_ASSEM=1
INS_T=2
DEL_T=2

MATCH_PROG="BLAT"
SORT_PROG="BLAT"
ALIGN_PROG="BLAT"

# REFERENCE SET
REF_SET=$(dirname $REF_SET)/$CUSTOM_REF_FILE