%define isl_ver 2

%def_without check

Name: isa-l_crypto
Version: 2.26.1
Release: alt1

Summary: Intelligent Storage Acceleration Library with crypto

License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/intel/isa-l_crypto
VCS: https://github.com/intel/isa-l_crypto

# Source-url: https://github.com/intel/isa-l_crypto/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

# x86 and ppc64 fail to compile
ExcludeArch: i586 ppc64le

BuildRequires: gcc openssl-devel nasm

%description
%summary.

%package -n libisal_crypto%isl_ver
Summary: %summary
Group: System/Libraries

%description -n libisal_crypto%isl_ver
%summary.

%package -n libisal_crypto-devel
Summary: Development package for %name
Group: Development/C

%description -n libisal_crypto-devel
The package provides development files for %name.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-static
%make

%install
%makeinstall_std

# other arches fail tests
%if_with check
%check
%make test
%endif

%files -n libisal_crypto%isl_ver
%doc LICENSE README.md
%_libdir/libisal_crypto.so.%{isl_ver}*

%files -n libisal_crypto-devel
%_includedir/%name.h
%dir %_includedir/%name/
%_includedir/%name/*.h
%_pkgconfigdir/libisal_crypto.pc
%_libdir/libisal_crypto.so

%changelog
* Mon Jun 15 2026 Leontiy Volodin <lvol@altlinux.org> 2.26.1-alt1
- New version 2.26.1.

* Tue Feb 03 2026 Leontiy Volodin <lvol@altlinux.org> 2.26-alt1
- New version 2.26.

* Fri Jul 05 2024 Leontiy Volodin <lvol@altlinux.org> 2.25.0-alt1
- New version 2.25.0.
- Excluded build on ppc64le.

* Wed Feb 08 2023 Leontiy Volodin <lvol@altlinux.org> 2.24.0-alt1.1
- Cleanup spec.

* Wed Feb 08 2023 Leontiy Volodin <lvol@altlinux.org> 2.24.0-alt1
- Initial build for ALT Sisyphus (thanks alpinelinux for the spec).
- Needed for spdk.
