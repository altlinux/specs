Name: mili
Version: 18
Release: alt1.hg20140430
Summary: Minimalistic headers-only C++ Library
License: Boost Software License v1.0
Group: Development/C++
Url: http://code.google.com/p/mili/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# hg clone https://code.google.com/p/mili/
Source: %name-%version.tar.gz

%description
MiLi is a collection of useful C++ libraries, composed only by headers.

%package devel
Summary: Headers of Minimalistic headers-only C++ Library
Group: Development/C++
BuildArch: noarch

%description devel
MiLi is a collection of useful C++ libraries, composed only by headers.

This package contains headers of MiLi.

%package examples
Summary: Examples for Minimalistic headers-only C++ Library
Group: Development/Documentation
BuildArch: noarch

%description examples
MiLi is a collection of useful C++ libraries, composed only by headers.

This package contains examples for MiLi.

%prep
%setup

%install
install -d %buildroot%_includedir/%name
install -p -m644 %name/* %buildroot%_includedir/%name

%files devel
%doc CHANGELOG CONTRIBUTORS README LICENSE_1_0.txt
%_includedir/*

%files examples
%doc examples/*

%changelog
* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 18-alt1.hg20140430
- Version 18

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 17-alt1.svn20120420
- New snapshot

* Tue Feb 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 17-alt1.svn20120221
- New snapshot

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 17-alt1.svn20111203
- New snapshot

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 17-alt1.svn20110428
- New snapshot

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 17-alt1.svn20101117
- Version 17

* Tue Sep 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 16-alt1.svn20100925
- Initial build for Sisyphus

