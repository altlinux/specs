%define oname uniseg

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.1
Summary: A pure Python library to determine Unicode text segmentations
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/uniseg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
# get by run 'make test'
Source1: data.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests sqlite3
#BuildPreReq: python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires sqlite3

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python-modules-sqlite3 python3-module-setuptools-tests rpm-build-python3 sqlite3

%description
This package provides:

* Functions to get Unicode Character Database (UCD) properties concerned
  with text segmentations.
* Functions to determin segmentation boundaries of Unicode strings.
* Classes that help implement Unicode-aware text wrapping on both
  console (monospace) and graphical (monospace / propotional) font
  environments.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A pure Python library to determine Unicode text segmentations.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A pure Python library to determine Unicode text segmentations
Group: Development/Python3
%py3_provides %oname
%py3_requires sqlite3

%description -n python3-module-%oname
This package provides:

* Functions to get Unicode Character Database (UCD) properties concerned
  with text segmentations.
* Functions to determin segmentation boundaries of Unicode strings.
* Classes that help implement Unicode-aware text wrapping on both
  console (monospace) and graphical (monospace / propotional) font
  environments.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A pure Python library to determine Unicode text segmentations.

This package contains tests for %oname.

%prep
%setup

tar -xf %SOURCE1

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
export LC_ALL=en_US.UTF-8
python setup.py test
%make test
%if_with python3
pushd ../python3
python3 setup.py test
#make test PYTHON=python3
popd
%endif

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*test*

%files tests
%python_sitelibdir/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*test*
%exclude %python3_sitelibdir/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*test*
%python3_sitelibdir/*/*/*test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

