%define _unpackaged_files_terminate_build 1
%define oname closure

%def_with python3

Name: python-module-%oname
Version: 20161201
Release: alt1.1
Summary: Closure compiler packaged for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/closure/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/miracle2k/python-closure.git
Source0: https://pypi.python.org/packages/0e/fb/877df05e79e4f719971e3cef9da6707b5f07ac29f223e80e6d5996c84b3b/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: closure-compiler jre /proc
#BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
Requires: closure-compiler jre /proc

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%description
The Closure Compiler is a tool for reducing the size of Javascript files
to make them download and run faster.

It's a Java-based tool. This package, in the spirit of the yuicompressor
package, provides a simple way to install and use the the Closure
compiler from Python, bundling the closure.jar with the Python package.

%package -n python3-module-%oname
Summary: Closure compiler packaged for Python
Group: Development/Python3
%py3_provides %oname
Requires: closure-compiler

%description -n python3-module-%oname
The Closure Compiler is a tool for reducing the size of Javascript files
to make them download and run faster.

It's a Java-based tool. This package, in the spirit of the yuicompressor
package, provides a simple way to install and use the the Closure
compiler from Python, bundling the closure.jar with the Python package.

%prep
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 20161201-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 20161201-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 20160517-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 20140110-alt1.git240319.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 20140110-alt1.git240319.1
- NMU: Use buildreq for BR.

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140110-alt1.git240319
- Initial build for Sisyphus

