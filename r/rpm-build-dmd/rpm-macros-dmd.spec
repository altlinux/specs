Name:      rpm-build-dmd
Version:   1.0
Release:   alt1
Summary:   RPM helper macros to build D lang(dmd) packages
Group:     Development/Other
License:   GPL
BuildArch: noarch

Source0:   dmd.macros

Requires:  dmd

%description
%summary.

%install
mkdir -p %buildroot%_rpmmacrosdir
cp %SOURCE0 %buildroot%_rpmmacrosdir/dmd

%files
%_rpmmacrosdir/dmd

%changelog
* Sun Apr 15 2018 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- Initial build

