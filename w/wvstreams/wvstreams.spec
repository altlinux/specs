%define soffix .so.4.6
%def_disable kdoc
%def_enable static

Name: wvstreams
Version: 4.6.1
Release: alt9

Summary: C++ libraries for rapid application development
License: LGPL-2.0
Group: Development/C++
Packager: Andrey Cherepanov <cas@altlinux.org>

URL: http://alumnit.ca/wiki/index.php?page=WvStreams
# git pull http://github.com/wlach/wvstreams master:upstream
Source: %name-%version.tar.gz
Source1: ChangeLog
Patch: %name-%version-alt-paths_links_USBmodem.patch
Patch1: %name-4.5.1-fix-build.patch
#install-xplc target was missing
Patch2: wvstreams-4.5-noxplctarget.patch
#Fix parallel build
Patch3: wvstreams-4.6.1-make.patch
#sys/stat.h is missing some files in rawhide build
Patch4: wvstreams-4.6.1-statinclude.patch
#const X509V3_EXT_METHOD * -> X509V3_EXT_METHOD * conversion not allowed
#by rawhide gcc
Patch5: wvstreams-4.6.1-gcc.patch
# fix missing unistd.h header for gcc 4.7
Patch6: wvstreams-4.6.1-gcc47.patch
Patch7: wvstreams-4.6.1-magic.patch
Patch8: 0001-Use-explicit-cast-and-prevent-compiler-error.patch
Patch9: wvstreams-4.6.1-openssl1.1.patch
Patch10: wvstreams-4.6.1-gcc10.patch
Patch11: wvstreams-4.6.1-tripledes-cast.patch
Patch2000: %name-e2k.patch

BuildPreReq: gcc-c++
BuildPreReq: OpenSP /proc
BuildRequires: boost-devel docbook-style-dsssl doxygen graphviz
BuildRequires: libcom_err-devel libdbus-devel libpam-devel libqt3-devel
BuildRequires: libreadline-devel libssl-devel openjade
%if_enabled kdoc
BuildPreReq: kdoc
%endif

BuildRequires(pre): rpm-macros-valgrind
%ifarch %valgrind_arches
BuildRequires: valgrind-devel
%endif

%description
WvStreams aims to be an efficient, secure, and easy-to-use library
for doing network applications development.

######## wvstreams
%package -n lib%name
Summary: %summary
Group: System/Libraries
%description -n lib%name
WvStreams aims to be an efficient, secure, and easy-to-use library
for doing network applications development.

%package -n lib%name-devel
Summary: %summary
Group: Development/C++
Requires: lib%name = %version-%release
Provides: %name-manual = %version-%release
Obsoletes: %name-manual < %version
%description -n lib%name-devel
WvStreams aims to be an efficient, secure, and easy-to-use library
for doing network applications development.

%package -n lib%name-devel-doc
Summary: %summary
Group: Development/Documentation
Requires: lib%name-devel = %version-%release
Provides: %name-doxy-manual = %version-%release
%description -n lib%name-devel-doc
WvStreams aims to be an efficient, secure, and easy-to-use library
for doing network applications development.

%package -n lib%name-devel-static
Summary: %summary
Group: Development/C++
Requires: lib%name-devel = %version-%release
%description -n lib%name-devel-static
WvStreams aims to be an efficient, secure, and easy-to-use library
for doing network applications development.

######## uniconf
%package -n libuniconf
Summary: %summary (configuration system)
Group: System/Libraries
Requires: lib%name = %version-%release
%description -n libuniconf
UniConf is a configuration system that can serve as the centrepiece
among many other, existing configuration systems, such as: GConf,
KConfig, Windows registry, and Mutt. ;)  UniConf can also be accessed
over the network, with authentication, allowing easy replication of
configuration data via the UniReplicateGen.

%package -n libuniconf-devel
Summary: %summary (configuration system)
Group: Development/C++
Requires: libuniconf = %version-%release
Requires: lib%name-devel = %version-%release
%description -n libuniconf-devel
UniConf is a configuration system that can serve as the centrepiece
among many other, existing configuration systems, such as: GConf,
KConfig, Windows registry, and Mutt. ;)  UniConf can also be accessed
over the network, with authentication, allowing easy replication of
configuration data via the UniReplicateGen.

%package -n libuniconf-devel-static
Summary: %summary (configuration system)
Group: Development/C++
Requires: libuniconf-devel = %version-%release
Requires: lib%name-devel-static = %version-%release
%description -n libuniconf-devel-static
UniConf is a configuration system that can serve as the centrepiece
among many other, existing configuration systems, such as: GConf,
KConfig, Windows registry, and Mutt. ;)  UniConf can also be accessed
over the network, with authentication, allowing easy replication of
configuration data via the UniReplicateGen.

%package -n uniconf-tools
Summary: Tools to interface with UniConf configuration system
Group: System/Configuration/Other
Requires: libuniconf = %version-%release
%description -n uniconf-tools
UniConf is a configuration system that can serve as the centrepiece
among many other, existing configuration systems, such as: GConf,
KConfig, Windows registry, and Mutt. ;)  UniConf can also be accessed
over the network, with authentication, allowing easy replication of
configuration data via the UniReplicateGen.

