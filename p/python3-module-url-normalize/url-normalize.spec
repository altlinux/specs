%def_with check

Name: python3-module-url-normalize
Version: 2.2.1
Release: alt1.1

Summary: URI Normalization function
License: MIT
Group: Development/Python
Url: https://pypi.org/project/url-normalize
VCS: https://github.com/niksite/url-normalize

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-idna
%endif

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%_bindir/url-normalize
%python3_sitelibdir/url_normalize
%python3_sitelibdir/url_normalize-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt1.1
- Demodernized packaging.

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.1-alt1
- 2.2.1 released

* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.3-alt1
- 1.4.3 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt1
- initial
