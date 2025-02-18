Name: unvanquished-data
Version: 0.55.2
Release: alt2

Summary: Data files for Unvanquished
License: CC-BY-SA-3.0 and CC-BY-SA-4.0 and GPL and CC0-1.0 and GPL-2.0-only and MIT and CC-BY-SA-2.5 and BSD-3-Clause and GPL-3.0-only
Group: Games/Other

Url: https://unvanquished.net
Vcs: https://github.com/Unvanquished/Unvanquished

ExclusiveArch: x86_64 i586 aarch64

# https://dl.unvanquished.net/
Source: %name-%version.tar

Requires: unvanquished

%description
%summary

%prep
%setup

%build
%install
mkdir -p %buildroot%_datadir/unvanquished/pkg/
cp -r pkg/* %buildroot%_datadir/unvanquished/pkg/

%files
%_datadir/unvanquished/pkg/

%changelog
* Mon Feb 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.55.2-alt2
- rebuilt for x86_64, i586, aarch64 architectures

* Sun Feb 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.55.2-alt1
- Initial build for ALT Linux.

