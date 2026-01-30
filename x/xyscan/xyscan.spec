%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: xyscan
Version: 4.68
Release: alt2

Summary: data thief for scientists
License: GPL-3.0-or-later
Group: Graphics
URL: https://rhig.physics.yale.edu/~ullrich/software/xyscan/
Vcs: https://salsa.debian.org/georgesk/xyscan

Source: %name-%version.tar

Patch: %name-%version-%release.patch

ExcludeArch: loongarch64 riscv64

BuildRequires(pre): rpm-macros-qt5

BuildRequires: qt5-tools
BuildRequires: qt5-base-devel
BuildRequires: dos2unix
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Charts)
BuildRequires: pkgconfig(Qt5Pdf)
BuildRequires: pkgconfig(poppler-qt5)

Requires: xyscan-data

%description
xyscan is a tool for the scientist in the need to extract data points,
i.e. numeric values, from a plot. It allows you to scan the plots and
extract data points including the size of the error bars (both in x
and y). It can handle plots with linear and logarithmic scales. In
fact xyscan can be used for extracting numeric values from any kind
of 2D technical drawings.

%package data
Summary: data thief for scientists - data files
Group: Graphics
BuildArch: noarch

%description data
xyscan is a tool for the scientist in the need to extract data points,
i.e. numeric values, from a plot. It allows you to scan the plots and
extract data points including the size of the error bars (both in x
and y). It can handle plots with linear and logarithmic scales. In
fact xyscan can be used for extracting numeric values from any kind
of 2D technical drawings.

This package contains the architecture independent data files.

%prep
%setup
dos2unix *.txt
sed -i "s|/usr/local|%_prefix|g" src/xyscanBaseWindow.cpp
sed -i "s|Icon=xyscanIcon.png|Icon=xyscan|" debian/xyscan.desktop
sed -i "s|Categories=.*|Categories=Science;|" debian/xyscan.desktop
%patch -p1

%build
lrelease-qt5 xyscan.pro
qmake-qt5 \
          PREFIX=%_prefix \
          CONFIG+=nostrip \
          QMAKE_CXXFLAGS="%optflags" \
          xyscan.pro

%install
%makeinstall_std INSTALL_ROOT=%buildroot

# Install icons and desktop file
for px in 16 24 32 48 64 128 256 512 ; do
  install -Dm 644 images/xyscanLogo${px}.png %buildroot%_iconsdir/hicolor/${px}x${px}/apps/%{name}.png
done
install -Dm 644 debian/xyscan.desktop %buildroot%_desktopdir/%{name}.desktop

# Install man-page
install -Dm 644 debian/xyscan.1 %buildroot%_man1dir/%{name}.1

# Install translations
mkdir -p %buildroot%_qt5_translationdir/
install -Dm 644 translations/%{name}_*.qm %buildroot/%_qt5_translationdir/

%find_lang %name --with-qt

%check
%make_build check

%files -f %{name}.lang
%doc gpl.txt license.txt README.txt
%_bindir/xyscan
%_desktopdir/xyscan.desktop
%_iconsdir/hicolor/*/apps/xyscan.png
%_man1dir/xyscan.1.*

%files data
%dir %_datadir/xyscan
%_datadir/xyscan/*

%changelog
* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 4.68-alt2
- Exclude loongarch64 and riscv64 arches as not buildable.

* Thu Dec 25 2025 Nikolay Strelkov <snk@altlinux.org> 4.68-alt1
- Initial build for Sisyphus
