Name: ann
Version: 1.1.2
Release: alt4
Summary: A Library for Approximate Nearest Neighbor Searching
License: LGPL v2.1 or later
Group: Sciences/Mathematics
Url: http://www.cs.umd.edu/~mount/ANN/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.cs.umd.edu/~mount/ANN/Files/1.1.2/ann_1.1.2.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: gcc-c++

%description
ANN is a library written in C++, which supports data structures and
algorithms for both exact and approximate nearest neighbor searching in
arbitrarily high dimensions.

In the nearest neighbor problem a set of data points in d-dimensional
space is given. These points are preprocessed into a data structure, so
that given any query point q, the nearest or generally k nearest points
of P to q can be reported efficiently. The distance between two points
can be defined in many ways. ANN assumes that distances are measured
using any class of distance functions called Minkowski metrics. These
include the well known Euclidean distance, Manhattan distance, and max
distance.

Based on our own experience, ANN performs quite efficiently for point
sets ranging in size from thousands to hundreds of thousands, and in
dimensions as high as 20. (For applications in significantly higher
dimensions, the results are rather spotty, but you might try it anyway.)

The library implements a number of different data structures, based on
kd-trees and box-decomposition trees, and employs a couple of different
search strategies.

The library also comes with test programs for measuring the quality of
performance of ANN on any particular data sets, as well as programs for
visualizing the structure of the geometric data structures.

%package test
Summary: Test for ANN
Group: Sciences/Mathematics
Requires: lib%name = %version-%release

%description test
ANN is a library written in C++, which supports data structures and
algorithms for both exact and approximate nearest neighbor searching in
arbitrarily high dimensions.

In the nearest neighbor problem a set of data points in d-dimensional
space is given. These points are preprocessed into a data structure, so
that given any query point q, the nearest or generally k nearest points
of P to q can be reported efficiently. The distance between two points
can be defined in many ways. ANN assumes that distances are measured
using any class of distance functions called Minkowski metrics. These
include the well known Euclidean distance, Manhattan distance, and max
distance.

Based on our own experience, ANN performs quite efficiently for point
sets ranging in size from thousands to hundreds of thousands, and in
dimensions as high as 20. (For applications in significantly higher
dimensions, the results are rather spotty, but you might try it anyway.)

The library implements a number of different data structures, based on
kd-trees and box-decomposition trees, and employs a couple of different
search strategies.

The library also comes with test programs for measuring the quality of
performance of ANN on any particular data sets, as well as programs for
visualizing the structure of the geometric data structures.

This package contains test for ANN.

%package example
Summary: Example for ANN
Group: Development/Documentation
Requires: lib%name = %version-%release

%description example
ANN is a library written in C++, which supports data structures and
algorithms for both exact and approximate nearest neighbor searching in
arbitrarily high dimensions.

In the nearest neighbor problem a set of data points in d-dimensional
space is given. These points are preprocessed into a data structure, so
that given any query point q, the nearest or generally k nearest points
of P to q can be reported efficiently. The distance between two points
can be defined in many ways. ANN assumes that distances are measured
using any class of distance functions called Minkowski metrics. These
include the well known Euclidean distance, Manhattan distance, and max
distance.

Based on our own experience, ANN performs quite efficiently for point
sets ranging in size from thousands to hundreds of thousands, and in
dimensions as high as 20. (For applications in significantly higher
dimensions, the results are rather spotty, but you might try it anyway.)

The library implements a number of different data structures, based on
kd-trees and box-decomposition trees, and employs a couple of different
search strategies.

The library also comes with test programs for measuring the quality of
performance of ANN on any particular data sets, as well as programs for
visualizing the structure of the geometric data structures.

This package contains example for ANN.

%package doc
Summary: Documentation for ANN
Group: Development/Documentation
BuildArch: noarch

%description doc
ANN is a library written in C++, which supports data structures and
algorithms for both exact and approximate nearest neighbor searching in
arbitrarily high dimensions.

In the nearest neighbor problem a set of data points in d-dimensional
space is given. These points are preprocessed into a data structure, so
that given any query point q, the nearest or generally k nearest points
of P to q can be reported efficiently. The distance between two points
can be defined in many ways. ANN assumes that distances are measured
using any class of distance functions called Minkowski metrics. These
include the well known Euclidean distance, Manhattan distance, and max
distance.

Based on our own experience, ANN performs quite efficiently for point
sets ranging in size from thousands to hundreds of thousands, and in
dimensions as high as 20. (For applications in significantly higher
dimensions, the results are rather spotty, but you might try it anyway.)

The library implements a number of different data structures, based on
kd-trees and box-decomposition trees, and employs a couple of different
search strategies.

