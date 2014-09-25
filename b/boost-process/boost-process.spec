Name: boost-process
Version: 0.5
Release: alt1
Summary: Library to manage system processes
License: Boost
Group: Development/C++
Url: http://www.highscore.de/boost/process0.5/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: gcc-c++ boost-devel doxygen graphviz boost-doc
#BuildPreReq: jam

%description
Boost.Process is a library to manage system processes. It can be used
to:

* create child processes
* setup streams for child processes
* communicate with child processes through streams (synchronously or
  asynchronously)
* wait for processes to exit (synchronously or asynchronously)
* terminate processes

%package devel
Summary: Library to manage system processes
Group: Development/C++
Requires: boost-devel

%description devel
Boost.Process is a library to manage system processes. It can be used
to:

* create child processes
* setup streams for child processes
* communicate with child processes through streams (synchronously or
  asynchronously)
* wait for processes to exit (synchronously or asynchronously)
* terminate processes

%package docs
Summary: Examples and documentation for %name
Group: Development/Documentation

%description docs
Boost.Process is a library to manage system processes. It can be used
to:

* create child processes
* setup streams for child processes
* communicate with child processes through streams (synchronously or
  asynchronously)
* wait for processes to exit (synchronously or asynchronously)
* terminate processes

This package contains examples and documentation for %name.

%prep
%setup

%build
#pushd libs/process/doc
#jam -f Jamfile.jam
#popd

%install
install -d %buildroot%_includedir
cp -fR boost %buildroot%_includedir/

%files devel
%_includedir/*

%files docs
%doc libs/process/example libs/process/doc libs/process/test

%changelog
* Thu Sep 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Initial build for Sisyphus

