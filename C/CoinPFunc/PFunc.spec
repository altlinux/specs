%define somver 0
%define sover %somver.0.0

%define oname PFunc
Name: Coin%oname
Version: 1.0.2
Release: alt1.svn20110825
Summary: Generic task-parallel library for C/C++
License:  Eclipse Public License 1.0
Group: Sciences/Mathematics
Url: https://projects.coin-or.org/PFunc
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/PFunc/trunk
Source: %oname-%version.tar.gz
Source1: CMakeCache.txt

BuildPreReq: doxygen graphviz gcc-c++ cmake libcilk-devel
BuildPreReq: libtbb-devel flex libstdc++-devel
BuildPreReq: texlive-latex-recommended ghostscript-utils

Requires: lib%name = %version-%release

%description
PFunc, short for Parallel Functions, is a lightweight and portable
library that provides C and C++ APIs to express task parallelism. The
features offered by PFunc are a strict superset of the features offered
by current solutions for task parallelism such as Cilk and Intel's
Threading Building Blocks. Specifically, PFunc extends the feature set
of current solutions with custom task scheduling, task priorities and
task affinities. Furthermore, PFunc offers task groups for SPMD-style
programming and multiple task completion notifications for parallel
execution of DAGs. PFunc's extended feature set is geared towards
helping knowledgeable users optimize their application performance.

%package -n lib%name
Summary: Shared libraries of generic task-parallel library for C/C++
Group: System/Libraries

%description -n lib%name
PFunc, short for Parallel Functions, is a lightweight and portable
library that provides C and C++ APIs to express task parallelism. The
features offered by PFunc are a strict superset of the features offered
by current solutions for task parallelism such as Cilk and Intel's
Threading Building Blocks. Specifically, PFunc extends the feature set
of current solutions with custom task scheduling, task priorities and
task affinities. Furthermore, PFunc offers task groups for SPMD-style
programming and multiple task completion notifications for parallel
execution of DAGs. PFunc's extended feature set is geared towards
helping knowledgeable users optimize their application performance.

This package contains shared libraries of generic task-parallel library
for C/C++.

%package -n lib%name-devel
Summary: Development files of generic task-parallel library for C/C++
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
PFunc, short for Parallel Functions, is a lightweight and portable
library that provides C and C++ APIs to express task parallelism. The
features offered by PFunc are a strict superset of the features offered
by current solutions for task parallelism such as Cilk and Intel's
Threading Building Blocks. Specifically, PFunc extends the feature set
of current solutions with custom task scheduling, task priorities and
task affinities. Furthermore, PFunc offers task groups for SPMD-style
programming and multiple task completion notifications for parallel
execution of DAGs. PFunc's extended feature set is geared towards
helping knowledgeable users optimize their application performance.

This package contains development files of generic task-parallel library
for C/C++.

%package -n lib%name-devel-doc
Summary: Documentation for generic task-parallel library for C/C++
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
PFunc, short for Parallel Functions, is a lightweight and portable
library that provides C and C++ APIs to express task parallelism. The
features offered by PFunc are a strict superset of the features offered
by current solutions for task parallelism such as Cilk and Intel's
Threading Building Blocks. Specifically, PFunc extends the feature set
of current solutions with custom task scheduling, task priorities and
task affinities. Furthermore, PFunc offers task groups for SPMD-style
programming and multiple task completion notifications for parallel
execution of DAGs. PFunc's extended feature set is geared towards
helping knowledgeable users optimize their application performance.

This package contains development documentation for generic
task-parallel library for C/C++.

%package examples
Summary: Examples for generic task-parallel library for C/C++
Group: Development/Documentation
BuildArch: noarch

%description examples
PFunc, short for Parallel Functions, is a lightweight and portable
library that provides C and C++ APIs to express task parallelism. The
features offered by PFunc are a strict superset of the features offered
by current solutions for task parallelism such as Cilk and Intel's
Threading Building Blocks. Specifically, PFunc extends the feature set
of current solutions with custom task scheduling, task priorities and
task affinities. Furthermore, PFunc offers task groups for SPMD-style
programming and multiple task completion notifications for parallel
execution of DAGs. PFunc's extended feature set is geared towards
helping knowledgeable users optimize their application performance.

This package contains examples for generic task-parallel library for
C/C++.

%prep
%setup
install -p -m644 %SOURCE1 .

%build
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-D CMAKE_INSTALL_PREFIX:PATH=%prefix \
	.

%make_build all VERBOSE=1

%make doc

%install
%makeinstall_std

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

mkdir %buildroot%_libdir/tmp
pushd %buildroot%_libdir/tmp
for i in libpfunc; do
	ar x ../$i.a
	g++ -shared -Wl,-soname,$i.so.%somver * -o ../$i.so.%sover -lpthread
	ln -s $i.so.%sover ../$i.so.%somver
	ln -s $i.so.%somver ../$i.so
	rm -f *
done
popd
rmdir %buildroot%_libdir/tmp

%files -n lib%name
%doc AUTHORS ChangeLog LICENSE NEWS README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%doc doc/html
%doc tutorial/*.pdf

%files examples
%doc examples

%changelog
* Mon Oct 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.svn20110825
- Version 1.0.2

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20110419
- Version 1.0.0

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100826.3
- Added -g into compiler flags

* Fri Feb 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100826.2
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100826.1
- Rebuilt for soname set-versions

* Fri Sep 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100826
- Initial build for Sisyphus

