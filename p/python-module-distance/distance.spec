%define oname distance

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20131122.1
Summary: Utilities for comparing sequences
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/Distance/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/doukremt/distance.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python3-devel rpm-build-python3

%description
This package provides helpers for computing similarities between
arbitrary sequences. Included metrics are Levenshtein, Hamming, Jaccard,
and Sorensen distance, plus some bonuses. All distance computations are
implemented in pure Python, and most of them are also implemented in C.

%package -n python3-module-%oname
Summary: Utilities for comparing sequences
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This package provides helpers for computing similarities between
arbitrary sequences. Included metrics are Levenshtein, Hamming, Jaccard,
and Sorensen distance, plus some bonuses. All distance computations are
implemented in pure Python, and most of them are also implemented in C.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug prepare --with-c
%python_build_debug --with-c

%if_with python3
pushd ../python3
%python3_build_debug prepare --with-c
%python3_build_debug --with-c
popd
%endif

%install
%python_install --with-c

%if_with python3
pushd ../python3
%python3_install --with-c
popd
%endif

%files
%doc *.md tests
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md tests
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1.git20131122.1
- NMU: Use buildreq for BR.

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20131122
- Initial build for Sisyphus

