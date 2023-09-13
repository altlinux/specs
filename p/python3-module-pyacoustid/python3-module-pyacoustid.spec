%define pypi_name pyacoustid

%def_disable check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Python3 bindings for Chromaprint acoustic fingerprinting and the Acoustid API
Group: Development/Python3
License: MIT
Url: https://pypi.python.org/pypi/%pypi_name
Vcs: https://github.com/dwolfhub/zxcvbn-python.git

Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch
Requires: /usr/bin/fpcalc
# or
#Requires: libchromaprint.so.1 python3(audioread)

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel python3-module-setuptools

%{?_enable_check:BuildRequires: python3(pytest)
BuildRequires: python3(audioread) python3(requests)}

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir
py.test3

%files
%python3_sitelibdir/acoustid.py
%python3_sitelibdir/chromaprint.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Wed Sep 13 2023 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Thu Jun 29 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- first build for Sisyphus



