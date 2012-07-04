%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.0.0

Name: berkeley_upc
Version: 2.14.2
Release: alt1
Summary: Berkeley Unified Parallel C (UPC)
License: BSD
Group: Development/C
Url: http://upc.lbl.gov/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: %mpiimpl-devel %{name}_translator gdb
BuildPreReq: flex perl(Term/ReadLine.pm)

Requires: lib%name-devel
Requires: %{name}_translator
Conflicts: GASNet

%description
Berkeley Unified Parallel C (UPC).

%package -n lib%name-devel
Summary: Development files of Berkeley UPC
Group: Development/C
Requires: %name = %version-%release
Conflicts: libgasnet-devel

%description -n lib%name-devel
Berkeley Unified Parallel C (UPC).

This package contains development files of Berkeley UPC.

This package contains static libraries of Berkeley UPC.

%package docs
Summary: Documentation for Berkeley UPC
Group: Development/Documentation
BuildArch: noarch

%description docs
Berkeley Unified Parallel C (UPC).

This package contains documentation for Berkeley UPC.

%prep
%setup
sed -i 's|@LIBDIR@|%_libdir|' \
	detect-upc/upcppp.pl profile/dump/upcc-dump upcc.pl
%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|" multiconf.conf.in

sed -i 's|^STRIP.*\=.*|STRIP=echo|' \
	Makefile.in configure

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh

./Bootstrap
%add_optflags %optflags_shared -DGASNETI_BUG1389_WORKAROUND=1
%configure \
	--includedir=%_includedir/bupc \
	--enable-udp \
	--enable-smp \
	--enable-mpi \
	--enable-ibv \
	--with-translator=%_libdir/%{name}_translator/targ \
	--enable-allow-gcc4 \
	--disable-aligned-segments \
	--with-multiconf=+opt_inst
%make_build

%install
source %mpidir/bin/mpivars.sh
%makeinstall_std

chmod +x %buildroot%_bindir/*

mv %buildroot%prefix/etc/* %buildroot%_sysconfdir/

install -d %buildroot%perl_vendorlib
pushd %buildroot%_includedir/bupc
for i in *.pl; do
	ln -s %_includedir/bupc/$i %buildroot%perl_vendorlib/
done
popd

install -d %buildroot%_docdir/%name
install -p -m644 ChangeLog LICENSE.TXT README* \
	%buildroot%_docdir/%name

sed -i 's|/opt||g' \
	%buildroot%_sysconfdir/*.conf \
	%buildroot%_includedir/bupc/*.mak \
	%buildroot%_includedir/bupc/*.h \
	%buildroot%_includedir/bupc/*-conduit/*.mak

sed -i 's|/usr/libexec|%_libdir|' \
	%buildroot%_includedir/bupc/upcc.mak

%ifarch x86_64
mv %buildroot%_libexecdir/*upc* %buildroot%_libdir/
%endif

mv %buildroot%_bindir/gasp-dump %buildroot%_includedir/bupc/
mv %buildroot%_includedir/bupc/gasp-dump/*.a %buildroot%_libdir/
rm -fR %buildroot%prefix/man

%files
%_sysconfdir/*
%_bindir/*
#exclude %_bindir/amudprun
#exclude %_bindir/gasnet*
%_libdir/*upc*
%exclude %_libdir/*.a
%_includedir/bupc/*.pl
%_libdir/valgrind
%perl_vendorlib/*

%files -n lib%name-devel
%_includedir/*
%exclude %_includedir/bupc/*.pl
%_libdir/*.a

%files docs
%_man1dir/*
%_docdir/*

%changelog
* Wed Jul 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.2-alt1
- Version 2.14.2

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.0-alt1
- Version 2.14.0

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.2-alt1
- Version 2.12.2

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.1-alt1
- Version 2.12.1

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt2
- Rebuilt for debuginfo

* Fri Dec 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt1
- Initial build for Sisyphus

