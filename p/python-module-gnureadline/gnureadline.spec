%define oname gnureadline

%def_with python3

Name: python-module-%oname
Version: 6.3.3
Release: alt1.git20140408.1.1
Summary: Stand-alone GNU readline module
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/gnureadline
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ludwigschwardt/python-gnureadline.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools libreadline-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
The standard Python readline extension.

%package -n python3-module-%oname
Summary: Stand-alone GNU readline module
Group: Development/Python3

%description -n python3-module-%oname
The standard Python readline extension.

%prep
%setup

%ifarch x86_64
LIBSUFF=64
%endif
sed -i "s|@64@|$LIBSUFF|" setup.py

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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.3-alt1.git20140408.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 6.3.3-alt1.git20140408.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.3-alt1.git20140408
- Initial build for Sisyphus

