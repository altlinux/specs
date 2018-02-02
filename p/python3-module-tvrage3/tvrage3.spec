%define oname tvrage3

%def_disable check

Name: python3-module-%oname
Version: 0.1.1
Release: alt2.git20140510.1.1
Summary: Python3 client for accessing tv show information from www.tvrage.com
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/tvrage3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kalind/tvrage3.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-xmltodict
BuildPreReq: python3-module-sphinx-devel rpm-macros-sphinx3

%py3_provides %oname

%description
Python3 client for accessing tv show information from www.tvrage.com.

%package docs
Summary: Documentation for %oname
Group: Development/Python3
BuildArch: noarch

%description docs
Python3 client for accessing tv show information from www.tvrage.com.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 .
#ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

%make -C docs html

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*

%files docs
%doc docs/_build/html/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt2.git20140510.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt2.git20140510.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 26 2016 Denis Medvedev <nbr@altlinux.org> 0.1.1-alt2.git20140510
- Fix sphinx doc build.

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20140510
- Initial build for Sisyphus

