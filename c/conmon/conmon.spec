Name: conmon
Version: 0
Release: alt1.8fba2062.1

Summary: OCI container runtime monitor
License: Apache-2.0
Group:    System/Configuration/Other
Url: https://github.com/projectatomic/conmon

Source: %name-%version.tar

BuildRequires: glib2-devel glibc-devel

%description
%summary.

%prep
%setup

%build
%make_build

%install
install -Dm 755 bin/conmon %buildroot/%_bindir/conmon

%files
%doc README.md
%_bindir/conmon

%changelog
* Tue Jan 08 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0-alt1.8fba2062.1
- Initial build for Sisyphus
