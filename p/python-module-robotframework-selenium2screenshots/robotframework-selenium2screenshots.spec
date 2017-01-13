%define _unpackaged_files_terminate_build 1
%define oname robotframework-selenium2screenshots

%def_with python3

Name: python-module-%oname
Version: 0.7.2
Release: alt1
Summary: Robot Framework keyword library for capturing annotated screenshots with Selenium2Library
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-selenium2screenshots/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/datakurre/robotframework-selenium2screenshots.git
Source0: https://pypi.python.org/packages/3b/0c/931fabf75c9954fc54f99d95147cdfc94bf448cd89b3fec899ddefb98d20/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-module-setuptools-tests python-module-robotframework
#BuildPreReq: python-module-robotframework-selenium2library
#BuildPreReq: python-module-Pillow python-module-docutils
#BuildPreReq: python-module-decorator
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-module-setuptools-tests python3-module-robotframework
#BuildPreReq: python3-module-robotframework-selenium2library
#BuildPreReq: python3-module-Pillow python3-module-docutils
#BuildPreReq: python3-module-decorator
%endif

%py_requires PIL

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-pytest python-module-pytz python-module-robotframework python-module-setuptools python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-robotframework python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-cffi python-module-docutils python-module-html5lib python-module-robotframework-selenium2library python-module-setuptools-tests python3-module-cffi python3-module-html5lib python3-module-robotframework-selenium2library python3-module-setuptools-tests python3-module-sphinx rpm-build-python3

%description
Robot Framework keyword library for capturing annotated screenshots with
Selenium2Library.

%if_with python3
%package -n python3-module-%oname
Summary: Robot Framework keyword library for capturing annotated screenshots with Selenium2Library
Group: Development/Python3
%py3_requires PIL

%description -n python3-module-%oname
Robot Framework keyword library for capturing annotated screenshots with
Selenium2Library.
%endif

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst docs
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt2.git20140720.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt2.git20140720.1
- NMU: Use buildreq for BR.

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.git20140720
- Added module for Python 3

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20140720
- Initial build for Sisyphus

