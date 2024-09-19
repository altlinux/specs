%define ltr libtorrent-rasterbar-devel
%define rel alt1

Name: qbittorrent
Version: 4.6.7
Epoch: 1
Release: %rel

Summary: qBittorrent is a bittorrent client written in C++ / Qt6 using the good libtorrent library
Summary(ru_RU.UTF-8): qBittorrent - bittorrent клиент написанный на C++ / Qt6, использующий библиотеку libtorrent.
License: GPLv2+
Group: Networking/File transfer
Url: http://qbittorrent.org

Source: %name-%version.tar.gz
Patch3500: ax_boost_base-loongarch64.patch

BuildPreReq: desktop-file-utils
BuildRequires(pre): rpm-build-ninja
BuildRequires: boost-devel boost-filesystem boost-filesystem-devel boost-datetime boost-program-options-devel boost-asio-devel
BuildRequires: gcc-c++  qt6-base-devel qt6-tools qt6-svg-devel qt6-tools-devel qt6-qtbase-gui libqt6-gui cmake 
# qt5-base-devel qt5-tools qt5-svg-devel systemd systemd-devel
BuildRequires: GeoIP-Lite-Country
BuildRequires: libnotify-devel
BuildRequires: zlib-devel
BuildRequires: gnu-config libappstream-glib 
BuildRequires: rpm-build-python3 rpm-macros-python3

%if "%rel" == "alt0.M80P"
%define ltr libtorrent-rasterbar9-devel
%endif
BuildRequires: %ltr

Requires: python3-module-ctypesgen qt6-svg
Requires: GeoIP-Lite-Country

%description
qBittorrent is a bittorrent client written in C++ / Qt6 using the good
libtorrent-rasterbar library (By Arvid Nordberg). qBittorrent is
free / open-source software released under the GNU GPL license.
qBittorrent aims to be a good alternative to all other bittorrent
clients. The Author is Christophe Dumez, French Student in
computer science (IT).

%description -l ru_RU.UTF8
qBittorrent - клиент bittorrent написанный на C++ / Qt6, использующий
библиотеку libtorrent-rasterbar (Arvid Nordberg). qBittorrent свободное
ПО с открытым исходным кодом, распространяющийся под лицензией GNU GPL.
qBittorrent стремится быть хорошей альтернативой всем другим bittorrent
клиентам. Автор Christophe Dumez, французский студент в области IT.

%package nox
Summary: qbittorrent version without GUI (WebUI version)
Group: Networking/File transfer
BuildRequires: systemd systemd-devel
%description nox
WebUI version of qbittorrent.

Default is to listen on tcp/8080 with admin/adminadmin credentials

%description -l ru_RU.UTF8 nox
Веб-интерфейс для qbittorrent

По умолчанию открывается порт 8080 с логином/паролем admin/adminadmin

%prep
%setup -q
%patch3500 -p1

