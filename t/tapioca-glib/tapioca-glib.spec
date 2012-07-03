Name: tapioca-glib
Version: 0.14.1.2
Release: alt3

Summary: A framework for Voice over IP (VoIP) and Instant Messaging (IM)
Group: Networking/Instant messaging
License: LGPLv2+
Url: http://tapioca-voip.sourceforge.net/wiki/index.php/Tapioca

# https://tapioca-voip.svn.sourceforge.net/svnroot/tapioca-voip/trunk/tapioca-glib
Source0: %name-%version.tar.gz

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Automatically added by buildreq on Sat Sep 29 2007
#BuildRequires: gcc-c++ gcc-fortran glibc-devel-static gtk-doc libdbus-glib-devel
BuildRequires: gcc-c++ gtk-doc libdbus-glib-devel

%description
Tapioca is a framework for Voice over IP (VoIP) and
Instant Messaging (IM). Its main goal is to provide
an easy way for developing and using VoIP and IM
services in any kind of application. It was designed
to be cross-platform, lightweight, thread-safe, having
mobile devices and applications in mind.

Tapioca's main goals are:

* Create a solution that integrates all components
used by VoIP and IM applications in a single, reliable
and easy to use framework, which is able to work on different
platforms.

* Spare resources, providing central services for multiple
applications. Eg.: The control of all incoming and outgoing SIP
requests are managed by the SIP service, avoiding the creation of
one SIP stack and allocation of a network port for each SIP-based
application.

* Reduce the overhead of control layers and library dependencies.

%package devel
Summary: Development libraries and header files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development libraries and header files for %name.

%package devel-doc
Summary: Development documentation files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel-doc
Development documentation files for %name.

%prep
%setup

%build
./autogen.sh
%configure \
	--enable-gtk-doc
%make

%install
sed -i 's|^\(install_sh\ .*\)|\1 -C|' tapioca/core/Makefile
sed -i 's|^\(INSTALL\ \).*|\1= cp -f|' tapioca/core/Makefile
sed -i 's|^\(INSTALL_DATA\).*|\1 = cp -f|' tapioca/core/Makefile
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%dir %_includedir/libtapioca-glib-0.14
%_includedir/libtapioca-glib-0.14/
%_pkgconfigdir/*.pc

%files devel-doc
%dir %_datadir/gtk-doc/html/tapioca-glib-client
%_datadir/gtk-doc/html/tapioca-glib-client/
%dir %_datadir/gtk-doc/html/tapioca-glib-core
%_datadir/gtk-doc/html/tapioca-glib-core/

%changelog
* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1.2-alt3
- Rebuilt for debuginfo

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1.2-alt2
- Rebuilt for soname set-versions

* Wed Feb 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1.2-alt1
- Version 0.14.1.2 (ALT #23010)
- Fixed for autogen.sh

* Sat Nov 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.14.0.1-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for tapioca-glib
  * postun_ldconfig for tapioca-glib

* Sat Sep 29 2007 Igor Zubkov <icesik@altlinux.org> 0.14.0.1-alt1
- build for Sisyphus


