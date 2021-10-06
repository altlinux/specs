%define modname fasttext
%def_disable check

Name: python3-module-%modname
Version: 0.9.2
Release: alt1

Summary: Python3 word representations and sentence classification library
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%modname

Vcs: https://github.com/facebookresearch/fastText.git
Source: https://pypi.io/packages/source/f/%modname/%modname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ python3-module-setuptools
BuildRequires: python3-module-numpy python3-module-pybind11
%{?_enable_check:BuildRequires: python3-module-pytest python3-module-six}

%description
fastText is a library for efficient learning of word representations and
sentence classification.

%prep
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir/*
%doc README*

%changelog
* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- first build for Sisyphus




