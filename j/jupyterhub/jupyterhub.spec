%def_without check

Name:    jupyterhub
Version: 5.4.5
Release: alt1

Summary: Multi-user server for Jupyter notebooks
License: BSD-3-Clause
Group:   Other
URL:     https://github.com/jupyterhub/jupyterhub

BuildArch: noarch

Source: %name-%version.tar
Patch1: do-not-use-npm.patch

Requires: node-configurable-http-proxy

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

# Tests
%add_python3_req_skip playwright.async_api

%description
%summary

%package -n python3-module-jupyterhub
Summary: Multi-user server for Jupyter notebooks
Group: Development/Python3

%description -n python3-module-jupyterhub
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%_bindir/*
%_datadir/%name

%files -n python3-module-jupyterhub
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Tue May 05 2026 Anton Vyatkin <toni@altlinux.org> 5.4.5-alt1
- new version 5.4.5

* Mon Mar 30 2026 Anton Vyatkin <toni@altlinux.org> 5.4.4-alt1
- new version 5.4.4 (fixes CVE-2026-33709)

* Tue Dec 23 2025 Anton Vyatkin <toni@altlinux.org> 5.4.3-alt1
- new version 5.4.3

* Wed Oct 29 2025 Anton Vyatkin <toni@altlinux.org> 5.4.2-alt1
- new version 5.4.2

* Sat Oct 18 2025 Anton Vyatkin <toni@altlinux.org> 5.4.1-alt1
- new version 5.4.1

* Wed Apr 30 2025 Anton Vyatkin <toni@altlinux.org> 5.3.0-alt1
- new version 5.3.0

* Thu Feb 27 2025 Anton Vyatkin <toni@altlinux.org> 5.2.1-alt1
- Initial build for Sisyphus.
