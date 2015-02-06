%define oname mf2py

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt1.git20150205
Summary: Python Microformats2 parser
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/mf2py/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tommorris/mf2py.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-html5lib python-module-requests
BuildPreReq: python-module-BeautifulSoup4 python-module-nose
BuildPreReq: python-module-flask python-module-gunicorn
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-html5lib python3-module-requests
BuildPreReq: python3-module-BeautifulSoup4 python3-module-nose
BuildPreReq: python3-module-flask python3-module-gunicorn
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires html5lib requests bs4 flask gunicorn

%description
Python parser for microformats 2. Full-featured and mostly stable.
Implements the full mf2 spec, including backward compatibility with
microformats1.

%package -n python3-module-%oname
Summary: Python Microformats2 parser
Group: Development/Python3
%py3_provides %oname
%py3_requires html5lib requests bs4 flask gunicorn

%description -n python3-module-%oname
Python parser for microformats 2. Full-featured and mostly stable.
Implements the full mf2 spec, including backward compatibility with
microformats1.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150205
- Initial build for Sisyphus

