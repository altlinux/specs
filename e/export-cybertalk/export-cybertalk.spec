Name: export-cybertalk
Version: 0.5
Release: alt1

License: AGPL-3.0-or-later
Group: Other

URL: https://altlinux.space/shad/export-cybertalk
VCS: https://altlinux.space/shad/export-cybertalk

Summary: Simple CLI utility for export Sisyphus|p1* news

BuildArch: noarch
AutoProv: nopython3

BuildRequires(pre): rpm-build-python3

Source: %name-%version.tar

%description
Simple CLI utility for export in text file or show Sisyphus|p1* news.

Supports automatic translation into Russian.

%prep
%setup

%build
%install
install -Dm755 %name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc LICENSE *.md

%changelog
* Wed Aug 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.5-alt1
- 0.4 -> 0.5

* Fri Aug 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.4-alt1
- 0.3 -> 0.4

* Sat Jul 18 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.3-alt1
- 0.2 -> 0.3

* Tue Jul 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.2-alt1
- Initial build.

