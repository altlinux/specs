%define oname wheel

Name: python3-module-%oname
Version: 0.34.2
Release: alt1
Summary: A built-package format for Python3
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/wheel/
Packager: Python Development Team <python@packages.altlinux.org>

# Source-url: https://bitbucket.org/pypa/wheel/get/%version.tar.gz
Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-keyring python3-module-pytest-cov python3-module-pyxdg python3-module-setuptools
%py3_provides %oname

%description
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.txt
%_bindir/*
%python3_sitelibdir/*

%changelog
* Sat Apr 11 2020 Alexey Shabalin <shaba@altlinux.org> 0.34.2-alt1
- 0.34.2

