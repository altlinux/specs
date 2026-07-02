%define isl_ver 2

%def_without doc
%def_with check

Name: isa-l
Version: 2.32.1
Release: alt1

Summary: Intelligent Storage Acceleration Library

License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/intel/isa-l
VCS: https://github.com/intel/isa-l

# Source-url: https://github.com/intel/isa-l/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: help2man nasm
%if_with doc
BuildRequires: doxygen graphviz
%endif

%description
%summary.

%package -n libisal%isl_ver
Summary: %summary
Group: System/Libraries

%description -n libisal%isl_ver
%summary.

The package provides libraries for %name.

%package -n libisal-devel
Summary: Development package for %name
Group: Development/C

%description -n libisal-devel
%summary.

The package provides development files for %name.

%package tools
Summary: Tools for %name
Group: Development/Tools

%description tools
%summary.

The package provides tools for %name.

%prep
%setup
%autopatch -p1
%ifarch %e2k
# because MSCT enables SSE4.2 by default, but only provides slow SSE4.2 emulation
%add_optflags -mno-sse4.2
sed -i "s/__x86_64__/__e2k__/" igzip/huffman.h
%endif

%build
%autoreconf
%configure --disable-static --enable-programs=yes
%make
%if_with doc
%make doc
%endif

%install
%makeinstall_std

%if_with check
%check
%make test
%endif

%files -n libisal%isl_ver
%doc LICENSE README.md Release_notes.txt
%if_with doc
%doc isa-l_api_%version.pdf
%endif
%_libdir/libisal.so.%{isl_ver}*

%files -n libisal-devel
%_libdir/libisal.so
%_includedir/%name.h
%dir %_includedir/%name/
%_includedir/%name/*.h
%_pkgconfigdir/libisal.pc

%files tools
%_bindir/igzip
%_man1dir/igzip.1.xz

%changelog
* Thu Jul 02 2026 Leontiy Volodin <lvol@altlinux.org> 2.32.1-alt1
- New version 2.32.1.

* Fri Mar 06 2026 Leontiy Volodin <lvol@altlinux.org> 2.32.0-alt1
- New version 2.32.0.

* Wed Jun 11 2025 Leontiy Volodin <lvol@altlinux.org> 2.31.1-alt1
- New version 2.31.1.
- Added VCS tag.

* Tue Apr 16 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.31.0-alt1.1
- Fixed build for Elbrus.

* Tue Jan 23 2024 Leontiy Volodin <lvol@altlinux.org> 2.31.0-alt1
- New version 2.31.0.

* Wed Feb 08 2023 Leontiy Volodin <lvol@altlinux.org> 2.30.0-alt1
- Initial build for ALT Sisyphus (thanks alpinelinux for the spec).
- Needed for spdk.
