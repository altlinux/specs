%define _unpackaged_files_terminate_build 1

Name: fast
Version: 0.1.0
Release: alt1

Summary: Test your internet speed from the command-line
License: MIT
Group: Networking/Other
Url: https://github.com/maaslalani/fast
Vcs: https://github.com/maaslalani/fast.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: golang

%description
Test your internet speed from the command-line

%prep
%setup -a1

%build
%gobuild -mod=vendor

%install
install -Dm0755 %name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Wed Aug 05 2026 Mikhail Nogin <joycap@altlinux.org> 0.1.0-alt1
- Initial built for Sisyphus.
