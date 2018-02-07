%define _unpackaged_files_terminate_build 1
%define oname intervals

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt1.1
Summary: Python tools for handling intervals (ranges of comparable objects)
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/intervals/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/intervals.git
Source0: https://pypi.python.org/packages/30/7a/7364356d073426b73014bc6f7aab36914fd9fc53e8d99150a0de69d7846a/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-infinity python-module-six
#BuildPreReq: python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-infinity python3-module-six
#BuildPreReq: python3-module-Pygments
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-docutils python-module-html5lib python-module-infinity python-module-setuptools python3-module-html5lib python3-module-infinity python3-module-setuptools python3-module-sphinx rpm-build-python3 time
BuildRequires: python-module-pytest
BuildRequires: python3-module-pytest

%description
Python tools for handling intervals (ranges of comparable objects).

%package -n python3-module-%oname
Summary: Python tools for handling intervals (ranges of comparable objects)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python tools for handling intervals (ranges of comparable objects).

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
#py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20141209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1.git20141209.1
- NMU: Use buildreq for BR.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141209
- New snapshot

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20141021
- Initial build for Sisyphus

