%define _unpackaged_files_terminate_build 1
%define oname itcase_sphinx_theme
Name: python-module-%oname
Version: 0.2.0
Release: alt1.1
Summary: ITCase Sphinx themes for documentation styling
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/itcase-sphinx-theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ITCase/itcase_sphinx_theme.git
Source0: https://pypi.python.org/packages/ff/de/6da16530baa0cd6ef931048b5f4cceafe9e4137c38a22bae76d46e744eda/itcase-sphinx-theme-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-modules-json

%py_provides %oname

%description
ITCase Sphinx themes for documentation styling.

%prep
%setup -q -n itcase-sphinx-theme-%{version}

%build
%python_build_debug

%install
%python_install

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1
- automated PyPI update

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.git20150723
- Initial build for Sisyphus

