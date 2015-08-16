%define oname didjvu

%def_disable check

Name: python-module-%oname
Version: 0.6.1
Release: alt1
Summary: DjVu encoder with foreground/background separation
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/didjvu
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: xsltproc docbook-style-xsl djvu-utils exiv2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-gamera
BuildPreReq: python-module-Pillow python-module-pyexiv2
BuildPreReq: python-module-libxmp

%py_provides %oname
%py_requires gamera PIL pyexiv2 libxmp
Requires: exiv2

%description
DjVu encoder with foreground/background separation.

%prep
%setup

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
* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

