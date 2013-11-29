%define oname llvm

%def_without python3
%def_with clang

Name: python-module-%oname
Version: 0.11.3
Release: alt1.git20131118
Summary: Python Bindings for LLVM
License: BSD
Group: Development/Python
Url: http://www.llvmpy.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: llvm-devel python-devel gcc-c++ libffi-devel
%if_with clang
BuildRequires: clang
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3 libnumpy-py3-devel
%endif

%description
llvm-py provides Python bindings for LLVM. It's goal is to expose enough
of LLVM APIs to implement a compiler backend or a VM in pure Python.
llvm-py consists of Python and C modules that wrap over the native C++/C
bindings of LLVM, and does not use / have dependencies on "glue
utilities" like Boost.Python, swig etc.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 Bindings for LLVM
Group: Development/Python3

%description -n python3-module-%oname
llvm-py provides Python bindings for LLVM. It's goal is to expose enough
of LLVM APIs to implement a compiler backend or a VM in pure Python.
llvm-py consists of Python and C modules that wrap over the native C++/C
bindings of LLVM, and does not use / have dependencies on "glue
utilities" like Boost.Python, swig etc.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

#sed -i 's|.*numpy\-py3.*||' llvm/_core.c

%build
%add_optflags -fno-strict-aliasing
%if_with clang
CC=clang; export CC;
CXX=clang++; export CXX;
%endif
%python_build_debug
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build_debug -fno-strict-aliasing
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

#check
#python -c 'import sys; sys.path.insert(0, "%buildroot%python_sitelibdir"); import llvm; llvm.test();'

%files
%doc CHANGELOG README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG README.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3-alt1.git20131118
- New snapshot

* Wed Aug 13 2013 Ivan Ovcherenko <asdus@altlinux.org> 0.11.3-alt1.git20130826
- Version 0.11.3
- Build with CLang 3.3 and over LLVM 3.3
- Removed -fno-rtti in compiler flags

* Tue Mar 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2.git20130302
- Added -fno-rtti in compiler flags

* Wed Mar 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.git20130302
- Version 0.11

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.svn20101105
- Initial build for Sisyphus

