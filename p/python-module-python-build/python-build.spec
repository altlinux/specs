%define oname python-build

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20150708.1.1
Summary: Tool to download and build python based upon pyenv
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/python-build/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/crdoconnor/python-build.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides python_build

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
BuildPython is a python library to download and build a version of
python into a specified directory.

It can substitute for virtualenv.

%if_with python3
%package -n python3-module-%oname
Summary: Tool to download and build python based upon pyenv
Group: Development/Python3
%py3_provides python_build

%description -n python3-module-%oname
BuildPython is a python library to download and build a version of
python into a specified directory.

It can substitute for virtualenv.
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

%filter_from_requires /^python-base/d

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20150708.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1.git20150708.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150708
- Initial build for Sisyphus

