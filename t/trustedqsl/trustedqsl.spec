Name:    trustedqsl
Version: 2.7.1
Release: alt1
Summary: TrustedQSL ham-radio applications

Group: Communications
License: BSD
URL: http://www.rickmurphy.net/trustedqsl.org/

Source0: tqsl-%version.tar

Patch1: tqsl-tqsllib.patch
Patch2: tqsl-fix-undefined-macro.patch
Patch3: tqsl-ssl-md5.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: libdb4-devel
BuildRequires: libssl-devel
BuildRequires: libcurl-devel
BuildRequires: libexpat-devel
BuildRequires: libsqlite3-devel
BuildRequires: libwxGTK3.2-devel
BuildRequires: zlib-devel
BuildRequires: desktop-file-utils

Requires: curl

%description
The TrustedQSL applications are used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the GUI applications tqslcert and tqsl.

%package -n tqsllib
Summary: TrustedQSL library
Group: System/Libraries

%description -n tqsllib
The TrustedQSL library is used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the library and configuration files needed to run
TrustedQSL applications.

%package -n tqsllib-devel
Summary: Development files the for TrustedQSL library
Group: 	Development/C++
Requires: tqsllib = %EVR

%description -n tqsllib-devel
The TrustedQSL library is used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the to develop with tqsllib.

%prep
%setup -q -n tqsl-%version
%patch1 -p1
#patch2 -p2
%patch3 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmakeinstall_std

## Install desktop files
#mkdir -p %buildroot%_desktopdir
#sed -i -e "s/.png//g" -e "s/Application;/Network;/g" -e "s/Utility;/GTK;/g" apps/tqsl.desktop
#desktop-file-install --dir=%buildroot%_desktopdir apps/tqsl.desktop
#
## Install icons
#for size in 16 32 48 64 128; do
#     install -Dpm 0644 apps/icons/key${size}.png \
#     %buildroot%_iconsdir/hicolor/${size}x${size}/apps/TrustedQSL.png
#done

%find_lang --output=%name.lang tqslapp
rm -f %buildroot%_datadir/locale/*/LC_MESSAGES/wxstd.mo

%files -f %name.lang
%doc AUTHORS.txt LICENSE.txt README
%_bindir/tqsl
%_datadir/TrustedQSL
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_pixmapsdir/TrustedQSL.png
%_man5dir/*.5*

%files -n tqsllib
%doc src/LICENSE src/ChangeLog.txt
%_libdir/libtqsllib.so.*

%files -n tqsllib-devel
%_includedir/*
%_libdir/libtqsllib.so

%changelog
* Thu Oct 19 2023 Andrey Cherepanov <cas@altlinux.org> 2.7.1-alt1
- New version.

* Sat Sep 30 2023 Andrey Cherepanov <cas@altlinux.org> 2.7-alt1
- New version.

* Thu Aug 25 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- New version.

* Tue Jul 19 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt2
- Rebuild with libwxGTK3.2-devel.

* Wed Jun 15 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- New version.

* Sat May 28 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.3-alt1
- New version.

* Fri May 13 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.2-alt1
- New version.

* Wed Apr 27 2022 Andrey Cherepanov <cas@altlinux.org> 2.6.1-alt1
- New version.

* Mon Mar 21 2022 Andrey Cherepanov <cas@altlinux.org> 2.6-alt1
- New version.

* Sat Oct 09 2021 Andrey Cherepanov <cas@altlinux.org> 2.5.9-alt1
- New version.

* Thu Oct 07 2021 Andrey Cherepanov <cas@altlinux.org> 2.5.8-alt2
- Rebuild with libwxGTK3.1-devel.

* Mon Jun 07 2021 Andrey Cherepanov <cas@altlinux.org> 2.5.8-alt1
- New version.

* Thu Nov 19 2020 Andrey Cherepanov <cas@altlinux.org> 2.5.7-alt1
- New version.

* Mon Nov 09 2020 Andrey Cherepanov <cas@altlinux.org> 2.5.6-alt1
- New version.

* Sat Aug 22 2020 Andrey Cherepanov <cas@altlinux.org> 2.5.5-alt1
- New version.

* Fri May 15 2020 Andrey Cherepanov <cas@altlinux.org> 2.5.4-alt1
- New version.

* Thu Apr 16 2020 Andrey Cherepanov <cas@altlinux.org> 2.5.3-alt16
- New version.

* Wed Apr 08 2020 Andrey Cherepanov <cas@altlinux.org> 2.5.2-alt15
- New version.

* Wed Dec 11 2019 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt14
- New version.

* Thu Nov 21 2019 Andrey Cherepanov <cas@altlinux.org> 2.5-alt13
- New version.

* Mon Apr 22 2019 Andrey Cherepanov <cas@altlinux.org> 2.4.7-alt12
- New version.

* Mon Apr 08 2019 Andrey Cherepanov <cas@altlinux.org> 2.4.5-alt11
- New version.

* Mon Apr 01 2019 Andrey Cherepanov <cas@altlinux.org> 2.4.4-alt10
- New version.

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.3-alt9
- New version.

* Mon Nov 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.2-alt8
- New version.

* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt7
- New version.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.4-alt6.1
- NMU: Rebuild with new openssl 1.1.0.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 2.4-alt6
- New version.

* Fri May 26 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt5
- New version

* Thu Nov 17 2016 Andrey Cherepanov <cas@altlinux.org> 2.3-alt4
- new version 2.3

* Mon Oct 10 2016 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt3
- New version

* Mon Apr 11 2016 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt2
- New version

* Thu Nov 19 2015 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- Initial build in Sisyphus (thanks Fedora for spec and patches)
