%define _unpackaged_files_terminate_build 1
%define oname statistics

Name: python-module-%oname
Version: 3.4.0
Release: alt2.b3
Summary: A Python 2.* port of 3.4 Statistics Module
License: Python Software Foundation
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/statistics

# https://github.com/digitalemagine/py-statistics.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools

%description
A port of Python 3.4 statistics module to Python 2.*, initially done through the 3to2 tool.

This module provides functions for calculating mathematical statistics of numeric (Real-valued) data.

%prep
%setup
grep -qsP 'install_requires = \[\x27docutils>=0.3\x27\],' setup.py || exit 1
sed -i '/install_requires = \[\x27docutils>=0.3\x27\],/d' setup.py

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc LICENSE README.rst
%python_sitelibdir/*

%changelog
* Fri Dec 21 2018 Stanislav Levin <slev@altlinux.org> 3.4.0-alt2.b3
- Dropped requirement on docutils.

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.0-alt1.b3
- Initial build for ALT.
