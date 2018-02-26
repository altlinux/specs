%define real_name mvapich
%define compiler gcc

Summary: MPI implementation over Infiniband RDMA-enabled interconnect
Name: %real_name-%compiler
Version: 1.2.0
Release: alt3

Provides: %real_name = %version-%release
Obsoletes: %real_name < %version-%release

%define mpi_device ch_gen2
%define full_name %name-%_host_cpu
%define mpi_prefix %_libexecdir/%full_name
%define mpi_sysconfdir %_sysconfdir/%full_name

License: BSD
Group: Development/Other
Source: %real_name-%version.tar
Patch: mvapich-0.9.9-1458-alt-buildreq.patch
Patch1: mvapich-1.0.1-alt-build.patch
Patch2: mvapich-1.0.1-alt-fpic.patch

Packager: Stanislav Ievlev <inger@altlinux.org>

URL: http://mvapich.cse.ohio-state.edu/

Requires(post,preun): mpi-selector >= 1.0.1-alt2
BuildPreReq: mpi-selector

BuildPreReq: libibumad-devel >= 1.2.3 libibverbs-devel >= 1.1.2
Requires: libibumad >= 1.2.3 libibverbs >= 1.1.2

# Automatically added by buildreq on Wed Jan 30 2008
BuildRequires: gcc-c++ gcc-fortran libibumad-devel libibverbs-devel

