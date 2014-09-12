Name: libtubo
Version: 5.0.14
Release: alt1.git20140218

Summary: Tubo Remote Process Execution Library
License: GPL
Group: System/Libraries
Url: http://xffm.sourceforge.net/libtubo.html

Source: %name-%version.tar.gz

BuildPreReq: gtk-doc
# Automatically added by buildreq on Tue Nov 07 2006
BuildRequires: gcc-c++ glib2-devel

%description
The Libtubo library is small and simple function set to enable a process to
run any other process in the background and communicate via the stdout,
stderr and stdin file descriptors.

%package devel
Summary: Development files for %name
Group: Development/C
PreReq: %name = %version-%release

%description devel
The Libtubo library is small and simple function set to enable a process to
run any other process in the background and communicate via the stdout,
stderr and stdin file descriptors.

The %name-devel package contains the header files and documentation
needed to develop applications with %name.

%package devel-docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-docs
The Libtubo library is small and simple function set to enable a process to
run any other process in the background and communicate via the stdout,
stderr and stdin file descriptors.

This package contains documentation for %name.

%package tools
Summary: Tools for %name
Group: Networking/Remote access
PreReq: %name = %version-%release

%description tools
The Libtubo library is small and simple function set to enable a process to
run any other process in the background and communicate via the stdout,
stderr and stdin file descriptors.

This package contains tools for %name.

%prep
%setup

%build
#libtoolize --copy --force
#aclocal -I m4
#automake -a -f -c
#autoconf
./autogen.sh
%configure \
	--includedir=%_includedir/xffm \
	--enable-shared \
	--disable-static \
	--enable-gtk-doc \
	--enable-gtk-doc-html \
	--with-debug \
	--with-html-dir=%_docdir \
	--with-examples
%make_build WANT_EXAMPLES=1

%install
%makeinstall_std WANT_EXAMPLES=1

mv %buildroot%_bindir/example %buildroot%_bindir/%name-example
ln -s tubo.pc %buildroot%_pkgconfigdir/%name.pc

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%dir %_includedir/xffm
%_includedir/xffm/tubo.h
%_pkgconfigdir/*

%files devel-docs
%_docdir/%name

%files tools
%doc src/example.c
%_bindir/*
%_man1dir/*

%changelog
* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.14-alt1.git20140218
- Version 5.0.14

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 4.5.0-alt4.qa1
- NMU: rebuilt for debuginfo.

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt4
- Rebuilt for soname set-versions

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 4.5.0-alt3.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libtubo
  * postun_ldconfig for libtubo

* Thu Jan 03 2008 Eugene Ostapets <eostapets@altlinux.ru> 4.5.0-alt3
- fix build with new autotools

* Mon Nov 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.5.0-alt2
- spec cleanup

* Mon Jun 26 2006 Igor Zubkov <icesik@altlinux.ru> 4.5.0-alt1
- Initial build for Sisyphus
