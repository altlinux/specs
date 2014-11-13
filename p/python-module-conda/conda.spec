%define oname conda

%def_with python3

Name: python-module-%oname
Version: 3.7.3
Release: alt1.git20141105
Summary: Cross-platform, Python-agnostic binary package manager
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/conda/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/conda/conda.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: git python-devel python-module-setuptools-tests
BuildPreReq: python-module-pycosat python-module-yaml
BuildPreReq: python-module-requests python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pycosat python3-module-yaml
BuildPreReq: python3-module-requests
%endif

%py_provides %oname
%py_requires json

%description
Conda is a cross-platform, Python-agnostic binary package manager. It is
the package manager used by Anaconda installations, but it may be used
for other systems as well. Conda makes environments first-class
citizens, making it easy to create independent environments even for C
libraries. Conda is written entirely in Python, and is BSD licensed open
source.

%package -n python3-module-%oname
Summary: Cross-platform, Python-agnostic binary package manager
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Conda is a cross-platform, Python-agnostic binary package manager. It is
the package manager used by Anaconda installations, but it may be used
for other systems as well. Conda makes environments first-class
citizens, making it easy to create independent environments even for C
libraries. Conda is written entirely in Python, and is BSD licensed open
source.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version

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
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.3-alt1.git20141105
- Initial build for Sisyphus

