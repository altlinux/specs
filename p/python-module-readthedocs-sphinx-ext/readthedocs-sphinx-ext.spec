
%define oname readthedocs-sphinx-ext
Name: python-module-%oname
Version: 0.4.3
Release: alt1.git20141102.1
Summary: This holds code specific for Read the Docs and Sphinx
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/readthedocs-sphinx-ext/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rtfd/readthedocs-sphinx-ext.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools

%py_provides readthedocs_ext

%description
Tooling for a better Read the Docs Sphinx build experience.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1.git20141102.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.git20141102
- Initial build for Sisyphus