%ifarch %e2k
sed -i "1i #include <cstdlib>\nnamespace std { using ::aligned_alloc; }" \
	src/{base/{bittorrent,rss},app,gui{,/properties,/rss,/search},webui/api}/*.cpp \
	src/base/{tagset,bittorrent/{filterparserthread,session}}.h \
	src/gui/{addnewtorrentdialog,properties/peersadditiondialog}.h
sed -i -E '/inline namespace/h;/^ *Q_ENUM_NS\(/{G;s/Q_ENUM_NS/&2/;s/\)\n.*inline namespace/,/;s/$/)/};/#include <QMeta(Type|Enum)>/a #define Q_ENUM_NS2(ENUM,NAME) Q_ENUMS(ENUM) inline Q_DECL_CONSTEXPR const QMetaObject *qt_getEnumMetaObject(ENUM) noexcept { return &NAME::staticMetaObject; } inline Q_DECL_CONSTEXPR const char *qt_getEnumName(ENUM) noexcept { return #ENUM; }' \
	src/base/bittorrent/*.h
%endif

%build

mkdir build-nox
pushd build-nox
%cmake \
 -DSYSTEMD=ON \
 -Wno-dev \
 -GNinja \
 -DQT6=ON \
 -DGUI=OFF \
 ..
%cmake_build
popd

# Build gui version
mkdir build
pushd build
%cmake \
 -Wno-dev \
 -DQT6=ON \
 -GNinja \
 ..
%cmake_build
popd

%install
# install headless version
pushd build-nox
%cmake_install
popd

# install gui version
pushd build
%cmake_install
popd

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/org.qbittorrent.qBittorrent.desktop



%files nox
%_bindir/%name-nox
%_man1dir/%name-nox.*
%_unitdir/qbittorrent-nox@.service

%files
%doc AUTHORS COPYING INSTALL README.* Changelog
%_bindir/%name
%_desktopdir/*
%_man1dir/%name.*
%_datadir/icons/hicolor/*/*/*
%_datadir/metainfo/*.xml

%changelog
* Thu Sep 19 2024 Ilya Mashkin <oddity@altlinux.ru> 1:4.6.7-alt1
- 4.6.7

* Thu Aug 22 2024 Ilya Mashkin <oddity@altlinux.ru> 1:4.6.6-alt1
- 4.6.6
- Add Requires qt6-svg (Closes: #50537)

* Mon May 27 2024 Ilya Mashkin <oddity@altlinux.ru> 1:4.6.5-alt1
- 4.6.5

* Thu Apr 11 2024 Ilya Mashkin <oddity@altlinux.ru> 1:4.6.4-alt2
- Build with Qt6 instead of Qt5 (Closes: #40723, #44079)
- Add BR systemd-devel for qbittorrent-nox

* Sat Mar 30 2024 Ilya Mashkin <oddity@altlinux.ru> 1:4.6.4-alt1
- 4.6.4

* Thu Jan 23 2024 Ilya Mashkin <oddity@altlinux.ru> 1:4.6.3-alt3
- Fixed typo in the module name

* Thu Jan 23 2024 Ilya Mashkin <oddity@altlinux.ru> 1:4.6.3-alt2
- Build with Python3 only (Closes: #49006)

* Thu Jan 18 2024 Ilya Mashkin <oddity@altlinux.ru> 1:4.6.3-alt1
- 4.6.3

* Thu Nov 30 2023 Ilya Mashkin <oddity@altlinux.ru> 1:4.6.2-alt1
- 4.6.2

* Mon Nov 27 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:4.6.1-alt1.1
- NMU: fixed FTBFS on LoongArch:
  + use fresh config.{guess,sub}
  + tell ax_boost_base to search libs in /usr/lib64 on LoongArch

* Fri Nov 24 2023 Ilya Mashkin <oddity@altlinux.ru> 1:4.6.1-alt1
- 4.6.1
- Fix invisible tray icon (Closes: #48285, #48286)

* Sun Oct 29 2023 Ilya Mashkin <oddity@altlinux.ru> 1:4.6.0-alt1
- 4.6.0

* Thu Aug 31 2023 Ilya Mashkin <oddity@altlinux.ru> 1:4.5.5-alt1
- 4.5.5

* Tue Jun 27 2023 Ilya Mashkin <oddity@altlinux.ru> 1:4.5.4-alt1
- 4.5.4

* Tue May 30 2023 Ilya Mashkin <oddity@altlinux.ru> 1:4.5.3-alt1
- 4.5.3

* Wed Mar 01 2023 Ilya Mashkin <oddity@altlinux.ru> 1:4.5.2-alt1
- 4.5.2

* Tue Feb 14 2023 Ilya Mashkin <oddity@altlinux.ru> 1:4.5.1-alt1
- 4.5.1

* Tue Dec 06 2022 Ilya Mashkin <oddity@altlinux.ru> 1:4.5.0-alt1
- 4.5.0

* Wed Aug 31 2022 Ilya Mashkin <oddity@altlinux.ru> 1:4.4.5-alt1
- 4.4.5

* Thu Aug 25 2022 Ilya Mashkin <oddity@altlinux.ru> 1:4.4.4-alt1
- 4.4.4

* Thu May 26 2022 Ilya Mashkin <oddity@altlinux.ru> 1:4.4.3.1-alt1
- 4.4.3.1
- Translations were broken with v4.4.3 and now are fixed.

* Wed May 25 2022 Ilya Mashkin <oddity@altlinux.ru> 1:4.4.3-alt1
- 4.4.3

* Wed Mar 30 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:4.4.2-alt2
- fixed build for Elbrus

* Fri Mar 25 2022 Ilya Mashkin <oddity@altlinux.ru> 1:4.4.2-alt1
- 4.4.2

* Wed Feb 16 2022 Ilya Mashkin <oddity@altlinux.ru> 1:4.4.1-alt1
- 4.4.1

* Fri Jan 07 2022 Ilya Mashkin <oddity@altlinux.ru> 1:4.4.0-alt1
- 4.4.0
- fix build on e2k

* Mon Nov 01 2021 Ilya Mashkin <oddity@altlinux.ru> 1:4.3.9-alt1
- 4.3.9

* Mon Aug 30 2021 Ilya Mashkin <oddity@altlinux.ru> 1:4.3.8-alt1
- 4.3.8

* Thu Aug 12 2021 Ilya Mashkin <oddity@altlinux.ru> 1:4.3.7-alt2
- fix build on e2k, ppc64le

* Fri Aug 06 2021 Ilya Mashkin <oddity@altlinux.ru> 1:4.3.7-alt1
- 4.3.7

* Tue Jul 13 2021 Ilya Mashkin <oddity@altlinux.ru> 1:4.3.6-alt1
- 4.3.6

* Fri May 07 2021 Ilya Mashkin <oddity@altlinux.ru> 1:4.3.5-alt1
- 4.3.5

* Thu Apr 22 2021 Ilya Mashkin <oddity@altlinux.ru> 1:4.3.4.1-alt1
- 4.3.4.1

* Sat May 02 2020 Motsyo Gennadi <drool@altlinux.ru> 1:4.2.5-alt1
- 4.2.5

* Thu Apr 23 2020 Motsyo Gennadi <drool@altlinux.ru> 1:4.2.4-alt1
- 4.2.4

* Sun Apr 12 2020 Motsyo Gennadi <drool@altlinux.ru> 1:4.2.3-alt1
- 4.2.3

* Sat Jan 04 2020 Motsyo Gennadi <drool@altlinux.ru> 1:4.2.1-alt1
- 4.2.1

* Fri Oct 18 2019 Motsyo Gennadi <drool@altlinux.ru> 1:4.1.8-alt1
- 4.1.8

* Thu Aug 15 2019 Motsyo Gennadi <drool@altlinux.ru> 1:4.1.7-alt1.1
- add ExcludeArch for ppc64le

* Tue Aug 13 2019 Motsyo Gennadi <drool@altlinux.ru> 1:4.1.7-alt1
- 4.1.7

* Tue May 07 2019 Motsyo Gennadi <drool@altlinux.ru> 1:4.1.6-alt1
- 4.1.6

* Thu Dec 27 2018 Motsyo Gennadi <drool@altlinux.ru> 1:4.1.5-alt1
- 4.1.5

* Mon Nov 19 2018 Motsyo Gennadi <drool@altlinux.ru> 1:4.1.4-alt1
- 4.1.4

* Thu Sep 27 2018 Motsyo Gennadi <drool@altlinux.ru> 1:4.1.3-alt1
- 4.1.3

* Fri Aug 17 2018 Motsyo Gennadi <drool@altlinux.ru> 1:4.1.2-alt1
- 4.1.2

* Mon Jun 04 2018 Motsyo Gennadi <drool@altlinux.ru> 1:4.1.1-alt1
- 4.1.1

* Sun May 06 2018 Motsyo Gennadi <drool@altlinux.ru> 1:4.1.0-alt1
- 4.1.0

* Wed Apr 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.0.4-alt2
- (NMU) Rebuilt with new libtorrent-rasterbar.

* Fri Mar 02 2018 Motsyo Gennadi <drool@altlinux.ru> 1:4.0.4-alt1
- 4.0.4

* Tue Dec 19 2017 Motsyo Gennadi <drool@altlinux.ru> 1:4.0.3-alt1
- 4.0.3

* Thu Dec 14 2017 Motsyo Gennadi <drool@altlinux.ru> 1:4.0.2-alt2
- cleanup

* Mon Dec 11 2017 Motsyo Gennadi <drool@altlinux.ru> 1:4.0.2-alt1
- 4.0.2

* Fri Nov 24 2017 Motsyo Gennadi <drool@altlinux.ru> 1:4.0.1-alt3
- fix

* Fri Nov 24 2017 Motsyo Gennadi <drool@altlinux.ru> 1:4.0.1-alt2
- fix build for x86

* Wed Nov 22 2017 Motsyo Gennadi <drool@altlinux.ru> 1:4.0.1-alt1
- 4.0.1

* Tue Nov 21 2017 Motsyo Gennadi <drool@altlinux.ru> 1:4.0.0-alt2
- fix build

* Mon Nov 20 2017 Motsyo Gennadi <drool@altlinux.ru> 1:4.0.0-alt1
- 4.0.0

* Mon Sep 11 2017 Motsyo Gennadi <drool@altlinux.ru> 1:3.3.16-alt1
- 3.3.16

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.3.15-alt1
- Updated to upstream release 3.3.15.

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.1.11-alt1.2.1
- Rebuilt for gcc5 C++11 ABI.

* Fri May 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.1.11-alt1.2
- Rebuilt with new libtorrent-rasterbar8

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1:3.1.11-alt1.1
- rebuild with boost 1.57.0

* Sat Nov 15 2014 Motsyo Gennadi <drool@altlinux.ru> 1:3.1.11-alt1
- 3.1.11

* Tue Oct 07 2014 Motsyo Gennadi <drool@altlinux.ru> 1:3.1.10-alt1
- 3.1.10 (ALT #30384)

* Wed Mar  5 2014 Terechkov Evgenii <evg@altlinux.org> 1:3.1.9-alt1
- 3.1.9 (ALT #29820)

* Thu Feb 13 2014 Terechkov Evgenii <evg@altlinux.org> 1:3.1.8-alt1
- 3.1.8 (ALT#29820)

* Fri Jan 24 2014 Terechkov Evgenii <evg@altlinux.org> 1:3.1.5-alt2
- qbittorrent-nox subpackage

* Fri Jan 24 2014 Terechkov Evgenii <evg@altlinux.org> 1:3.1.5-alt1
- 3.1.5

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.9-alt1.2
- Rebuilt with new libtorrent-rasterbar8

* Thu Jul 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.9-alt1.1
- Rebuilt with new libtorrent-rasterbar8

* Tue Apr 16 2013 Andrey Cherepanov <cas@altlinux.org> 1:3.0.9-alt1
- New version 3.0.9 (ALT #28367)

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.9.3-alt1.5
- Rebuilt with updated libtorrent-rasterbar

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.9.3-alt1.4
- Rebuilt with Boost 1.52.0

* Wed Nov 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.9.3-alt1.3
- Fixed build with glibc 2.16

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.9.3-alt1.2
- Rebuilt with Boost 1.51.0

* Sat Jun 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.9.3-alt1.1
- Rebuilt with Boost 1.49.0

* Wed Dec 21 2011 Alexey Morsov <swi@altlinux.ru> 1:2.9.3-alt1
- new version

* Tue Oct 18 2011 Alexey Morsov <swi@altlinux.ru> 1:2.9.0-alt1.git20111016
- new git version (commit 33325cdfee2289f87c573d7ae8cb455fb324f202)
- 2.9.0 release

* Thu Sep 01 2011 Alexey Morsov <swi@altlinux.ru> 1:2.9.0-alt0.1.svn5623
- new svn trunk version

* Mon Apr 18 2011 Alexey Morsov <swi@altlinux.ru> 1:2.8.0-alt0.1.svn5489
- new svn trunk version

* Fri Mar 25 2011 Alexey Morsov <swi@altlinux.ru> 1:2.7.0-alt1
- release 2.7.0

* Sun Mar 13 2011 Alexey Morsov <swi@altlinux.ru> 1:2.7.0-alt0.1.svn5307
- new svn update

* Tue Jan 25 2011 Alexey Morsov <swi@altlinux.ru> 1:2.7.0-alt0.1.svn5159
- 2.7 alpha

* Fri Jan 07 2011 Alexey Morsov <swi@altlinux.ru> 1:2.6.0-alt0.1.svn5001
- rc2

* Tue Dec 28 2010 Alexey Morsov <swi@altlinux.ru> 1:2.6.0-alt0.1.svn4929
- new svn trunk version

* Fri Dec 17 2010 Alexey Morsov <swi@altlinux.ru> 1:2.6.0-alt0.1.svn4870
- new svn trunk version

* Tue Dec 07 2010 Alexey Morsov <swi@altlinux.ru> 1:2.6.0-alt0.1.svn4841
- new svn trunk version (2.6.0)

* Thu Nov 04 2010 Alexey Morsov <swi@altlinux.ru> 1:2.5.0-alt0.1.svn4657
- new svn trunk version (2.5.0)

* Sun Oct 17 2010 Alexey Morsov <swi@altlinux.ru> 1:2.5.0-alt0.1.svn4531
- new svn trunk version (2.5.0 alpha)

* Mon Aug 23 2010 Alexey Morsov <swi@altlinux.ru> 1:2.4.0-alt0.1.svn4402
- new svn trunk version (commit b2d556a1f287d9d7aafc3f5e3f22218953e2f660)

* Tue May 25 2010 Alexey Morsov <swi@altlinux.ru> 1:2.3.0-alt0.1.svn3936
- new svn trunk version (commit 4f4f6f857c65a3c37e7b1073ff0c6cdd8330d025)

* Tue May 25 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.8-alt1.svn3934
- new 2.2 svn branch version

* Mon Mar 15 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.0-alt1
- new release

* Sat Mar 13 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.0-alt0.1.svn3673
- new svn trunk version (now preferences columns resizable)

* Sat Mar 13 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.0-alt0.1.svn3672
- new svn trunk version

* Wed Feb 10 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.0-alt0.1.svn3565
- new svn trunk version

* Thu Feb 04 2010 Alexey Morsov <swi@altlinux.ru> 1:2.2.0-alt0.1.svn3534
- new svn trunk version
- add libnotify dependency

* Fri Jan 22 2010 Alexey Morsov <swi@altlinux.ru> 1:2.1.1-alt0.1.svn3460
- new version

* Thu Jan 14 2010 Alexey Morsov <swi@altlinux.ru> 1:2.1.1-alt0.1.svn3439
- new svn version (commit 9bb0e5ef935ddb9f60d88cecf9bcd95fc36324d1)
- clean requires
- update russian translation

* Wed Jan 06 2010 Alexey Morsov <swi@altlinux.ru> 1:2.0.6-alt1
- new release

* Thu Dec 31 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.5-alt1
- new release (critical bug fix)

* Wed Dec 30 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.4-alt1
- new release

* Wed Dec 23 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.3-alt1
- new release
- fix qt4 requires (qt >= 4.4)

* Sun Dec 20 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.2-alt0.2.svn3163
- add GeoIP-Lite-Country to BuildRequires

* Sat Dec 19 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.2-alt0.1.svn3163
- new svn branch version (commit 3f3aaf2b00cc819f7cbb84d3694972aa19501d20)

* Fri Nov 20 2009 Alexey Morsov <swi@altlinux.ru> 1:2.0.0-alt0.1.svn2870
- new svn version (commit 2055f3b6893f95721650acc322330b8c3aeb354c)

* Fri Oct 30 2009 Alexey Morsov <swi@altlinux.ru> 1:1.6.0-alt0.1.svn2658
- new svn version (commit fd3f3b6b308173f538dca55c4fb685b988425891)

* Mon Oct 19 2009 Alexey Morsov <swi@altlinux.ru> 1:1.6.0-alt0.1.svn2636
- new svn version (commit d15344bd5e02271f236354af353508c994dfd34e)

* Wed Oct 14 2009 Alexey Morsov <swi@altlinux.ru> 1:1.6.0-alt0.1.svn2631
- new svn version (commit e00352dd5ea6226fe0e22dc3fbc2e9be26f51e1a)

* Tue Sep 22 2009 Alexey Morsov <swi@altlinux.ru> 1:1.6.0-alt0.1.svn2616
- new svn version (commit ef193f0758af91058926b149742d6417e7319bd6)

* Mon Sep 07 2009 Alexey Morsov <swi@altlinux.ru> 1:1.6.0-alt0.1.svn2608
- build svn r2608

* Fri Aug 28 2009 Alexey Morsov <swi@altlinux.ru> 1:1.5.0-alt0.2.svn2566
- build svn r2566
  + (fixed import 1.4 active torrens)
  + (desktop file fixed in upstream now)

* Wed Aug 26 2009 Alexey Morsov <swi@altlinux.ru> 1:1.5.0-alt0.2.beta4
- new version

* Tue Jun 09 2009 Alexey Morsov <swi@altlinux.ru> 1:1.4.0-alt0.3.beta2
- rebuild with new libtorrent-rasterbar

* Thu Apr 30 2009 Alexey Morsov <swi@altlinux.ru> 1:1.4.0-alt0.2.beta2
- add python-modules-ctypes to requires (for search engines)

* Wed Apr 22 2009 Alexey Morsov <swi@altlinux.ru> 1:1.4.0-alt0.1.beta2
- new beat version

* Wed Apr 22 2009 Alexey Morsov <swi@altlinux.ru> 1:1.3.3-alt1
- new version

* Sat Mar 21 2009 Alexey Morsov <swi@altlinux.ru> 1:1.3.2-alt1
- new version

* Wed Feb 25 2009 Alexey Morsov <swi@altlinux.ru> 1:1.3.1-alt2
- fix name for libtorrent-rasterbar-devel

* Sat Feb 07 2009 Alexey Morsov <swi@altlinux.ru> 1:1.3.1-alt1
- new version

* Wed Nov 26 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.1-alt1
- new version
- fix spec
  + remove deprecated call from post/postun

* Wed Oct 29 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.0-alt0.rc4.1
- fix build with boost1.36

* Mon Oct  6 2008 Alexey Morsov <swi@altlinux.org> 1:1.2.0-alt0.rc4
- new devel version

* Sun Aug 31 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.0-alt0.beta5
- new devel version

* Tue Aug 19 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.0-alt0.beta4
- new devel version
- update russian translation

* Sat Aug 09 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.0-alt0.beta2
- new devel version

* Sat Aug 02 2008 Alexey Morsov <swi@altlinux.ru> 1:1.2.0-alt0.beta1
- new devel version

* Sat Aug 02 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.1-alt1
- new release
  + updated russian translation now in upstream

* Tue Jul 29 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.0-alt0.rc1.1
- update russian translation

* Thu Jul 24 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.0-alt0.rc1
- new version
- change requires
  + libtorrent changed to libtorrent-rasterbar (upstream renaming)

* Wed Jun 25 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.0-alt0.beta2
- 1.1.0 beta2

* Mon Jun 16 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.0-alt0.beta1.1
- svn r1793 (pre beta2)

* Sat Jun 07 2008 Alexey Morsov <swi@altlinux.ru> 1:1.1.0-alt0.beta1.0
- new beta version

* Sat May 17 2008 Alexey Morsov <swi@altlinux.ru> 1:1.0.0-alt3
- fix menus to correspond with policy
- patch desktop file to correspond standard

* Thu Apr 24 2008 Alexey Morsov <swi@altlinux.ru> 1:1.0.0-alt2
- put 1.0.0 tar to package (not 1.0.0rc11)

* Wed Apr 23 2008 Alexey Morsov <swi@altlinux.ru> 1:1.0.0-alt1
- 1.0.0 release
- Improved a lot the torrent creation module
- Bittorrent FAST extension support
- Added UPnP / NAT-PMP port forwarding support
- Brand new search engine plugins system
- IPv6 is now fully supported
- many other (see ChangeLog file)

* Tue Mar 25 2008 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt2.rc11
- rebuild with new libtorrent and boost-1.34.1

* Wed Jan 02 2008 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc11
- Bypass exit confirmation on system shutdown
- Download from urls are now able to follow redirections
- Fixed torrent creation from a directory
- Fixed save path when seeding automatically after torrent creation

* Mon Dec 10 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc10
- Filtered files don't appear on hard disk anymore
- Real torrent share ratio is now displayed in transfer list

* Sat Nov 24 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc9
- fix crash on add partial torrent

* Sat Nov 17 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc8
- 1.0.0rc8

* Sat Nov 03 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc7
- Filtered files are not allocated on the hard-drive anymore
- Torrent content is now displayed as a tree

* Thu Oct 25 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc6
- Bittorrent FAST extension support
- Allow to use  a proxy for trackers / web seeds / peers / DHT connections
- Allow to set upload/download limit per torrent (right click)
- Search engine is now using one thread per website for faster results
- Improved a lot the torrent creation module
- Improved unicode support

* Sat Oct 13 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc5
- version 1.0.0.rc5

* Sat Oct 06 2007 Alexey Morsov <swi@altlinux.ru> 1.0.0-alt1.rc3
- Added UPnP / NAT-PMP port forwarding support
- Added encryption support (compatible with Azureus)
- Added RSS support
- Brand new search engine plugins system
- Supports SOCKS5 proxies as well as HTTP ones
- ..and many more anchanced and some bug fixes

* Wed Aug 15 2007 Alexey Morsov <swi@altlinux.ru> 0.9.3-alt2
- rebuild with libtorrent-0.12-alt1

* Tue May 08 2007 Alexey Morsov <swi@altlinux.ru> 0.9.3-alt1
- new version

* Mon Apr 16 2007 Alexey Morsov <swi@altlinux.ru> 0.9.2-alt1
- new version (bug fixing)

* Tue Apr 10 2007 Alexey Morsov <swi@altlinux.ru> 0.9.1-alt1
- New version (lot of new features such as Peer Exchange (PeX) support,
  autocompletion, new system tray popups, better internationalization,
  a lot of code rewriting (optimized and cleaned).
- based on latest libtorrent library by Arvid Norberg (v0.12)
- spec cleanup

* Fri Dec 22 2006 Alexey Morsov <swi@altlinux.ru> 0.8.0-alt1
- Initial build for sisyphus

