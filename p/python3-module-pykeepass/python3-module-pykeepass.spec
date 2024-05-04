# no tests in tarball
%def_enable snapshot
%define beta .post1
%define pypi_name pykeepass

%def_enable check

Name: python3-module-%pypi_name
Version: 4.0.7
Release: alt1%beta

Summary: Python library to interact with KeePass databases
Group: Development/Python3
License: GPL-3.0
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/libkeepass/pykeepass.git
%if_disabled snapshot
Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version%beta.tar.gz
%else
Source: %pypi_name-%version%beta.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest) python3(pyotp)
BuildRequires: python3(construct) python3(lxml) python3(Cryptodome)
BuildRequires: python3(argon2)}
BuildRequires: dos2unix

%description
Python library to interact with KeePass databases.

%prep
%setup -n %pypi_name-%version%beta
dos2unix pyproject.toml
sed -i 's|^\(packages = .*%{pypi_name}\"\)|\1, "pykeepass.kdbx_parsing"|' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
%__python3 tests/tests.py

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README* CHANGELOG*


%changelog
* Sat May 04 2024 Yuri N. Sedunov <aris@altlinux.org> 4.0.7-alt1.post1
- 4.0.7.post1 (4.0.7-11-g66bc409)

* Fri Mar 01 2024 Yuri N. Sedunov <aris@altlinux.org> 4.0.7-alt1
- updated to 4.0.7-1-g769ee25
- enabled %%check

* Wed Aug 23 2023 Yuri N. Sedunov <aris@altlinux.org> 4.0.6-alt1
- 4.0.6

* Fri Jun 23 2023 Yuri N. Sedunov <aris@altlinux.org> 4.0.5-alt1
- first build for Sisyphus



