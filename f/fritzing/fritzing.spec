Name: fritzing
Version: 0.9.4
Release: alt1

Summary: Intuitive EDA platform featuring from prototype to product
License: GPLv3, CC-BY-SA-3.0
Group: Engineering

Url: http://fritzing.org
# https://github.com/fritzing/fritzing-app
Source0: %name-%version.tar
# https://github.com/fritzing/fritzing-parts
Source1: %name-parts.tar
# Need to refresh at every update of fritzing-parts
# Execute Fritzing -db parts.db in fritzing-parts directory
Source2: parts.db

Patch: fritzing-desktop-file-translation.patch

# Translations
Patch1: 430dc369b4418f783aa6e367ea5e2dcfdf38a2cf.patch

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires: boost-devel-headers desktop-file-utils gcc-c++ glibc-devel-static
BuildRequires: phonon-devel rpm-build-python3 rpmbuild-helper-desktop
BuildRequires: rpmbuild-helper-sugar-activity ruby ruby-stdlibs qt5-tools
BuildRequires: libgit2-devel qt5-base-devel qt5-svg-devel qt5-serialport-devel

# large chunk of arch-independent data is better not duplicated
Requires: %name-data = %EVR

%description
Fritzing is an open-source initiative to support designers, artists,
researchers and hobbyists to take the step from physical prototyping
to actual product. It is in the spirit of Processing and Arduino which
allows users to document their Arduino and other electronic-based
prototypes, and to create a PCB layout for manufacturing.

%package data
Summary: Data files for %name
License: GPLv3
Group: Engineering
BuildArch: noarch

%description data
Fritzing is an open-source initiative to support designers, artists,
researchers and hobbyists to take the step from physical prototyping
to actual product. It is in the spirit of Processing and Arduino which
allows users to document their Arduino and other electronic-based
prototypes, and to create a PCB layout for manufacturing.

This package contains shared data files for Fritzing.

%prep
%setup -a1

# Dynamically link against system libgit2
sed -i 's/LIBGIT_STATIC = true/LIBGIT_STATIC = false/' phoenix.pro

%patch -p1
%patch1 -p1

# make sure that russian translation will be removed
rm translations/fritzing_ru.qm

# rebuild russian translation
lrelease-qt5 phoenix.pro

%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
qmake-qt5
%make_build debug

%install
%makeinstall_std INSTALL_ROOT=%buildroot debug-install

cp -r %name-parts %buildroot/%_datadir/%name

install -m0644 %SOURCE2 "%buildroot/%_datadir/%name/%name-parts/parts.db"

%files
%doc LICENSE.*
%_bindir/Fritzing
%_pixmapsdir/%name.png
%_desktopdir/org.fritzing.Fritzing.desktop
%_datadir/metainfo/org.fritzing.Fritzing.appdata.xml
%_man1dir/Fritzing.*
%_datadir/mime/packages/%name.xml
%_datadir/metainfo

%files data
%_datadir/%name

%changelog
* Thu Dec 26 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.4-alt1
- Fix version.
- Cleanup changelog.

* Mon Dec 02 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.3b.0.312.git6efd5ec2-alt1
- Build from last commit.
- Update parts.
- Update russian translation.

* Tue Jul 16 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.3b.0.31.git701e3a3-alt5
- Add russian translation to desktop file (Closes: #36850).

* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 0.9.3b.0.31.git701e3a3-alt4
- E2K: strip UTF-8 BOM for lcc < 1.24

* Tue Jul 17 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.3b.0.31.git701e3a3-alt3
- Fixed FTBFS (removed xdg macro).

* Thu Feb 01 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.3b.0.31.git701e3a3-alt2
- Add missing part definitions.

* Wed Jan 31 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.3b.0.31.git701e3a3-alt1
- Build new version (Closes: #30924).
- Transfer to Qt5.

* Thu Jun 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.7b-alt3
- Updated build for new toolchain

* Tue Apr 22 2014 Michael Shigorin <mike@altlinux.org> 0.8.7b-alt2
- rebuilt for Sisyphus
- minor spec cleanup

* Sat Apr 19 2014 Konstantin Kogan <kostyalamer at yandex.ru> 0.8.7b-alt1
- First build for ALT Linux t7
