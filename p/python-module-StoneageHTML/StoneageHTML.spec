%define oname StoneageHTML
Name: python-module-%oname
Version: 0.2.1
Release: alt1.dev.git20101119.1
Summary: Stone-Age HTML Filter: prepare documents for e-mail distribution
License: LGPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/StoneageHTML/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/stoneagehtml.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-BeautifulSoup python-module-cssutils

%py_provides stoneagehtml

%description
This package prepares an HTML document for sending by email. The most
common usecase is to find all inline CSS declarations which are directly
written to the HTML tags.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.dev.git20101119.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.dev.git20101119
- Initial build for Sisyphus

