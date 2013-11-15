%define sover 0

Name: otf2
License: BSD
Group: Development/Tools
Summary: Open Trace Format 2 (OTF2)
Version: 1.2.1
Release: alt1
Url: http://www.vi-hps.org/projects/score-p/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.vi-hps.org/upload/packages/otf2/otf2-1.2.1.tar.gz

BuildPreReq: uncrustify doxygen graphviz texlive-base-bin
BuildPreReq: gcc-c++

Requires: lib%name = %EVR

%description
The OTF2 library provides an interface to write and read trace data.

OTF2 is developed within the Score-P project. The Score-P project is
funded by the German Federal Ministry of Education and Research. OTF2 is
available under the BSD open source license that allows free usage for
academic and commercial applications.

%package -n lib%name
Summary: Shared library of OTF2
Group: System/Libraries

%description -n lib%name
The OTF2 library provides an interface to write and read trace data.

OTF2 is developed within the Score-P project. The Score-P project is
funded by the German Federal Ministry of Education and Research. OTF2 is
available under the BSD open source license that allows free usage for
academic and commercial applications.

This package contains shared library of OTF2.

%package -n lib%name-devel
Summary: Development files of OTF2
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
The OTF2 library provides an interface to write and read trace data.

OTF2 is developed within the Score-P project. The Score-P project is
funded by the German Federal Ministry of Education and Research. OTF2 is
available under the BSD open source license that allows free usage for
academic and commercial applications.

This package contains development files of OTF2.

%package docs
Summary: Documentation for OTF2
Group: Documentation
BuildArch: noarch

%description docs
The OTF2 library provides an interface to write and read trace data.

OTF2 is developed within the Score-P project. The Score-P project is
funded by the German Federal Ministry of Education and Research. OTF2 is
available under the BSD open source license that allows free usage for
academic and commercial applications.

This package contains documentation for OTF2.

%prep
%setup

%build
#autoreconf
%add_optflags %optflags_shared
%configure
%make_build V=1

%install
%makeinstall_std

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

pushd %buildroot%_libdir
gcc -shared -Wl,--whole-archive lib%name.a -Wl,--no-whole-archive -lm \
	-Wl,-soname,lib%name.so.%sover -o lib%name.so.%sover
ln -s lib%name.so.%sover lib%name.so
popd

%files
%doc AUTHORS ChangeLog COPYING README
%_bindir/*
%exclude %_bindir/%name-config
%dir %_datadir/%name
%_datadir/%name/python

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/%name-config
%_includedir/*
%_libdir/*.so

%files docs
%_docdir/%name

%changelog
* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Thu Sep 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Moved %name-config into lib%name-devel

* Mon Sep 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

