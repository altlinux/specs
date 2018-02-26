%set_verify_elf_method unresolved=relaxed
#%add_optflags %optflags_shared
%def_disable static

Name: volpack
Version: 1.0c7
Release: alt1.1

Summary: Portable library for fast volume rendering
License: BSD
Group: System/Libraries
Url: http://amide.sourceforge.net
Packager: Andrey Yurkovsky <anyr@altlinux.org>

Source0: %name-%version.tgz

BuildRequires: m4

%description
VolPack is a portable library of fast volume rendering algorithms that
produce high-quality images.

%package devel
Summary: Shared libraries and header files for development using volpack
Group: Development/C
Requires: %name = %version-%release

%description devel
The volpack-devel package contains the header files and shared libraries
necessary for developing programs using the volpack volume rendering 
library.

%if_enabled static
%package devel-static
Summary: Static libraries and header files for development using volpack
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
The volpack-devel package contains the header files and static libraries
necessary for developing programs using the volpack volume rendering 
library.
%endif

%package doc
Summary: Documentation and examples for help using volpack
Group: Books/Other
Requires: volpack = %version-%release

%description doc
The volpack-doc package contains docs and examples helpful for developing
programs using the volpack volume rendering library.

%prep
%setup

%build
%configure %{subst_enable static}
%make_build

%install
%makeinstall
# remove doc and example files we don't want to package
rm -f doc/vp_userguide..pdf doc/Makefile*
pushd examples
make clean
rm -f Makefile.*
chmod 644 test.csh
popd

%files
%_libdir/*.so.*
%doc AUTHORS COPYING ChangeLog README
%_mandir/man3/*.3*

%files devel
%_libdir/*.so
%_includedir/*.h

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%files doc
%doc doc/ examples/

%changelog
* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0c7-alt1.1
- Rebuilt for soname set-versions

* Mon Feb 08 2010 Andrey Yurkovsky <anyr@altlinux.org> 1.0c7-alt1
- initial build

