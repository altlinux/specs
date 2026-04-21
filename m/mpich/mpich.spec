%define _unpackaged_files_terminate_build 1

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%def_with devel
%def_with doc

Name:    mpich
Version: 5.0.1
Release: alt1

Summary: Official MPICH Repository
License: BSD
Group:   System/Libraries
Url:	 https://www.mpich.org/
Vcs:     https://github.com/pmodels/mpich.git

%define mpich_dir %_libdir/%name

Source0: %name-%version.tar
Source1: modules.tar

%filter_from_requires /^\/usr\/bin\/bash/d

BuildRequires(pre): rpm-macros-mpi-selector rpm-macros-valgrind
BuildRequires: mpi-selector

Patch0: 0001-Skip-submodules-check-in-autogen.sh.patch

BuildRequires: gcc-c++
BuildRequires: gcc-fortran
BuildRequires: libhwloc-devel
BuildRequires: libfabric-devel
BuildRequires: libyaksa-devel
%ifarch aarch64 x86_64
BuildRequires: libucx-devel
%endif
BuildRequires: libjson-c-devel
BuildRequires: python3-devel
BuildRequires: rdma-core-devel
BuildRequires: libnl-devel
BuildRequires: libnuma-devel

%description
MPICH is a high-performance and widely portable implementation of the Message
Passing Interface (MPI) standard (MPI-1, MPI-2 and MPI-3). The goals of MPICH
are: (1) to provide an MPI implementation that efficiently supports different
computation and communication platforms including commodity clusters (desktop
systems, shared-memory systems, multicore architectures), high-speed networks
(10 Gigabit Ethernet, InfiniBand, Myrinet, Quadrics) and proprietary high-end
computing systems (Blue Gene, Cray) and (2) to enable cutting-edge research in
MPI through an easy-to-extend modular framework for other derived
implementations.

The mpich binaries in this RPM packages were configured to use the default
process manager (Hydra) using the default device (ch3). The ch3 device
was configured with support for the nemesis channel that allows for
shared-memory and TCP/IP sockets based communication.

This build also include support for using the 'module environment' to select
which MPI implementation to use when multiple implementations are installed.
If you want MPICH support to be automatically loaded, you need to install the
mpich-autoload package.

%if_with devel
%package devel
Summary: Development files for mpich
Group: Development/C
Requires: %name = %EVR

%description devel
Contains development headers and libraries for mpich.
%endif

%if_with doc
%package doc
Summary: Documentations and examples for mpich
Group: Documentation
Requires: %name-devel = %EVR

%description doc
Contains documentations, examples and man-pages for mpich.
%endif

%prep
%setup -a1
%autopatch -p1

%build
# Disable ROMIO tests during build
# Reason: Tests require running mpicc from the /usr/lib64/mpich/bin/ directory, which
# is not available in the chroot environment used for building the RPM.
# Running the tests would fail and break the package build.
sed -i 's/^\(SUBDIRS *=.*\) test/\1/' src/mpi/romio/Makefile.am

./autogen.sh

CONFIGURE_OPTS=(
        --with-custom-version-string=%version-%release
        --enable-sharedlibs=gcc
        --enable-shared
        --enable-static=no
        --enable-lib-depend
        --disable-rpath
        --disable-silent-rules
        --disable-dependency-tracking
        --with-gnu-ld
        --includedir=%_includedir/%name-%_arch
        --bindir=%mpich_dir/bin
        --libdir=%mpich_dir/lib
        --datadir=%_datadir/%name
        --mandir=%_mandir/%name-%_arch
        --docdir=%_datadir/%name/doc
        --htmldir=%_datadir/%name/doc
        --with-hwloc
        --with-libfabric
%ifarch x86_64 aarch64 
        --with-ucx
%endif
        --with-yaksa
)

%configure "${CONFIGURE_OPTS[@]}"  \
    --disable-romio-tests

%make_build VERBOSE=1 

