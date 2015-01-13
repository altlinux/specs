%define oname doxx

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20150112
Summary: Simple, flexible text file templating engine
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/doxx/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/chrissimpkins/doxx.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Naked python-modules-json
BuildPreReq: python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Naked
BuildPreReq: python3-module-requests
%endif

%py_provides %oname
%py_requires Naked

%description
Simple, flexible text file templating engine.

%package -n python3-module-%oname
Summary: Simple, flexible text file templating engine
Group: Development/Python3
%py3_provides %oname
%py3_requires Naked

%description -n python3-module-%oname
Simple, flexible text file templating engine.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md docs/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150112
- Initial build for Sisyphus

