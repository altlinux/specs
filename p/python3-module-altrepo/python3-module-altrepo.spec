%define oname altrepo

Name: python3-module-%oname
Version: 0.4.0
Release: alt1
License: AGPL-3.0-or-later

Summary: Async Python client for ALT Linux repository services

Group: Development/Python3

Url: https://pypi.org/project/altrepo/
VCS: https://gitlab.eterfund.ru/fiersik/python3-module-altrepo.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-poetry-core

%description
Async Python client for ALT Linux repository services:
 - rdb.altlinux.org API (packages, tasks, maintainers, bugs and more)
 - sisyphus-cybertalk news parser
 - watch.altlinux.org package tracking
 - FTBFS lists
 - AppStream metadata

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sat Jun 20 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.4.0-alt1
- new version 0.4.0

* Fri Apr 03 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.3.0-alt1
- new version 0.3.0

* Sat Mar 14 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- Initial build
