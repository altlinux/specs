# Because upstream is not good about bumping the library version for ABI
# incompatible changes the Release should not be reset to 1 unless both version
# numbers change, otherwise the NEVR of the library may cause a package not to
# be updated even if it should be.
%global srcname tqsl
%global tqslver 2.3
%global libtqslver 2.5

Name:           trustedqsl
Version:        2.3
Release:        alt4
Summary:        TrustedQSL ham-radio applications

Group:		Communications
License:        BSD
URL:            http://www.rickmurphy.net/trustedqsl.org/

Source0:        %srcname-%version.tar

Patch0:         tqsl-2.0-rpath.patch
Patch1:         tqsl-tqsllib.patch
Patch2:         tqsl-fix-undefined-macro.patch
Patch3:         tqsl-ssl-md5.patch

BuildRequires(pre): cmake
BuildRequires:  gcc-c++
BuildRequires:  libdb4-devel
BuildRequires:  libssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexpat-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils

Requires:       curl

%description
The TrustedQSL applications are used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the GUI applications tqslcert and tqsl.

%package -n tqsllib
Version:        %libtqslver
Summary:        TrustedQSL library
Group:		System/Libraries

%description -n tqsllib
The TrustedQSL library is used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the library and configuration files needed to run
TrustedQSL applications.

%package -n tqsllib-devel
Version:        %libtqslver
Summary:        Development files the for TrustedQSL library
Group:		Development/C++
Requires:       tqsllib = %libtqslver-%release

%description -n tqsllib-devel
The TrustedQSL library is used for generating digitally signed
QSO records (records of Amateur Radio contacts). This package
contains the to develop with tqsllib.

%prep
%setup -q -n %srcname-%tqslver
%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmakeinstall_std

# Install desktop files
mkdir -p %buildroot%_desktopdir
sed -i -e "s/.png//g" -e "s/Application;/Network;/g" -e "s/Utility;/GTK;/g" apps/tqsl.desktop
desktop-file-install \
        --dir=%buildroot%_desktopdir apps/tqsl.desktop

# Install icons
for size in 16 32 48 64 128; do
    install -Dpm 0644 apps/icons/key${size}.png \
    %buildroot%_iconsdir/hicolor/${size}x${size}/apps/TrustedQSL.png
done

%find_lang --output=%name.lang tqslapp
rm -f %buildroot%_datadir/locale/*/LC_MESSAGES/wxstd.mo

%files -f %name.lang
%doc AUTHORS.txt LICENSE.txt README
%_bindir/tqsl
%_datadir/TrustedQSL
%_desktopdir/tqsl.desktop
%_iconsdir/hicolor/*/apps/TrustedQSL.png
%_pixmapsdir/TrustedQSL.png
%_man5dir/*.5*

%files -n tqsllib
%doc src/LICENSE src/ChangeLog.txt
%_libdir/libtqsllib.so.%libtqslver

%files -n tqsllib-devel
%_includedir/*
%_libdir/libtqsllib.so

%changelog
* Thu Nov 17 2016 Andrey Cherepanov <cas@altlinux.org> 2.3-alt4
- new version 2.3

* Mon Oct 10 2016 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt3
- New version

* Mon Apr 11 2016 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt2
- New version

* Thu Nov 19 2015 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- Initial build in Sisyphus (thanks Fedora for spec and patches)