The library also comes with test programs for measuring the quality of
performance of ANN on any particular data sets, as well as programs for
visualizing the structure of the geometric data structures.

This package contains documentation for ANN.

%package -n lib%name
Summary: Shared library of ANN
Group: System/Libraries

%description -n lib%name
ANN is a library written in C++, which supports data structures and
algorithms for both exact and approximate nearest neighbor searching in
arbitrarily high dimensions.

In the nearest neighbor problem a set of data points in d-dimensional
space is given. These points are preprocessed into a data structure, so
that given any query point q, the nearest or generally k nearest points
of P to q can be reported efficiently. The distance between two points
can be defined in many ways. ANN assumes that distances are measured
using any class of distance functions called Minkowski metrics. These
include the well known Euclidean distance, Manhattan distance, and max
distance.

Based on our own experience, ANN performs quite efficiently for point
sets ranging in size from thousands to hundreds of thousands, and in
dimensions as high as 20. (For applications in significantly higher
dimensions, the results are rather spotty, but you might try it anyway.)

The library implements a number of different data structures, based on
kd-trees and box-decomposition trees, and employs a couple of different
search strategies.

The library also comes with test programs for measuring the quality of
performance of ANN on any particular data sets, as well as programs for
visualizing the structure of the geometric data structures.

This package contains shared library of ANN.

%package -n lib%name-devel
Summary: Development files of ANN
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
ANN is a library written in C++, which supports data structures and
algorithms for both exact and approximate nearest neighbor searching in
arbitrarily high dimensions.

In the nearest neighbor problem a set of data points in d-dimensional
space is given. These points are preprocessed into a data structure, so
that given any query point q, the nearest or generally k nearest points
of P to q can be reported efficiently. The distance between two points
can be defined in many ways. ANN assumes that distances are measured
using any class of distance functions called Minkowski metrics. These
include the well known Euclidean distance, Manhattan distance, and max
distance.

Based on our own experience, ANN performs quite efficiently for point
sets ranging in size from thousands to hundreds of thousands, and in
dimensions as high as 20. (For applications in significantly higher
dimensions, the results are rather spotty, but you might try it anyway.)

The library implements a number of different data structures, based on
kd-trees and box-decomposition trees, and employs a couple of different
search strategies.

The library also comes with test programs for measuring the quality of
performance of ANN on any particular data sets, as well as programs for
visualizing the structure of the geometric data structures.

This package contains development files of ANN.

%package -n lib%name-devel-static
Summary: Static library of ANN
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
ANN is a library written in C++, which supports data structures and
algorithms for both exact and approximate nearest neighbor searching in
arbitrarily high dimensions.

In the nearest neighbor problem a set of data points in d-dimensional
space is given. These points are preprocessed into a data structure, so
that given any query point q, the nearest or generally k nearest points
of P to q can be reported efficiently. The distance between two points
can be defined in many ways. ANN assumes that distances are measured
using any class of distance functions called Minkowski metrics. These
include the well known Euclidean distance, Manhattan distance, and max
distance.

Based on our own experience, ANN performs quite efficiently for point
sets ranging in size from thousands to hundreds of thousands, and in
dimensions as high as 20. (For applications in significantly higher
dimensions, the results are rather spotty, but you might try it anyway.)

The library implements a number of different data structures, based on
kd-trees and box-decomposition trees, and employs a couple of different
search strategies.

The library also comes with test programs for measuring the quality of
performance of ANN on any particular data sets, as well as programs for
visualizing the structure of the geometric data structures.

This package contains static library of ANN.

%prep
%setup
mkdir -p lib bin

%build
%make_build linux-g++

%install
rm -f $(find ./ -name '*.o')

install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/ANN
install -d %buildroot%_datadir/%name/test
install -d %buildroot%_datadir/%name/example
install -d %buildroot%_docdir/%name

install -m755 bin/* %buildroot%_bindir
cp -P lib/* %buildroot%_libdir
chmod -x %buildroot%_libdir/*
install -p -m644 include/ANN/* %buildroot%_includedir/ANN
install -p -m644 test/*.pts test/*.in test/*.save %buildroot%_datadir/%name/test
install -p -m644 sample/* %buildroot%_datadir/%name/example
install -p -m644 doc/* %buildroot%_docdir/%name

%files
%doc Copyright.txt License.txt ReadMe.txt
%_bindir/ann2fig

%files test
%_bindir/ann_test
%dir %_datadir/%name
%_datadir/%name/test

%files example
%_bindir/ann_sample
%dir %_datadir/%name
%_datadir/%name/example

%files doc
%_docdir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt4
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt3
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Rebuilt for soname set-versions

* Fri Jun 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Fri Sep 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

