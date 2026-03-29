%define _unpackaged_files_terminate_build 1
%define pypi_name httptools
%define mod_name %pypi_name

%def_with check

# %%python3_set_limited_api is not supported yet

Name: python3-module-%pypi_name
Version: 0.7.1
Release: alt1.1
Summary: A collection of framework independent HTTP protocol utils
License: MIT
Group: Development/Python
Url: https://pypi.org/project/httptools/
Vcs: https://github.com/MagicStack/httptools
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: libhttp-parser-devel
BuildRequires: libllhttp-devel
BuildRequires: python3-module-cython

%description
%summary

%prep
%setup
%autopatch -p1
rm -r vendor

%build
%pyproject_build --backend-config-settings='{"--build-option": ["build_ext", "--cython-always", "--use-system-http-parser", "--use-system-llhttp"]}'

%install
%pyproject_install
# remove Cython dev files
rm -v %buildroot%python3_sitelibdir/%mod_name/parser/*.{pyx,pxd}

%check
# .github/workflows/tests.yml
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eux
mkdir empty
cd empty
python -m unittest discover -v ../tests
ENDTESTS

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.7.1-alt1.1
- Demodernized packaging.

* Fri Dec 12 2025 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- 0.6.4 -> 0.7.1.

* Tue Oct 22 2024 Stanislav Levin <slev@altlinux.org> 0.6.4-alt1
- 0.1.1 -> 0.6.4.

* Thu Feb 11 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.1-alt1
- initial
