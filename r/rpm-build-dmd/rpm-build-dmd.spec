
Name: rpm-build-dmd
Version: 2.0
Release: alt1
Summary: RPM build enviroment to build D lang(dmd) packages
Group: Development/Other
Url: https://packages.altlinux.org/en/Sisyphus/srpms/%name
License: GPL
BuildArch: noarch
Source1: dmd.macros

%ifarch %ix86 x86_64
Requires: dmd
%endif
Requires: rpm-macros-dmd >= %EVR

%description
%summary.

%package -n rpm-macros-dmd
Summary: RPM helper macros to build D lang(dmd) packages
Group: Development/Other
BuildArch: noarch

%description -n rpm-macros-dmd
%summary.

%install
mkdir -p %buildroot%_rpmmacrosdir
cp %SOURCE1 %buildroot%_rpmmacrosdir/dmd

#TODO add scripts for dmd
%files

%files -n rpm-macros-dmd
%_rpmmacrosdir/dmd

%changelog
* Sat Sep 22 2018 Alexey Shabalin <shaba@altlinux.org> 2.0-alt1
- add empty rpm-build-dmd package

* Sun Apr 15 2018 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- Initial build
