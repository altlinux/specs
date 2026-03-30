Name: python3-module-fnvhash
Version: 0.2.1
Release: alt1.1

Summary: Pure Python FNV hash implementation
License: MIT
Group: Development/Python
Url: https://pypi.org/project/fnvhash
VCS: https://github.com/znerol/py-fnvhash

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v

%files
%python3_sitelibdir/fnvhash
%python3_sitelibdir/fnvhash-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt1.1
- Demodernized packaging.

* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt1
- 0.2.1 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.0-alt1
- initial

