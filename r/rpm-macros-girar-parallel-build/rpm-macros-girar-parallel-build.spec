# vim: set ft=spec: -*- rpm-spec -*-

Name: rpm-macros-girar-parallel-build
Version: 2010.12.14
Release: alt1

Summary: RPM macros for automatic parallel build on girar server
Group: Development/Other
License: DWTFYWTPL

BuildArch: noarch

Source: girar-parallel-build.macros

%description
This package contains RPM macros for automatic parallel build on
girar server.

%install
mkdir -p %buildroot%_rpmmacrosdir
install -pm644 %_sourcedir/girar-parallel-build.macros %buildroot%_rpmmacrosdir/girar-parallel-build

%files
%_rpmmacrosdir/girar-parallel-build

%changelog
* Tue Dec 14 2010 Alexey I. Froloff <raorn@altlinux.org> 2010.12.14-alt1
- Initial build

