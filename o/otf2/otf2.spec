%define _unpackaged_files_terminate_build 1

%def_with python3

%define sover 1

Name: otf2
License: BSD
Group: Development/Tools
Summary: Open Trace Format 2 (OTF2)
Version: 2.2
Release: alt1
Url: http://www.vi-hps.org/projects/score-p/

Source: %name-%version.tar
Patch1: %name-2.1-fedora-rpath.patch
Patch2: %name-2.1-alt-build.patch

BuildRequires: uncrustify doxygen graphviz texlive-base-bin
BuildRequires: gcc-c++

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(six)
%endif

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

%if_with python3
%package -n python3-module-%name
Summary: Python bindings for OTF2
Group: Development/Python3

%description -n python3-module-%name
The OTF2 library provides an interface to write and read trace data.

OTF2 is developed within the Score-P project. The Score-P project is
funded by the German Federal Ministry of Education and Research. OTF2 is
available under the BSD open source license that allows free usage for
academic and commercial applications.

This package contains python bindings for OTF2
%endif

%prep
%setup
%patch1 -p1
%patch2 -p2

%build
%autoreconf
%add_optflags %optflags_shared
%configure \
%if_with python3
	PYTHON=$(which python3) \
%else
	PYTHON=: \
%endif
	%nil
%make_build V=1

%install
%makeinstall_std

pushd %buildroot%_libdir
gcc -shared -Wl,--whole-archive lib%name.a -Wl,--no-whole-archive -lm \
	-Wl,-soname,lib%name.so.%sover -o lib%name.so.%sover
ln -s lib%name.so.%sover lib%name.so
popd

%if_with python3
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

find %buildroot%python3_sitelibdir -name '*.la' -delete
%endif

# remove unpackaged files
rm -f %buildroot%_libdir/*.a

%files
%doc AUTHORS ChangeLog COPYING README
%_bindir/*
%exclude %_bindir/%name-config
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/%name-config
%_includedir/*
%_libdir/*.so

%files docs
%_docdir/%name

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2-alt1
- Updated to upstream version 2.2.
- Built bindings for python-3.

* Thu Sep 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1-alt1
- Updated to upstream version 2.1.

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Thu Sep 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Moved %name-config into lib%name-devel

* Mon Sep 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

