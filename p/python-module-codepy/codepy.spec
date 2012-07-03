%define oname codepy

%def_with python3

Name: python-module-%oname
Version: 2012.1.2
Release: alt1.git20120424
Summary: C metaprogramming toolkit for Python
License: MIT
Group: Development/Python
Url: http://documen.tician.de/codepy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://git.tiker.net/trees/codepy.git
Source: %oname-%version.tar

BuildPreReq: python-devel boost-python-devel
BuildPreReq: python-module-sphinx-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3
BuildPreReq: python3-module-distribute
%endif
BuildArch: noarch
%py_requires decorator

%description
CodePy is a C metaprogramming toolkit for Python. It handles two aspects
of metaprogramming:

* Generating C source code.

* Compiling this source code and dynamically loading it into the Python
interpreter.

Both capabilities are meant to be used together, but also work on their
own. In particular, the code generation facilities work well in
conjunction with PyCuda. Dynamic compilation and linking are so far only
supported in Linux with the GNU toolchain.

%if_with python3
%package -n python3-module-%oname
Summary: C metaprogramming toolkit for Python 3
Group: Development/Python3
%py3_requires decorator

%description -n python3-module-%oname
CodePy is a C metaprogramming toolkit for Python. It handles two aspects
of metaprogramming:

* Generating C source code.

* Compiling this source code and dynamically loading it into the Python
interpreter.

Both capabilities are meant to be used together, but also work on their
own. In particular, the code generation facilities work well in
conjunction with PyCuda. Dynamic compilation and linking are so far only
supported in Linux with the GNU toolchain.
%endif

%package pickles
Summary: Pickles for CodePy
Group: Development/Python

%description pickles
CodePy is a C metaprogramming toolkit for Python. It handles two aspects
of metaprogramming:

* Generating C source code.

* Compiling this source code and dynamically loading it into the Python
interpreter.

This package contains pickles for CodePy.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source

%build
%python_build_debug
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build_debug
popd
%endif

%make -C doc html
%make -C doc pickle

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_includedir/%oname %buildroot%_includedir/%oname-py3
%endif
%python_install

cp -fR doc/build/pickle \
	%buildroot%python_sitelibdir/%oname/

%files
%doc doc/build/html/*
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%_includedir/%oname

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%_includedir/%oname-py3
%endif

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1.2-alt1.git20120424
- Version 2012.1.2
- Added module for Python 3

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.1-alt1.git20111010
- Initial build for Sisyphus

