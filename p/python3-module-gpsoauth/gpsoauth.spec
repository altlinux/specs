%def_with check

Name: python3-module-gpsoauth
Version: 1.0.0
Release: alt2

Summary: Python API for google play services oauth
License: MIT
Group: Development/Python
Url: https://pypi.org/project/gpsoauth/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3

# build backend and its deps
BuildRequires: python3(poetry-core)

%if_with check
BuildRequires: python3(requests)
BuildRequires: python3(pycryptodomex)

# pycryptodome is used, but is not specified in deps; fixed in upstream
BuildRequires: python3(Crypto)

BuildRequires: python3(pytest)
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
%tox_create_default_config
%tox_check_pyproject

%files
%python3_sitelibdir/gpsoauth
%python3_sitelibdir/gpsoauth-%version.dist-info/

%changelog
* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 1.0.0-alt2
- NMU: Modernized packaging (fixes FTBFS due to poetry-core 1.1.0).

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

* Mon Jul 27 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- initial
