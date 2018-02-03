%define _unpackaged_files_terminate_build 1
%define oname didjvu

%def_disable check

Name: python-module-%oname
Version: 0.8.1
Release: alt1.1
Summary: DjVu encoder with foreground/background separation
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/didjvu
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/d1/4c/5ceedb3d8fcdd4a886e7e6344e6a0c31fb205d20e26413bd914d62187e95/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: xsltproc docbook-style-xsl djvu-utils exiv2
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-gamera
BuildPreReq: python-module-Pillow python-module-pyexiv2
BuildPreReq: python-module-libxmp

%py_provides %oname
%py_requires gamera PIL pyexiv2 libxmp
Requires: exiv2

%description
DjVu encoder with foreground/background separation.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

rm -f doc/*.1
python setup.py build_doc

%install
%python_install

%check
python setup.py test -v

%files
%doc doc/changelog doc/*.txt
%_bindir/*
%python_sitelibdir/*
%_man1dir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1
- automated PyPI update

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