%install
%makeinstall_std CC=%buildroot%mpich_dir/bin/mpicc 

# Install the module file
mkdir -p %buildroot%_datadir/modulefiles/mpi
sed -r 's|%_bindir|%mpich_dir/bin|;
        s|@LIBDIR@|%mpich_dir|;
        s|@MPINAME@|%name|;
        s|@py2sitearch@|%python_sitelibdir|;
        s|@py3sitearch@|%python3_sitelibdir|;
        s|@ARCH@|%_arch|;
     ' \
     <src/packaging/envmods/mpich.module \
     >%buildroot%_datadir/modulefiles/mpi/%name-%_arch

#Delete rpath
sed -r -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -r -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# Create cmake directory
install -d %{buildroot}%mpich_dir/lib/cmake \
           %{buildroot}%mpich_dir/include

find %{buildroot} -type f -name "*.la" -delete

rm -f %{buildroot}%mpich_dir/bin/parkill

cat >%buildroot%mpich_dir/bin/mpivars.sh <<'EOF'
if ! echo $PATH | grep -q %mpich_dir/bin ; then
    PATH=%mpich_dir/bin:$PATH
    export PATH
fi

if ! echo $LD_LIBRARY_PATH | grep -q %mpich_dir/lib ; then
    LD_LIBRARY_PATH=%mpich_dir/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
    export LD_LIBRARY_PATH
fi

if ! echo $MANPATH | grep -q %mpich_dir/man ; then
    MANPATH=%mpich_dir/man:$MANPATH
    export MANPATH
fi
EOF

cat >%buildroot%mpich_dir/bin/mpivars.csh <<'EOF'
if ($?path) then
    if ( "$path" !~ *%mpich_dir/bin* ) then
        set path = ( %mpich_dir/bin $path )
    endif
else
    set path = ( %mpich_dir/bin )
endif

if ($?LD_LIBRARY_PATH) then
    if ( "$LD_LIBRARY_PATH" !~ *%mpich_dir/lib* ) then
        setenv LD_LIBRARY_PATH %mpich_dir/lib:$LD_LIBRARY_PATH
    endif
else
    setenv LD_LIBRARY_PATH %mpich_dir/lib
endif

if ($?MANPATH) then
    if ( "$MANPATH" !~ *%mpich_dir/man* ) then
        setenv MANPATH %mpich_dir/man:$MANPATH
    endif
else
    setenv MANPATH %mpich_dir/man
endif
EOF

%post
%post_mpi_selector %name %mpich_dir/bin

%preun
%preun_mpi_selector %name

%files
%doc COPYRIGHT CHANGES README README.vin 
%dir %mpich_dir
%dir %mpich_dir/lib
%dir %mpich_dir/bin
%dir %mpich_dir/lib/cmake
%dir %mpich_dir/include
%mpich_dir/lib/*.so.*
%mpich_dir/bin/hydra*
%mpich_dir/bin/mpichversion
%mpich_dir/bin/mpiexec*
%mpich_dir/bin/mpirun
%mpich_dir/bin/mpivars
%mpich_dir/bin/mpivars.*
%_datadir/modulefiles/mpi/
%_sysconfdir/mpixxx_opts.conf

%if_with devel
%files devel
%_includedir/%name-%_arch/
%mpich_dir/lib/pkgconfig
%mpich_dir/lib/cmake
%mpich_dir/lib/*.so
%mpich_dir/bin/mpicc
%mpich_dir/bin/mpic++
%mpich_dir/bin/mpicxx
%mpich_dir/bin/mpif77
%mpich_dir/bin/mpif90
%mpich_dir/bin/mpifort
%endif

%if_with doc
%files doc
%dir %_datadir/%name
%_datadir/%name/doc/
%endif

%changelog
* Mon Apr 20 2026 Nikita Shmatko <nash@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Mon Oct 13 2025 Nikita Shmatko <nash@altlinux.org> 4.3.1-alt1
- Initial build for Sisyphus.
