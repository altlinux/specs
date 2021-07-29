%define _unpackaged_files_terminate_build 1

Name: qvge
Version: 0.6.3
Release: alt1
Summary: Qt Visual Graph Editor
Group: Development/Other
License: MIT
Url: https://github.com/ArsMasiuk/qvge

# https://github.com/ArsMasiuk/qvge.git
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel qt5-svg-devel qt5-x11extras-devel

%description
QVGE is a multiplatform graph editor written in C++/Qt.
Its main goal is to make possible visually edit two-dimensional graphs
in a simple and intuitive way.

%prep
%setup

%build
cd src
%qmake_qt5 PREFIX=%_prefix CONFIG+=nostrip
%make_build

%install
cd src
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc LICENSE
%doc CHANGES README.md
%_bindir/qvgeapp
%_datadir/appdata/%name.appdata.xml
%_datadir/mime/packages/application-xgr.xml
%_datadir/pixmaps/%name.png
%_desktopdir/%name.desktop

%changelog
* Thu Jul 29 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.3-alt1
- Updated to upstream version 0.6.3.

* Mon Nov 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1
- Initial build for ALT.
