Name: surguch
Version: 0.2
Release: alt1
License: GPL-3.0-or-later

Summary: Verification and creation of digitally signed pdf documents.

Source:  %name-%version.tar

Group: Office

BuildRequires: gcc-c++ cmake ninja-build
BuildRequires: libaltcsp-devel libcsppdf-devel
BuildRequires: libmupdf-devel
BuildRequires:  qt6-base-devel qt6-declarative-devel rpm-macros-qt6 qt6-declarative qt6-svg-devel qt6-svg qt6-tools

Requires: qt6-svg qt6-declarative fonts-ttf-google-noto-sans qt6-wayland qt6-translations

%description
A gui application for verification and creation of digitally signed pdf documents.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release -G Ninja
%cmake_build

%install
%cmake_install

%files
%_bindir/surguch
%_datadir/applications/surguch.desktop
%_datadir/icons/hicolor/scalable/apps/SealWax-1_32.svg
%_datadir/pixmaps/SealWax-1_32.png


%changelog
* Thu Dec 26 2024 Oleg Proskurin <proskur@altlinux.org> 0.2-alt1
- zoom with mouse wheel

* Thu Dec 19 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt2
- License info was added

* Thu Nov 21 2024 Oleg Proskurin <proskur@altlinux.org> 0.1-alt1
- Initial build

