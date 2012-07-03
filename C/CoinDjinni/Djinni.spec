%define oname djinni
Name: CoinDjinni
Version: 2.2.4
Release: alt1
Summary: A Templatized C++ Framework with Python Bindings for Heuristic Search
License: ISC License
Group: Sciences/Mathematics
Url: http://www.coin-or.org/projects/Djinni.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: boost-devel python-devel swig gcc-c++
BuildPreReq: doxygen graphviz

%description
Djinni is a framework for implementing heuristic search algorithms. The
core elements are coded in C++ and python bindings are provided to
simplify the user interface. The current version of Djinni implements
compressed annealing (Ohlmann et al., 2004), a generalization of the
well-known simulated annealing algorithm, and includes code used by
Ohlmann and Thomas (2007) to solve the traveling salesman problem with
time windows (TSPTW). The Djinni framework uses C++ templates to
separate code into three parts: a heuristic search algorithm, a problem
model, and problem data. Thus, it is straightforward to apply compressed
or simulated annealing to problems other than the TSPTW. Furthermore, it
is not difficult to apply different heuristic search algorithms to the
same problem.

%package devel
Summary: Development files for COIN-OR Djinni
Group: Development/C++
Requires: boost-devel
BuildArch: noarch

%description devel
Djinni is a framework for implementing heuristic search algorithms. The
core elements are coded in C++ and python bindings are provided to
simplify the user interface. The current version of Djinni implements
compressed annealing (Ohlmann et al., 2004), a generalization of the
well-known simulated annealing algorithm, and includes code used by
Ohlmann and Thomas (2007) to solve the traveling salesman problem with
time windows (TSPTW). The Djinni framework uses C++ templates to
separate code into three parts: a heuristic search algorithm, a problem
model, and problem data. Thus, it is straightforward to apply compressed
or simulated annealing to problems other than the TSPTW. Furthermore, it
is not difficult to apply different heuristic search algorithms to the
same problem.

This package contains development files for Djinni.

%package -n python-module-%oname
Summary: Python bindings of COIN-OR Djinni
Group: Development/Python

%description -n python-module-%oname
Djinni is a framework for implementing heuristic search algorithms. The
core elements are coded in C++ and python bindings are provided to
simplify the user interface. The current version of Djinni implements
compressed annealing (Ohlmann et al., 2004), a generalization of the
well-known simulated annealing algorithm, and includes code used by
Ohlmann and Thomas (2007) to solve the traveling salesman problem with
time windows (TSPTW). The Djinni framework uses C++ templates to
separate code into three parts: a heuristic search algorithm, a problem
model, and problem data. Thus, it is straightforward to apply compressed
or simulated annealing to problems other than the TSPTW. Furthermore, it
is not difficult to apply different heuristic search algorithms to the
same problem.

This package contains Python bindings of Djinni.

%package docs
Summary: Documentation and examples for COIN-OR Djinni
Group: Development/Documentation
BuildArch: noarch

%description docs
Djinni is a framework for implementing heuristic search algorithms. The
core elements are coded in C++ and python bindings are provided to
simplify the user interface. The current version of Djinni implements
compressed annealing (Ohlmann et al., 2004), a generalization of the
well-known simulated annealing algorithm, and includes code used by
Ohlmann and Thomas (2007) to solve the traveling salesman problem with
time windows (TSPTW). The Djinni framework uses C++ templates to
separate code into three parts: a heuristic search algorithm, a problem
model, and problem data. Thus, it is straightforward to apply compressed
or simulated annealing to problems other than the TSPTW. Furthermore, it
is not difficult to apply different heuristic search algorithms to the
same problem.

This package contains development documentation and examples for Djinni.

%prep
%setup

%build
%autoreconf
%configure \
	--with-boost
%make_build

pushd src
doxygen
popd

%install
%makeinstall_std

rm -f %buildroot%python_sitelibdir/%oname/*.la
rm -f %buildroot%python_sitelibdir/%oname/*.a

install -d %buildroot%_includedir/%oname
cp -fR src/TSPTW src/Twister src/annealer \
	%buildroot%_includedir/%oname/

%files devel
%doc AUTHORS ChangeLog LICENSE NEWS README
%_includedir/*

%files -n python-module-%oname
%python_sitelibdir/*

%files docs
%doc src/docs/html src/examples

%changelog
* Tue Feb 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.4-alt1
- Initial build for Sisyphus

