Name: mvapich2
Version: 1.5.1
Release: alt1.p1.1.1

%define mpi_prefix %_libexecdir/%name
%define mpi_sysconfdir %_sysconfdir/%name
%define docdir %_defaultdocdir/%name-devel-%version

Summary: OSU MVAPICH2 MPI package
License: BSD
Group: Development/Other

Url: http://mvapich.cse.ohio-state.edu/
Source: %name-%version.tar
Patch0: %name-1.5.1-alt-build.patch
Packager: Stanislav Ievlev <inger@altlinux.org>

BuildRequires(pre): mpi-selector
Requires(post,preun): mpi-selector

BuildPreReq: libibumad-devel >= 1.3.6 libibverbs-devel >= 1.1.4
BuildPreReq: librdmacm-devel
Requires: libibumad >= 1.3.6 libibverbs >= 1.1.4

# Automatically added by buildreq on Sat Jan 19 2008 (-bi)
BuildRequires: gcc-c++ gcc-fortran libibumad-devel libibverbs-devel python-modules

%description
This is an MPI-2 implementation which includes all MPI-1 features.  It is
based on MPICH2 and MVICH.

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
BuildArch: noarch
 
%description devel-doc
Documentation for the %name


%prep
%setup

%patch0 -p2

%build
pushd src/mpid/ch3/channels/mrail/src/hwloc
./autogen.sh
popd
%configure \
    --prefix=%mpi_prefix \
		--exec-prefix=%mpi_prefix \
		--bindir=%mpi_prefix/bin \
		--sysconfdir=%mpi_sysconfdir \
		--libdir=%mpi_prefix/lib \
		--includedir=%mpi_prefix/include \
		--mandir=%mpi_prefix/man \
    --with-pm=mpd \
    --without-mpe \
    --docdir=%docdir
%make

%install
%makeinstall_std

install -d %buildroot%_pkgconfigdir
mv %buildroot%mpi_prefix/lib/pkgconfig/* %buildroot%_pkgconfigdir/

rm osu_benchmarks/configure
cp -a osu_benchmarks %buildroot/%mpi_prefix

find %buildroot -type f -print0 |
    xargs -r0 file |
    fgrep text |
    cut -d: -f1 | xargs -r \
		    sed -i \
	    		-e "s^prefix=%buildroot/%mpi_prefix^prefix=%mpi_prefix^g" \
    	    		-e "s^sysconfdir=.*^sysconfdir=%mpi_sysconfdir^g" \
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

if ! echo \$MANPATH | grep -q %mpi_prefix/man ; then
    MANPATH=%mpi_prefix/man:\$MANPATH
fi
EOF


%post
%post_mpi_selector %name %mpi_prefix/bin

%preun
%preun_mpi_selector %name

%files
%dir %mpi_prefix
%mpi_prefix/bin
%dir %mpi_prefix/man
%dir %mpi_prefix/man/man1
%exclude %mpi_prefix/bin/mpif77
%exclude %mpi_prefix/bin/mpif90
%exclude %mpi_prefix/bin/mpicc
%exclude %mpi_prefix/bin/mpicxx
%mpi_prefix/man/man1/mpiexec*

%files devel
%mpi_prefix/bin/mpif77
%mpi_prefix/bin/mpif90
%mpi_prefix/bin/mpicc
%mpi_prefix/bin/mpicxx
%dir %mpi_sysconfdir
%config(noreplace) %mpi_sysconfdir/*.conf
%mpi_prefix/include
%mpi_prefix/lib/*.a
%mpi_prefix/man
%exclude %mpi_prefix/man/man1/mpiexec*
%mpi_prefix/osu_benchmarks
%_pkgconfigdir/*

%files devel-doc
%docdir

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.1-alt1.p1.1.1
- Rebuild with Python-2.7

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.p1.1
- Rebuilt for debuginfo

* Fri Dec 17 2010 Timur Aitov <timonbl4@altlinux.org> 1.5.1-alt1.p1
- New version (1.5.1p1)

* Sun Oct 17 2010 Michael Shigorin <mike@altlinux.org> 1.4.1-alt1.qa1
- fix FTBFS (macro name)
- dropped rpm-build-compat from BR
- minor spec cleanup according to packaging policy

* Wed Aug 18 2010 Andriy Stepanov <stanv@altlinux.ru> 1.4.1-alt1
- OFED 1.5.1

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0p1-alt2
- Rebuilt with python 2.6

* Mon May 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0p1-alt1
- Version 1.2.0p1

* Mon Oct 13 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.3-alt1
- 1.0.3, rebuild with OFED-1.3.1

* Sat May 24 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.2p1-alt1
- 1.0.2p1

* Thu Jan 31 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt3
- add osu_benchmarks to package

* Tue Jan 29 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt2
- add support for mpi-selector

* Sat Jan 19 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt1
- 1.0.1
- build ofa variant (without ptmalloc, ptmalloc build is broken)

* Wed Aug 29 2007 Stanislav Ievlev <inger@altlinux.org> 0.9.8-alt1 
- Initial build (tcp variant)
