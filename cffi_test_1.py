from cffi import FFI

ffi = FFI()
ffi.cdef(
	"""
	int main(int mu);
	"""
	)

lib = ffi.verify(
"""
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <ida/ida.h>
#include <ida/ida_band.h>
#include <sundials/sundials_dense.h>
#include <nvector/nvector_serial.h>
#include <sundials/sundials_types.h>
#include "basic_pde_solver.c"
""", include_dirs=['.','/usr/local/include'],
#libraries=['liblapack.so.3gf', 'libblas.so.3gf','librt'], 
libraries=['sundials_ida','sundials_nvecserial'],
#library_dirs=['usr/local/lib','/usr/lib/x86_64-linux-gnu', '/usr/lib'], 
library_dirs=['/usr/local/lib'],
#extra_compile_args=['-o','-DNDEBUG']
)