%package -n uniconfd
Summary: Server that manages UniConf elements
Group: System/Servers
Requires: libuniconf = %version-%release
%description -n uniconfd
UniConf is a configuration system that can serve as the centrepiece
among many other, existing configuration systems, such as: GConf,
KConfig, Windows registry, and Mutt. ;)  UniConf can also be accessed
over the network, with authentication, allowing easy replication of
configuration data via the UniReplicateGen.

######## qt
%package -n libwvqt
Summary: %summary (Qt3 GUI)
Group: System/Libraries
Requires: lib%name = %version-%release
%description -n libwvqt
This package contains the library necessary to tie WvStreams and Qt
program event loops together to enable WvStreams to act as the I/O and
configuration back end for Qt and KDE.

%package -n libwvqt-devel
Summary: %summary (Qt3 GUI)
Group: Development/KDE and QT
Requires: libwvqt = %version-%release
Requires: lib%name-devel = %version-%release
Requires: libqt3-devel
%description -n libwvqt-devel
This package contains the library necessary to tie WvStreams and Qt
program event loops together to enable WvStreams to act as the I/O and
configuration back end for Qt and KDE.

%package -n libwvqt-devel-static
Summary: %summary (Qt3 GUI)
Group: Development/KDE and QT
Requires: libwvqt-devel = %version-%release
Requires: lib%name-devel-static = %version-%release
%description -n libwvqt-devel-static
This package contains the library necessary to tie WvStreams and Qt
program event loops together to enable WvStreams to act as the I/O and
configuration back end for Qt and KDE.

%prep
%setup -n %name-%version
install -m644 %SOURCE1 .
bzip2 -9fk ChangeLog
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%ifarch %e2k
%patch2000 -p1
# _BSD_SOURCE is deprecated
sed -i "s|-D_BSD_SOURCE||" wvrules.mk
%endif

%build
%global optflags_lto %optflags_lto -ffat-lto-objects
%autoreconf
%configure

%make SOFFIX="%soffix" VERBOSE=1 \
	COPTS="%optflags %optflags_shared" CXXOPTS="%optflags %optflags_shared" 
%make_build -C Docs/sgmlmanual html
%make_build doxygen
%if_enabled kdoc
kdoc -f html -d Docs/kdoc-html --name %name --strip
%endif

%install
%make_install SOFFIX="%soffix" DESTDIR=%buildroot install

