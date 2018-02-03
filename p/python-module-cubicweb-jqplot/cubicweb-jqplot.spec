%define _unpackaged_files_terminate_build 1
%define oname cubicweb-jqplot
Name: python-module-%oname
Version: 0.4.2
Release: alt1.1
Summary: Views wrapping jqPlot graphic library
License: LGPL & MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-jqplot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/09/d9/a5978b64676507863b6f707bd3021622306a9e03fbe25fe836cc7d6a3f33/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-markdown

Requires: cubicweb

%description
This is the CubicWeb integration of Chris Leonello's jqPlot library,
which is included under the data subdirectory, along with it's license
(MIT).

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README PKG-INFO
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1
- automated PyPI update

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

