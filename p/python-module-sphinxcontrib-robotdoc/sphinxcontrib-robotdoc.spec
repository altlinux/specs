%define _unpackaged_files_terminate_build 1
%define oname sphinxcontrib-robotdoc
Name: python-module-%oname
Version: 0.8.0
Release: alt1.1
Summary: Sphinx extension to embed Robot Framework test cases and and user keywords
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-robotdoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/datakurre/sphinxcontrib-robotdoc.git
Source0: https://pypi.python.org/packages/bd/03/6105275a3b2db05fe7ea799b504af76a78199bf89f1ebdeb62583fce8fb6/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-Pygments
BuildPreReq: python-module-robotframework

%description
This package provides a Sphinx-extension to embed Robot Framework test
suites, test cases, or user keywords in into Sphinx-documents in spirit
of the autodoc Sphinx-extension.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst PKG-INFO
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- automated PyPI update

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1.git20140905
- Initial build for Sisyphus

