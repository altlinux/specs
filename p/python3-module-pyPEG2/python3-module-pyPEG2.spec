%global srcname pyPEG2

Name: python3-module-%srcname
Version: 2.15.2
Release: alt2
Summary: A PEG Parser-Interpreter in Python
#%{?python_provide:%python_provide python3-%srcname}
Packager: Ilya Mashkin <oddity@altlinux.ru>
License: GPLv2
Url: http://fdik.org/pyPEG
Source0: https://pypi.python.org/packages/source/p/%srcname/%srcname-%version.tar.gz
Group: Development/Python3

BuildArch: noarch

#BuildRequires: python3-devel python3-pytest
#Requires: python3-lxml
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
pyPEG is a plain and simple intrinsic parser interpreter framework for Python
version 3.x. It is based on Parsing Expression Grammar, PEG.
With pyPEG you can parse many formal languages in a very easy way.

%prep
%setup -n %srcname-%version

%build
%python3_build

%install
%python3_install

#check
#PYTHONPATH=. py.test-%_python3_version pypeg2/test

%files
#license LICENSE.txt
%doc README.txt CHANGES.txt PKG-INFO docs
%python3_sitelibdir/%srcname-%version-py?.??.egg-info
%python3_sitelibdir/pypeg2

%changelog
* Sun May 01 2022 Ilya Mashkin <oddity@altlinux.ru> 2.15.2-alt2
- Fix FTBFS

* Thu Oct 11 2018 Ilya Mashkin <oddity@altlinux.ru> 2.15.2-alt1
- build for Sisyphus

* Tue Feb 16 2016 Tomas Orsava <torsava@redhat.com> - 2.15.2-1
- Let there be package.
- This package is needed as a dependency for qutebrowser.

