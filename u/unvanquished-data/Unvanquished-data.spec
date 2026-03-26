Name: unvanquished-data
Version: 0.56.1
Release: alt1

Summary: Data files for Unvanquished
License: CC-BY-SA-3.0 and CC-BY-SA-4.0 and GPL and CC0-1.0 and GPL-2.0-only and MIT and CC-BY-SA-2.5 and BSD-3-Clause and GPL-3.0-only
Group: Games/Other

Url: https://unvanquished.net
Vcs: https://github.com/Unvanquished/Unvanquished

ExclusiveArch: x86_64 i586 aarch64

# https://dl.unvanquished.net/
Source: %name-%version.tar

BuildArch: noarch

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
* Thu Mar 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.56.1-alt1
- 0.55.5 -> 0.56.1

* Tue Sep 30 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.55.5-alt1
- 0.55.4 -> 0.55.5

* Tue May 27 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.55.4-alt1
- 0.55.3 -> 0.55.4

* Wed Apr 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.55.3-alt1
- 0.55.2 -> 0.55.3

* Mon Feb 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.55.2-alt2
- rebuilt for x86_64, i586, aarch64 architectures

* Sun Feb 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.55.2-alt1
- Initial build for ALT Linux.

