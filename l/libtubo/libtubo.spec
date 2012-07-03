Name: libtubo
Version: 4.5.0
Release: alt4

Summary: Tubo Remote Process Execution Library
License: GPL
Group: System/Libraries
Url: http://xffm.sourceforge.net/libtubo.html

Source: %name-%version.tar.gz

Patch0: libtubo-4.5.0-alt-unresolved.patch

Packager: Eugene Ostapets <eostapets@altlinux.ru>

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

%prep
%setup -q
%patch0 -p1

%build
libtoolize --copy --force
aclocal -I m4
automake -a -f -c
autoconf
%configure \
	--enable-shared \
	--disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/xffm/tubo.h
%_pkgconfigdir/libtubo.pc

%changelog
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
