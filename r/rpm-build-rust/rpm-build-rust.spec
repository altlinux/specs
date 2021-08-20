Name:      rpm-build-rust
Version:   0.1.2
Release:   alt1
Summary:   RPM build enviroment to build rust packages
Group:     Development/Other
License:   GPLv2
BuildArch: noarch
Packager:  Mikhail Gordeev <obirvalger@altlinux.ru>

Source0:   rust.macros

Requires:  rust-cargo rpm-macros-rust

%description
RPM build enviroment to build rust packages

%package -n rpm-macros-rust
Summary: RPM helper macros to build rust packages
Group: Development/Other
BuildArch:      noarch

%description -n rpm-macros-rust
These helper macros provide possibility to create rust packages.

%install
mkdir -p %buildroot/%_rpmmacrosdir

cp %SOURCE0 %buildroot%_rpmmacrosdir/rust

%files

%files -n rpm-macros-rust
%_rpmmacrosdir/rust

%changelog
* Fri Aug 20 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.2-alt1
- Add parameters to macros

* Tue Aug 03 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.1-alt1
- Remove target specifiaction

* Tue Jun 22 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.0-alt1
- Initila build
