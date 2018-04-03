Name: pve-spice-client
Version: 1.2.0
Release: alt1%ubt

Summary: PVE Spice Client
License: GPLv3
Group: Networking/Remote access

Url: https://github.com/mxmvoronov/pve-spice-client.git 
Source: %name-%version.tar

Requires: virt-viewer
Provides: spice-ec = %EVR
Obsoletes: spice-ec < %EVR

BuildRequires(pre): rpm-build-ubt rpm-macros-cmake cmake
BuildRequires: qt5-base-devel libqtkeychain-qt5-devel

%description
Spice remote viewer launcher

%prep
%setup

%build
%cmake_insource
%make_build VERBOSE=1

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README.md
%_bindir/*
%_desktopdir/*

%changelog
* Fri Mar 30 2018 Maxim Voronov <mvoronov@altlinux.org> 1.2.0-alt1%ubt
- new version

* Wed Mar 21 2018 Maxim Voronov <mvoronov@altlinux.org> 1.1.1-alt1%ubt
- new version

* Mon Mar 19 2018 Maxim Voronov <mvoronov@altlinux.org> 1.1.0-alt1%ubt
- new version

* Thu Mar 15 2018 Maxim Voronov <mvoronov@altlinux.org> 1.0.1-alt1%ubt
- new version

* Mon Mar 12 2018 Maxim Voronov <mvoronov@altlinux.org> 1.0.0-alt1%ubt
- initial build

