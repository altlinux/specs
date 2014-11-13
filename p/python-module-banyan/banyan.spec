%define oname banyan

%def_with python3
# very slow!
%def_disable check

Name: python-module-%oname
Version: 0.1.5.1
Release: alt1.git20141112
Summary: Backup of Banyan Python module
License: BSD
Group: Development/Python
Url: https://github.com/pyannote/pyannote-banyan
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pyannote/pyannote-banyan.git
Source: %name-%version.tar

BuildPreReq: gcc-c++
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-UnittestRandGenState
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-UnittestRandGenState
%endif

%py_provides %oname
%py_provides %{oname}_c

%description
Highly-optimized search trees (red-black, splay, and sorted-list) with
optional augmentation (dynamic order statistics, interval trees, etc.)

%package -n python3-module-%oname
Summary: Backup of Banyan Python module
Group: Development/Python3
%py3_provides %oname
%py3_provides %{oname}_c

%description -n python3-module-%oname
Highly-optimized search trees (red-black, splay, and sorted-list) with
optional augmentation (dynamic order statistics, interval trees, etc.)

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Highly-optimized search trees (red-black, splay, and sorted-list) with
optional augmentation (dynamic order statistics, interval trees, etc.)

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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
exit 1

%files
%doc *.txt
%python_sitelibdir/*

%files docs
%doc docs/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5.1-alt1.git20141112
- Initial build for Sisyphus

