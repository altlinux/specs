%define oname humanize

%def_with python3

Name: python-module-%oname
Version: 0.5.1
Release: alt1.git20141113.1.1
Summary: Python humanize utilities
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/humanize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jmoiron/humanize.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-mock
%endif

%py_provides %oname

%description
This modest package contains various common humanization utilities, like
turning a number into a fuzzy human readable duration ('3 minutes ago')
or into a human readable size or throughput. It works with python 2.7
and 3.3 and is localized to Russian, French, and Korean.

%package -n python3-module-%oname
Summary: Python humanize utilities
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This modest package contains various common humanization utilities, like
turning a number into a fuzzy human readable duration ('3 minutes ago')
or into a human readable size or throughput. It works with python 2.7
and 3.3 and is localized to Russian, French, and Korean.

%prep
%setup

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
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1.git20141113.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20141113.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20141113
- Initial build for Sisyphus