%description
This is high performance and scalable MPI-1 implementation over Infiniband and
RDMA-enabled interconnect.
This implementation is based on  MPICH and MVICH. MVAPICH is pronounced as
`em-vah-pich''. 

%package devel
Summary: development part of the %name
Group: Development/Other
Requires: %name = %version-%release
Requires: libibumad-devel libibverbs-devel
 
%description devel
development part of the %name

%package devel-doc
Summary: Documentation for the %name
Group: Development/Documentation
 
%description devel-doc
Documentation for the %name


%prep
%setup -q -n %real_name-%version
%patch -p1
%patch1 -p2
%patch2 -p2

%build
unset MPICH_CC
unset MPICH_CLINKER
unset MPICH_F77
unset MPICH_F77LINKER
unset MPICH_F90
unset MPICH_F90LINKER
unset I_MPI_ROOT

ARCH_NAME=
IB_INCLUDE=
IB_LIB=
OPTIMIZATION_FLAG="%optflags"
BIT=
CONFIG_ENABLE_F77="--enable-f77"
CONFIG_ENABLE_F90="--enable-f90"
EXTRA_CFLAG=
MPE_FLAGS=
buildidfile=BUILDID

# GNU compilers
%if %(test "%{compiler}" = "gcc" && echo 1 || echo 0)
    export CC=gcc
    export CXX=g++
    if ( which gfortran &>/dev/null ); then
        # new gcc version
        export FC=gfortran
        export F77=gfortran
        export F90=gfortran
        export F77_GETARGDECL=" "
    elif ( which g77 &>/dev/null ); then
        # old gcc version
        export FC=g77
        export F77=g77
        export F90=g77
    fi
    export CFLAGS="-Wall -DDISABLE_PTMALLOC"
    export FFLAGS=
    export CXXFLAGS=""
    export F90FLAGS=""
    export CONFIG_FLAGS=""
%endif
# Intel compiler
%if %(test "%{compiler}" = "intel" && echo 1 || echo 0)
    export CC=icc
    export CXX=icc
    export FC=ifort
    export F90=$FC
    export CFLAGS="-D__INTEL_COMPILER"
    export FFLAGS="-fPIC"
    export CXXFLAGS="-fPIC"
    export CCFLAGS="-lstdc++"
    export F90FLAGS=$FFLAGS
    export CONFIG_FLAGS=""
    export COMPILER_CONFIG="--enable-f90modules --with-romio"
%endif
# Pathscale compiler
%if %(test "%{compiler}" = "pathscale" && echo 1 || echo 0)
    export CC=pathcc
    export CXX=pathCC
    export FC=pathf90
    export F90=pathf90
    export F77=pathf90
    export CFLAGS=""
    export FFLAGS="-fPIC"
    export CXXFLAGS="-fPIC"
    export CCFLAGS=""
    export F90FLAGS=$FFLAGS
    export CONFIG_FLAGS=""
    export COMPILER_CONFIG="--enable-f90modules --with-romio"
%endif
# PGI compiler
%if %(test "%{compiler}" = "pgi" && echo 1 || echo 0)
    export CC=pgcc
    export CXX=pgCC
    export FC=pgf77
    export F90=pgf90
    export CFLAGS="-Msignextend -DPGI"
    export FFLAGS="-fPIC"
    export CXXFLAGS="-fPIC"
    export F90FLAGS=$FFLAGS
    export CONFIG_FLAGS=""
    export OPTIMIZATION_FLAG=""
%endif
#############################################################################

EXTRA_CFLAG="$CFLAGS -Wl,-R%mpi_prefix/lib -L%buildroot%mpi_prefix/lib"
#export MPI_LIBDIR=%mpi_prefix/lib
#EXTRA_CFLAG="$CFLAGS -L%buildroot%mpi_prefix/lib"

%ifarch %ix86
    ARCH_NAME="-D_IA32_"
%endif

%ifarch x86_64
    ARCH_NAME="-D_EM64T_"
%endif

# check for version
if [ -f $buildidfile ]; then
    buildid=`cat $buildidfile | grep MVAPICH_BUILDID |awk '{print $2}'`
    if [ "$buildid" != "" ];then
        DEF_BUILDID="$DEF_BUILDID -DMVAPICH_BUILDID=\\\"$buildid\\\""
    else
        DEF_BUILDID=""
    fi
fi

IB_INCLUDE=%_includedir
IB_LIB=%_libdir

export CFLAGS="-g $OPTIMIZATION_FLAG -DCOMPAT_MODE -DCH_GEN2 -DMEMORY_SCALE -D_AFFINITY_ $CFLAGS -D_SMP_ -D_SMP_RNDV_ -DVIADEV_RPUT_SUPPORT -DEARLY_SEND_COMPLETION -DLAZY_MEM_UNREGISTER $ARCH_NAME -I$IB_INCLUDE"
#TCP
#export CFLAGS=
#TCP
export USER_CFLAGS
export MPE_OPTS
export MPE_CFLAGS
export LDFLAGS
export CXXFLAGS="-g $CXXFLAGS"
export FFLAGS="-g $FFLAGS -L$IB_LIB $EXTRA_CFLAG"
export F90FLAGS="-g $F90FLAGS $EXTRA_CFLAG"
export CONFIG_FLAGS
export MPIRUN_CFLAGS="$MPIRUN_CFLAGS -DPARAM_GLOBAL=\\\"%mpi_sysconfdir/mvapich.conf\\\" -DLD_LIBRARY_PATH_MPI=\\\"%mpi_prefix/lib\\\" $DEF_BUILDID"

install -d %buildroot%mpi_prefix/lib
./configure \
     --without-mpe \
     --with-device=%mpi_device \
     --with-arch=LINUX \
     --prefix=%buildroot/%mpi_prefix \
     --enable-sharedlib=%buildroot%mpi_prefix/lib \
     $CONFIG_ENABLE_F77 \
     $CONFIG_ENABLE_F90 \
     $COMPILER_CONFIG \
     -lib="-L$IB_LIB -libverbs -libumad -libcommon -lpthread -lstdc++ $EXTRA_CFLAG" \
     -rsh=ssh \
     $MPE_FLAGS \
     $CONFIG_FLAGS

#TCP
#./configure \
#     --without-mpe \
#     --with-arch=LINUX \
#     --prefix=%buildroot/%mpi_prefix \
#     $CONFIG_ENABLE_F77 \
#     $CONFIG_ENABLE_F90 \
#     $COMPILER_CONFIG \
#     -rsh=ssh \
#     $MPE_FLAGS \
#     $CONFIG_FLAGS
#TCP

#NO SMP
%make

%install
%make install

install -d %buildroot/%_sysconfdir
mv %buildroot/%mpi_prefix/etc %buildroot/%mpi_sysconfdir
cp -a osu_benchmarks %buildroot/%mpi_prefix

find %buildroot -type f -print0 |
    xargs -r0 file |
    fgrep text |
    cut -d: -f1 | xargs -r \
		    sed -i \
	    		-e "s^prefix=%buildroot/%mpi_prefix^prefix=%mpi_prefix^g" \
    	    		-e "s^sysconfdir=.*^sysconfdir=%mpi_sysconfdir^g" \
    	    		-e "s^includedir=.*^includedir=%mpi_prefix/include^g" \
    	    		-e "s^libdir=.*^libdir=%mpi_prefix/lib^g" \
    	    		-e "s^bindir=.*^bindir=%mpi_prefix/bin^g" \
			-e "s^-L%buildroot^-L^g" \
			-e "s^-I%buildroot^-I^g"

# Additionally, create the mpivars.[c]sh files.
cat >%buildroot%mpi_prefix/bin/mpivars.csh <<EOF
if (\$?path) then
    if ( "\${path}" !~ *%mpi_prefix/bin* ) then
	set path = ( %mpi_prefix/bin \$path )
    endif
else
    set path = ( %mpi_prefix/bin )
endif

if (\$?LD_LIBRARY_PATH) then
    if ( "\$LD_LIBRARY_PATH" !~ *%mpi_prefix/lib* ) then
	setenv LD_LIBRARY_PATH %mpi_prefix/lib:\$LD_LIBRARY_PATH
    endif
else
    setenv LD_LIBRARY_PATH %mpi_prefix/lib:
endif

if (\$?MANPATH) then
    if ( "\$MANPATH" !~ *%mpi_prefix/man* ) then
	setenv MANPATH %mpi_prefix/man:\$MANPATH
    endif
else
    setenv MANPATH %mpi_prefix/man:
endif
EOF

cat >%buildroot%mpi_prefix/bin/mpivars.sh <<EOF
if ! echo \$PATH | grep -q %mpi_prefix/bin ; then
    PATH=%mpi_prefix/bin:\$PATH
fi

if ! echo \$LD_LIBRARY_PATH | grep -q %mpi_prefix/lib ; then
    LD_LIBRARY_PATH=%mpi_prefix/lib:\$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH
fi

if ! echo \$MANPATH | grep -q %mpi_prefix/man ; then
    MANPATH=%mpi_prefix/man:\$MANPATH
fi
EOF

rm -f %buildroot%mpi_prefix/bin/mpirun_dbg.ddd

%post
%post_mpi_selector %full_name %mpi_prefix/bin

%preun
%preun_mpi_selector %full_name

%files
%dir %mpi_prefix
%mpi_prefix/bin
%exclude %mpi_prefix/bin/mpif77
%exclude %mpi_prefix/bin/mpif90
%exclude %mpi_prefix/bin/mpicc
%exclude %mpi_prefix/bin/mpiCC
%exclude %mpi_prefix/bin/mpicxx
%mpi_prefix/sbin
%dir %mpi_prefix/lib
%mpi_prefix/lib/*.so.*

%dir %mpi_prefix/man/
%mpi_prefix/man/man1
%exclude %mpi_prefix/man/man1/mpicc*
%exclude %mpi_prefix/man/man1/mpiCC*
%exclude %mpi_prefix/man/man1/mpif*

%dir %mpi_sysconfdir
%config(noreplace) %mpi_sysconfdir/*.conf

%files devel
%mpi_prefix/bin/mpif77
%mpi_prefix/bin/mpif90
%mpi_prefix/bin/mpicc
%mpi_prefix/bin/mpicxx

%mpi_prefix/man/man1/mpicc*
%mpi_prefix/man/man1/mpiCC*
%mpi_prefix/man/man1/mpif*
%mpi_prefix/man/man3
%mpi_prefix/man/man4

%mpi_prefix/include
%mpi_prefix/lib/*.a
%mpi_prefix/lib/*.so
%mpi_prefix/osu_benchmarks

%files devel-doc
%mpi_prefix/doc
%mpi_prefix/examples
%mpi_prefix/www

%changelog
* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt3
- Rebuilt for debuginfo

* Thu Sep 02 2010 Andriy Stepanov <stanv@altlinux.ru> 1.2.0-alt2
- Rebuild with new libibumad

* Fri Aug 13 2010 Andriy Stepanov <stanv@altlinux.ru> 1.2.0-alt1
- Version 1.2.0

* Mon May 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Mon Nov 10 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt5
- fix build with gcc-4.3
- build with shared libraries

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt4
- rebuild with OFED 1.3.1

* Wed Sep 17 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt3
- build for Sisyphus

* Tue Sep 16 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt2
- special versions for each compiler type

* Thu Jun 19 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt1.M41.1
- build for 4.1

* Thu Jun 19 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sat May 24 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- 1.0
- fix build in Sisyphus

* Thu Jan 31 2008 Stanislav Ievlev <inger@altlinux.org> 0.9.9-alt2
- little spec improvements
- install osu_benchmarks

* Wed Jan 30 2008 Stanislav Ievlev <inger@altlinux.org> 0.9.9-alt1
- Initial build
