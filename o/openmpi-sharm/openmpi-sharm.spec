%define _unpackaged_files_terminate_build 1
%define mpi_soversion 40
%define openshmem_soversion 40
%define open_pal_soversion 80

Name: openmpi-sharm
Version: 5.0.7
Release: alt1
Summary: A High Performance MPI Library with a shared memory collectivies

License: BSD
Group: Development/Other

Url: https://github.com/r9odt/ompi
Vcs: https://github.com/r9odt/ompi

Source0: %name-%version.tar
Source1: %name-%version-oac.tar

Patch0: %name-doc-5.0.7-alt1-add-version-file-to-submodules.patch

# Unsupported architecture by UCX
ExcludeArch: i586

BuildRequires(pre): rpm-macros-mpi-selector
BuildRequires: flex libevent-devel
BuildRequires: libucx-devel ucc-devel libhwloc-devel openpmix-devel prrte-devel
BuildRequires: chrpath zlib-devel
# HWLOC Support configure requirementes below
BuildRequires: libxml2-devel liblzma-devel
# Documentation build requirements (docs/requirements.txt)
BuildRequires: python3-module-sphinx python3-module-recommonmark
BuildRequires: python3-module-docutils python3-module-sphinx_rtd_theme

Requires(post,preun): mpi-selector
Requires: prrte

%description
A High Performance Message Passing Library with a shared memory collectivies.
Coponent SHARM (SHARed Memory) implements a set of blocking collective
communication.
Package contains coll/sharm component for shared-memory based collectivies.

%package -n %name-devel
Summary: Development files for Open MPI
Group: System/Libraries

%description -n %name-devel
Development files for Open MPI.

%package -n %name-doc
Summary: Documentation for Open MPI
Group: System/Libraries
Requires: %name = %EVR

%description -n %name-doc
Documentation for Open MPI.

%prep
%setup -a1

%patch0 -p1

%build

%define prefix %_libdir/%name
%define sysconfig_prefix %_sysconfdir/%name
%define data_prefix %_datadir/%name
%define bin_prefix %prefix/bin
%define lib_prefix %prefix/lib
%define include_prefix %_includedir/%name
%define localstate_prefix %_runtimedir/%name
%define man_prefix %_mandir/%name
export CFLAGS="-Wno-incompatible-pointer-types -Wno-int-conversion"
./autogen.pl \
    --no-3rdparty="openpmix,prrte"
%configure \
    --prefix=%prefix \
    --sysconfdir=%sysconfig_prefix \
    --datarootdir=%data_prefix \
    --datadir=%data_prefix \
    --bindir=%bin_prefix \
    --libdir=%lib_prefix \
    --mandir=%man_prefix \
    --includedir=%include_prefix \
    --localstatedir=%localstate_prefix \
    --disable-static \
    --with-sysroot=%prefix

%make_build

%install
%makeinstall_std

rm %buildroot%lib_prefix/*.la
rm %buildroot%lib_prefix/openmpi/libompi_dbg_msgq.la

fix_rpath() {
    # Cut /usr/lib64 from rpath
    fixed_path=$(chrpath -l ${1?} | cut -d'=' -f2 | sed 's;\(^/usr/lib64$\|:/usr/lib64$\|^/usr/lib64:\);;g')
    if [ -n "$fixed_path" ]; then
      chrpath -r $fixed_path $1
    else
      chrpath -d $1
    fi
}

for f in $(ls %buildroot%lib_prefix/libmpi.so.%mpi_soversion.*); do
fix_rpath $f
done

for f in $(ls %buildroot%lib_prefix/liboshmem.so.%openshmem_soversion.*); do
fix_rpath $f
done

for f in $(ls %buildroot%lib_prefix/libopen-pal.so.%open_pal_soversion.*); do
fix_rpath $f
done

fix_rpath %buildroot%lib_prefix/openmpi/libompi_dbg_msgq.so

for f in ompi_info oshmem_info mpirun opal_wrapper ; do
fix_rpath %buildroot%bin_prefix/$f
done

cat <<EOF >%buildroot/%bin_prefix/mpivars.sh
if ! echo \$PATH | grep -q %bin_prefix ; then
    PATH=%bin_prefix:\$PATH
    export PATH
fi

if ! echo \$LD_LIBRARY_PATH | grep -q %lib_prefix ; then
    LD_LIBRARY_PATH=%lib_prefix\${LD_LIBRARY_PATH:+:\$LD_LIBRARY_PATH}
    export LD_LIBRARY_PATH
fi

if ! echo \$MANPATH | grep -q %man_prefix ; then
    MANPATH=%man_prefix\${MANPATH:+:\$MANPATH}
    export MANPATH
fi

EOF

cat <<EOF >%buildroot/%bin_prefix/mpivars.csh
if (\$?path) then
    if ( "\${path}" !~ *%{bin_prefix}* ) then
	set path = ( %bin_prefix \$path )
    endif
else
    set path = ( %bin_prefix )
endif

if (\$?LD_LIBRARY_PATH) then
    if ( "\$LD_LIBRARY_PATH" !~ *%{lib_prefix}* ) then
	setenv LD_LIBRARY_PATH %lib_prefix:\$LD_LIBRARY_PATH
    endif
else
    setenv LD_LIBRARY_PATH %lib_prefix
endif

if (\$?MANPATH) then
    if ( "\$MANPATH" !~ *%{man_prefix}* ) then
	setenv MANPATH %man_prefix:\$MANPATH
    endif
else
    setenv MANPATH %man_prefix
endif

EOF

%post
%post_mpi_selector %name %bin_prefix

%preun
%preun_mpi_selector %name

%files
%dir %sysconfig_prefix
%config(noreplace) %sysconfig_prefix/openmpi-mca-params.conf
%config(noreplace) %sysconfig_prefix/openmpi-totalview.tcl
%dir %prefix
%dir %bin_prefix
%bin_prefix/mpivars.sh
%bin_prefix/mpivars.csh
%bin_prefix/mpicc
%bin_prefix/mpiexec
%bin_prefix/mpirun
%bin_prefix/ompi_info
%bin_prefix/opal_wrapper
%bin_prefix/oshc++
%bin_prefix/oshcc
%bin_prefix/oshCC
%bin_prefix/oshcxx
%bin_prefix/oshfort
%bin_prefix/oshmem_info
%bin_prefix/oshrun
%bin_prefix/shmemc++
%bin_prefix/shmemcc
%bin_prefix/shmemCC
%bin_prefix/shmemcxx
%bin_prefix/shmemfort
%dir %lib_prefix
%lib_prefix/libmpi.so.%mpi_soversion
%lib_prefix/libmpi.so.%mpi_soversion.*
%lib_prefix/liboshmem.so.%openshmem_soversion
%lib_prefix/liboshmem.so.%openshmem_soversion.*
%lib_prefix/libopen-pal.so.%open_pal_soversion
%lib_prefix/libopen-pal.so.%open_pal_soversion.*
%dir %lib_prefix/openmpi
%lib_prefix/openmpi/libompi_dbg_msgq.so
%data_prefix/

%files -n %name-devel
%include_prefix/
%lib_prefix/lib*.so
%dir %lib_prefix/pkgconfig
%lib_prefix/pkgconfig/*.pc

%files -n %name-doc
%doc LICENSE README.md VERSION
%man_prefix/

%changelog
* Wed Sep 17 2025 Alexey Romanyuta <r9odt@altlinux.org> 5.0.7-alt1
- Initial build 5.0.7.
