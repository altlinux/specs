%define _unpackaged_files_terminate_build 1
%define oname derpconf
Name: python-module-%oname
Version: 0.8.1
Release: alt1.1
Summary: derpconf abstracts loading configuration files for your app
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/derpconf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/globocom/derpconf.git
Source0: https://pypi.python.org/packages/98/2d/4703d2f342faf2d66970f67d7664f24facca299b16983365f3c8ee20a0cd/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-gevent
BuildPreReq: python-module-pyvows python-module-coverage
BuildPreReq: python-module-colorama python-module-tox
BuildPreReq: python-module-six

%py_provides %oname

%description
derpconf abstracts loading configuration files for your app. derpconf
was extracted from thumbor.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.md
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1
- automated PyPI update

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20140930
- Initial build for Sisyphus

