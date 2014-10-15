%define oname cssmin

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20131014
Summary: A Python port of the YUI CSS compression algorithm
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/cssmin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zacharyvoase/cssmin.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
A Python port of the YUI CSS compression algorithm.

%package -n python3-module-%oname
Summary: A Python port of the YUI CSS compression algorithm
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A Python port of the YUI CSS compression algorithm.

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
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20131014
- Initial build for Sisyphus

