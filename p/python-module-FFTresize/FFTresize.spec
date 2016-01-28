%define oname FFTresize

%def_with python3

Name: python-module-%oname
Version: 0.4.7
Release: alt1.git20141104.1
Summary: FFTresize resizes images using zero-padding in the frequency domain
License: ISC
Group: Development/Python
Url: https://pypi.python.org/pypi/FFTresize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://bitbucket.org/eliteraspberries/fftresize.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-numpy python-module-Pillow
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-numpy python3-module-Pillow
#BuildPreReq: python-tools-2to3
%endif

%py_provides fftresize

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-numpy python-module-pluggy python-module-py python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-numpy python3-module-pluggy python3-module-py python3-module-pycparser python3-module-setuptools xz
BuildRequires: python-module-Pillow python-module-numpy-testing python-module-pytest python3-module-Pillow python3-module-numpy-testing python3-module-pytest rpm-build-python3 time

%description
FFTresize resizes images using zero-padding in the frequency domain.

%package -n python3-module-%oname
Summary: FFTresize resizes images using zero-padding in the frequency domain
Group: Development/Python3
%py3_provides fftresize
%add_python3_req_skip cv2

%description -n python3-module-%oname
FFTresize resizes images using zero-padding in the frequency domain.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	2to3 -w -n $i
	mv $i $i.py3
done
popd
%endif

%python_install

%check
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
popd
%endif

%files
%doc LICENSE README*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.4.7-alt1.git20141104.1
- NMU: Use buildreq for BR.

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.7-alt1.git20141104
- Initial build for Sisyphus

