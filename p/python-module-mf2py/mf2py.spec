%define oname mf2py

%def_with python3

Name: python-module-%oname
Version: 1.0.5
Release: alt1.git20170715.1
Summary: Python Microformats2 parser
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/mf2py/

# https://github.com/tommorris/mf2py.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-requests
BuildRequires: python-module-BeautifulSoup4 python-module-nose
BuildRequires: python-module-gunicorn
BuildRequires: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-requests
BuildRequires: python3-module-BeautifulSoup4 python3-module-nose
BuildRequires: python3-module-mock
%endif

%py_provides %oname
%py_requires html5lib requests bs4 flask gunicorn

%description
Python parser for microformats 2. Full-featured and mostly stable.
Implements the full mf2 spec, including backward compatibility with
microformats1.

%if_with python3
%package -n python3-module-%oname
Summary: Python Microformats2 parser
Group: Development/Python3
%py3_provides %oname
%py3_requires html5lib requests bs4 flask gunicorn

%description -n python3-module-%oname
Python parser for microformats 2. Full-featured and mostly stable.
Implements the full mf2 spec, including backward compatibility with
microformats1.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test
#nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
#nosetests3 -v
popd
%endif

%files
%doc AUTHORS *.md doc/source/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.md doc/source/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1.git20170715.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1.git20170715
- Updated to current upstream version.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150205
- Initial build for Sisyphus

