%def_disable static

Name: libvigra
Version: 1.6.0
Release: alt2.2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Generic Programming for Computer Vision
License: MIT
Group: System/Libraries

Url: http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra
Source: %url/vigra%version.tar.gz
Patch: libvigra-1.6.0-alt-libpng15.patch

# Automatically added by buildreq on Wed Jun 13 2007
BuildRequires: gcc-c++ libfftw3-devel libjpeg-devel libpng-devel libtiff-devel

Provides: vigra
Obsoletes: vigra

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel
computer vision library that puts its main emphasize on customizable
algorithms and data structures.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name = %version-%release
Provides: vigra-devel
Obsoletes: vigra-devel

%description devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%package devel-doc
Summary: Development documentation for vigra library
Group: Development/C
Requires: %name-devel = %version-%release
Provides: vigra-devel-doc
Obsoletes: vigra-devel-doc
BuildArch: noarch

%description devel-doc
Development documentation for vigra library.

%prep
%setup -n vigra%version
%patch -p2

%__subst 's/^CXXFLAGS=.*$//; s/^CFLAGS=.*$//' configure

%build
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
%add_optflags %optflags_shared -fpermissive
export CXXFLAGS="%optflags"
export CFLAGS="%optflags"
./configure --prefix=%_prefix --libdir=%_libdir %{subst_enable static} \
	--with-fftw --with-jpeg --with-png --with-tiff
%make_build

%install
%make_install prefix=%buildroot/usr libdir=%buildroot%_libdir docdir=`pwd`/docs install

%files
%_libdir/*.so.*

%files devel
%_bindir/*
%_includedir/vigra
%_libdir/*.so

%files devel-doc
%doc docs/[!L]*

%changelog
* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt2.2
- Rebuilt with libpng15

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2.1
- rebuild for set:provides by request of mithraen

* Fri Jan 09 2009 Victor Forsyuk <force@altlinux.org> 1.6.0-alt2
- Remove obsolete ldconfig calls.

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 1.6.0-alt1
- 1.6.0

* Tue Jul 10 2007 Victor Forsyuk <force@altlinux.org> 1.5.0-alt2
- Fix 64 bit build.

* Mon Jul 09 2007 Victor Forsyuk <force@altlinux.org> 1.5.0-alt1
- Initial build.
