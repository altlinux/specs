%define isl_ver 2

# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
#%%ifnarch ppc64le riscv64 s390x
#%%def_with doc
#%%else
%def_without doc
#%%endif
%def_with check

Name: isa-l
Version: 2.30.0
Release: alt1

Summary: Intelligent Storage Acceleration Library

License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/intel/isa-l

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-ec.patch
Patch1: %name-sve-ec.patch
Patch2: %name-s390x.patch
Patch3: %name-i386.patch

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

%build
%autoreconf
%configure --disable-static
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
* Wed Feb 08 2023 Leontiy Volodin <lvol@altlinux.org> 2.30.0-alt1
- Initial build for ALT Sisyphus (thanks alpinelinux for the spec).
- Needed for spdk.
