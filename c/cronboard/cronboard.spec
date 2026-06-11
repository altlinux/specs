Name: cronboard
Version: 0.7.1
Release: alt1

Summary: A terminal-based dashboard for managing cron jobs locally and on servers
License: MIT
Group: System/Configuration/Other

URL: https://antoniorodr.github.io/cronboard
VCS: https://github.com/antoniorodr/cronboard

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md LICENSE
%_bindir/%name
%python3_sitelibdir/*

%changelog
* Fri Jun 12 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.1-alt1
- automatic build: 0.7.0 -> 0.7.1

* Fri Jun 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt1
- 0.6.2 -> 0.7.0

* Fri May 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.2-alt1
- 0.6.1 -> 0.6.2

* Tue May 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.1-alt1
- 0.6.0 -> 0.6.1

* Sat May 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt1
- 0.5.4 -> 0.6.0

* Fri May 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.5.4-alt1
- 0.5.2 -> 0.5.4

* Mon Apr 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.5.2-alt1
- 0.5.1 -> 0.5.2

* Fri Mar 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.5.1-alt1
- Initial build for ALT Linux.

