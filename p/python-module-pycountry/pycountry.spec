%define oname pycountry
Name: python-module-%oname
Version: 0.14.5
Release: alt1
Summary: ISO country, subdivision, language, currency and script definitions
License: LGPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/pycountry
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
ISO country, subdivision, language, currency and script definitions and
their translations.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt PKG-INFO
%python_sitelibdir/*

%changelog
* Fri Sep 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.5-alt1
- Initial build for Sisyphus

