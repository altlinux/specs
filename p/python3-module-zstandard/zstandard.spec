Name: python3-module-zstandard
Version: 0.21.0
Release: alt1.1

Summary: Python bindings for zstandard compression library
License: BSD-3-Clause
Group: Development/Python
Url: https://pypi.org/project/zstandard/

Source0: %name-%version-%release.tar

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)

# Nobody provides it
%add_python3_req_skip zstandard._cffi

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
rm -r zstandard
%pyproject_run_pytest

%files
%python3_sitelibdir/zstandard
%python3_sitelibdir/zstandard-%version.dist-info

%changelog
* Thu Aug 17 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 0.21.0-alt1.1
- NMU: ignored unmet dependency

* Wed May 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21.0-alt1
- 0.21.0 released

* Wed Dec 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.0-alt1
- initial
