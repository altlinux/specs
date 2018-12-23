%def_disable snapshot
%define _name graphite2
%def_disable docs
%def_enable check

Name: lib%_name
Version: 1.3.13
Release: alt1

Summary: Font rendering capabilities for complex non-Roman writing systems
Group: System/Libraries
License: LGPLv2.1+ or MPL
Url: http://sourceforge.net/projects/silgraphite/

%if_disabled snapshot
Source: http://downloads.sourceforge.net/silgraphite/%_name-%version.tgz
%else
# VCS: https://github.com/silnrsi/graphite.git
Source: %_name-%version.tar
%endif

Obsoletes: %_name
Provides: %_name = %version-%release

# fc patch
Patch1: graphite2-1.2.0-cmakepath.patch

BuildRequires: gcc-c++ cmake ctest libfreetype-devel
%{?_enable_docs:BuildRequires: doxygen asciidoc-a2x dblatex %_bindir/pdflatex}
%{?_enable_check:BuildRequires: python3-module-fonttools}

%description
Graphite2 is a project within SIL's Non-Roman Script Initiative and
Language Software Development groups to provide rendering capabilities
for complex non-Roman writing systems. Graphite can be used to create
"smart fonts" capable of displaying writing systems with various
complex behaviors. With respect to the Text Encoding Model, Graphite
handles the "Rendering" aspect of writing system implementation.

%package devel
Summary: Files for developing with Graphite2
Group: Development/C++
Provides: %_name-devel = %version-%release
Requires: %name = %version-%release

%description devel
Includes and definitions for developing with Graphite2.

%prep
%setup -n %_name-%version
%patch1 -p1 -b .cmake

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%ifarch %e2k
# Some plugins use C++ and need lcxa. It can't be loaded
# dynamically, so all binaries should be linked with it.
cc --version | grep -q '^lcc:1.21' && export LIBS='-lcxa'
%endif
%cmake -DGRAPHITE2_COMPARE_RENDERER=OFF \
	-DCMAKE_SHARED_LINKER_FLAGS=$LIBS \
	-DPYTHON_EXECUTABLE:FILEPATH=%_bindir/python3
%cmake_build

%if_enabled docs
%make docs -C BUILD
sed -i -e 's!<a id="id[a-z]*[0-9]*"></a>!!g' BUILD/doc/manual.html
%endif

%install
%cmakeinstall_std

%check
LD_LIBRARY_PATH=%buildroot%_libdir %make test -C BUILD

%files
%_libdir/%name.so.*
%doc COPYING ChangeLog

%files devel
%_bindir/gr2fonttest
%_includedir/%_name/
%_libdir/%name.so
%dir %_libdir/%_name/
%_libdir/%_name/%_name-release.cmake
%_libdir/%_name/%_name.cmake
%_libdir/pkgconfig/%_name.pc
%{?_enable_docs:%doc BUILD/doc/manual.html}

%changelog
* Sun Dec 23 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.13-alt1
- 1.3.13

* Wed Oct 31 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.12-alt2.1
- e2k fixes, see previous release

* Wed Oct 31 2018 Michael Shigorin <mike@altlinux.org> 1.3.12-alt2
- E2K: adjust for lcc >= 1.21.24 (and prepare for 1.23)

* Thu Aug 16 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.12-alt1
- 1.3.12

* Sun May 13 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.11-alt1
- 1.3.11

* Sun Aug 27 2017 Michael Shigorin <mike@altlinux.org> 1.3.10-alt2
- E2K: avoid lcc-unsupported option; explicit -lcxa

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.10-alt1
- 1.3.10

* Mon Dec 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.9-alt1
- 1.3.9

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.8-alt1
- 1.3.8

* Tue Feb 16 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.5-alt1
- 1.3.5

* Tue Feb 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Sat Nov 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1.1
- obsoletes/provides graphite2 package

* Tue Nov 19 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- first build for Sisyphus

