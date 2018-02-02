%define oname sphinxcontrib-ansi
Name: python-module-%oname
Version: 0.6
Release: alt1.1
Summary: Sphinx extension ansi
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-ansi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-sphinx
BuildPreReq: python-module-mock

%py_provides sphinxcontrib.ansi
%py_requires sphinxcontrib sphinx

%description
A Sphinx extension, which turns ANSI color sequences in Sphinx documents
into colored HTML output.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
py.test -vv

%files
%doc README *.rst doc/*.rst
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

