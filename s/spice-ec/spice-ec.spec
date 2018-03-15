Name: spice-ec
Version: 1.0.1
Release: alt1%ubt

Summary: Spice Easy Connect
License: GPLv3
Group: Networking/Remote access

Url: http://git.altlinux.org/people/mvoronov/packages/spice-ec.git 
Source: %name-%version.tar

Requires: virt-viewer

BuildRequires(pre): rpm-build-ubt rpm-macros-cmake cmake
BuildRequires: qt5-base-devel

%description
SPICE remote viewer launcher

%prep
%setup

%build
%cmake_insource
%make_build VERBOSE=1

%install
%makeinstall_std

%files
%_bindir/*
%_desktopdir/*

%changelog
* Thu Mar 15 2018 Maxim Voronov <mvoronov@altlinux.org> 1.0.1-alt1%ubt
- new version

* Mon Mar 12 2018 Maxim Voronov <mvoronov@altlinux.org> 1.0.0-alt1%ubt
- initial build

