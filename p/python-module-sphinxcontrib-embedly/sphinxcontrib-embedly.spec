%define oname sphinxcontrib-embedly
Name: python-module-%oname
Version: 0.2
Release: alt1.git20140223.1
Summary: This is a sphinx extension for using Embedly
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-embedly/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jezdez/sphinxcontrib-embedly.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-Embedly
BuildPreReq: python-module-sphinx

%py_provides sphinxcontrib.embedly
%py_requires sphinx sphinxcontrib embedly

%description
This extension enables you to embed anything that is supported by
Embedly.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc AUTHORS *.rst
%python_sitelibdir/sphinxcontrib/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.git20140223.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20140223
- Initial build for Sisyphus

