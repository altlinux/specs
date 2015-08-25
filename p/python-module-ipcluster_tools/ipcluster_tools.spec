%define oname ipcluster_tools

%def_with python3

Name: python-module-%oname
Version: 0.0.11
Release: alt1.git20140803
Summary: IPython cluster tools
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ipcluster_tools
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nfaggian/ipcluster_tools.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests git ipython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests git ipython3
%endif

%py_provides %oname
%py_requires IPython

%description
A collection of tools to watch jobs on ipython clusters.

%if_with python3
%package -n python3-module-%oname
Summary: IPython cluster tools
Group: Development/Python3
%py3_provides %oname
%py3_requires IPython

%description -n python3-module-%oname
A collection of tools to watch jobs on ipython clusters.
%endif

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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.md notebooks
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md notebooks
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Aug 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.11-alt1.git20140803
- Initial build for Sisyphus