%define pkgdocdir %_docdir/%name-%version
mkdir -p %buildroot%pkgdocdir/html
mkdir -p %buildroot%pkgdocdir/doxy-html
install -p -m644 ChangeLog.bz2 README %buildroot%pkgdocdir
install -p -m644 Docs/sgmlmanual/*/*.htm* %buildroot%pkgdocdir/html
install -p -m644 Docs/doxy-html/* %buildroot%pkgdocdir/doxy-html
mkdir -p %buildroot%_localstatedir/uniconf
mv %buildroot%_localstatedir/lib/uniconf/uniconfd.ini \
	%buildroot%_localstatedir/uniconf/

######## wvstreams
%files -n lib%name
%_bindir/wsd
%_bindir/wvtestrun
%_libdir/libwvbase%soffix
%_libdir/libwvutils%soffix
%_libdir/lib%name%soffix
%_libdir/libwvdbus%soffix
%dir %pkgdocdir
%pkgdocdir/README

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*.h
%_includedir/%name/xplc
%exclude %_includedir/%name/uni*.h
%exclude %_includedir/%name/wvqt*.h
%_libdir/libwvbase.so
%_libdir/libwvutils.so
%_libdir/lib%name.so
%_libdir/libwvdbus.so
%_pkgconfigdir/*.pc
%exclude %_pkgconfigdir/libuniconf.pc
%exclude %_pkgconfigdir/libwvqt.pc
%pkgdocdir/ChangeLog.bz2
%ifarch %valgrind_arches
%_libdir/valgrind/wvstreams.supp
%endif

%files -n lib%name-devel-doc
%pkgdocdir/html/
%pkgdocdir/doxy-html/
%if_enabled kdoc
%pkgdocdir/kdoc-html
%endif

%if_enabled static
%files -n lib%name-devel-static
%_libdir/libwvtest.a
%_libdir/libwvstatic.a
%endif

######## uniconf
%files -n libuniconf
%_libdir/libuniconf%soffix

%files -n libuniconf-devel
%_includedir/%name/uni*.h
%_libdir/libuniconf.so
%_libdir/pkgconfig/libuniconf.pc

%files -n uniconf-tools
%_bindir/uni
%_man8dir/uni.*

%files -n uniconfd
%config(noreplace) %_sysconfdir/uniconf.conf
%_sbindir/uniconfd
%_man8dir/uniconfd.*
%_localstatedir/uniconf

######## qt
%files -n libwvqt
%_libdir/libwvqt%soffix

%files -n libwvqt-devel
%_includedir/%name/wvqt*.h
%_libdir/libwvqt.so
%_libdir/pkgconfig/libwvqt.pc

%changelog
* Fri Dec 15 2023 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt9
- Rebuilt with openssl 3.x (ALT #48809).

* Thu Sep 02 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 4.6.1-alt8
- Fixed passing of **data instead of *data in wvtripledes.cc
- Added patch for Elbrus

* Fri Aug 27 2021 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt7
- FTBFS: fix build with LTO by default.

* Tue Jan 05 2021 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt6
- FTBFS: fix build with GCC 10.
- Fix License tag.

* Wed Nov 06 2019 Michael Shigorin <mike@altlinux.org> 4.6.1-alt5
- Move to rpm-macros-valgrind

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 4.6.1-alt4.qa1
- NMU: applied repocop patch

* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt4
- Fix build with OpenSSL 1.1.

* Sun Jun 04 2017 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt3
- Use explicit cast and prevent compiler error (patch from Fedora)
- Disable noarch for doc package

* Mon Oct 05 2015 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt2
- rebuilt against gcc5-built qt3

* Fri Nov 29 2013 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt1
- New version
- Apply Fedora patches

* Tue Apr 02 2013 Andrey Cherepanov <cas@altlinux.org> 4.5.1-alt4.git20090319.2
- Fix build

* Mon Oct 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.1-alt4.git20090319.1
- Rebuilt with openssl10

* Wed May 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.1-alt4.git20090319
- Rebuild with gcc 4.4

* Wed Mar 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.1-alt3.git20090319
- Reform directory structure (git pull from upstream)

* Tue Mar 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.1-alt2
- URL's of project was changed
- fix #8217

* Sat Feb 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.1-alt1.1
- set noarch for devel docs
- remove dependency on fonts-ttf-ms

* Mon Jan 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.1-alt1
- Get up from orphaned; version 4.5.1

* Sun May 01 2005 Alexey Tourbin <at@altlinux.ru> 4.0.2-alt1
- 3.75.0 -> 4.0.2
- lib%name: built with libdb4 libfam libopenslp libpam libssl libxplc
- subpackages: 
  + libuniconf libuniconf-devel uniconf-tools uniconfd
  + libwvfft libwvfft-devel
  + libwvqt libwvqt-devel
  + libwvtelephony libwvtelephony-devel
  + libwvoggvorbis libwvoggvorbis-devel
  + libwvoggspeex libwvoggspeex-devel
- TODO: uniconfd init script (looking for feedback)

* Fri Mar 04 2005 Alexey Tourbin <at@altlinux.ru> 3.75.0-alt1
- 3.74.0 -> 3.75.0
- merged RedHat patches (gcc3, gcc34, stringbuf)
- dropped mdk-db1.patch, rebuilt without libdb1
- libuniconf not packaged

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 3.74.0-alt2.1.1
- Rebuilt with openssl-0.9.7d.

* Sun Feb 15 2004 Alexey Tourbin <at@altlinux.ru> 3.74.0-alt2.1
- fixed interpackage dependencies

* Wed Feb 11 2004 Alexey Tourbin <at@altlinux.ru> 3.74.0-alt2
- %name-manual packaged (html)

* Tue Feb 10 2004 Alexey Tourbin <at@altlinux.ru> 3.74.0-alt1
- 3.74.0, soname change, maintainer change
- mdk-db1.patch: fix libdb1 detection
- ogg, gtk, qt, etc. refused (only db1, openssl and zlib support kept)
- lib%name-devel-static not packaged by default

* Wed Dec 25 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.70-alt2
- Fixed /var/lock path

* Mon Oct 21 2002 Konstantin Volckov <goldhead@altlinux.ru> 3.70-alt1
- First build for Sisyphus

* Tue Sep 10 2002 Mike A. Harris <mharris@redhat.com> 3.70-6
- use FHS macros for multilib systems

* Sat Aug 10 2002 Elliot Lee <sopwith@redhat.com>
- rebuilt with gcc-3.2 (we hope)

* Mon Jul 22 2002 Tim Powers <timp@redhat.com>
- rebuild using gcc-3.2-0.1

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 20 2002 Nalin Dahyabhai <nalin@redhat.com> 3.70-1
- patch to build with gcc 3.x
- build with -fPIC

* Wed Apr 10 2002 Nalin Dahyabhai <nalin@redhat.com>
- update to 3.70

* Wed Mar 27 2002 Nalin Dahyabhai <nalin@redhat.com> 3.69-1
- pull in from upstream tarball

* Wed Feb 27 2002 Nalin Dahyabhai <nalin@redhat.com>
- merge the main and -devel packages into one .spec file
- use globbing to shorten the file lists
- don't define name, version, and release as macros (RPM does this by default)
- use the License: tag instead of Copyright: (equivalent at the package level,
  but License: reflects the intent of the tag better)
- use a URL to point to the source of the source tarball
- add BuildRequires: openssl-devel (libwvcrypto uses libcrypto)
- move the buildroot to be under %%{_tmppath}, so that it can be moved by
  altering RPM's configuration

* Tue Jan 29 2002 Patrick Patterson <ppatters@nit.ca>
- Initial Release of WvStreams
