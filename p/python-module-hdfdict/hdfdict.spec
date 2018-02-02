%define oname hdfdict

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.alpha.git20150227.1.1
Summary: Helps h5py to dump and load python dictionaries
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/hdfdict
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/SiggiGue/hdfdict.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-h5py python-module-numpy
BuildPreReq: python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-h5py python3-module-numpy
BuildPreReq: python3-module-Cython
%endif

%py_provides %oname
%py_requires h5py numpy

%description
If you have a hierarchical data structure of numpy arrays in a
dictionary for example, you can use this tool to save this dictionary
into a h5py File() or Group() and load it again. This tool just maps the
hdf Groups to dict keys and the Datset to dict values. Only types
supported by h5py can be used. The dicitonary-keys need to be strings
until now.

%if_with python3
%package -n python3-module-%oname
Summary: Helps h5py to dump and load python dictionaries
Group: Development/Python3
%py3_provides %oname
%py3_requires h5py numpy

%description -n python3-module-%oname
If you have a hierarchical data structure of numpy arrays in a
dictionary for example, you can use this tool to save this dictionary
into a h5py File() or Group() and load it again. This tool just maps the
hdf Groups to dict keys and the Datset to dict values. Only types
supported by h5py can be used. The dicitonary-keys need to be strings
until now.
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt1.alpha.git20150227.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.alpha.git20150227.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.alpha.git20150227
- Initial build for Sisyphus

