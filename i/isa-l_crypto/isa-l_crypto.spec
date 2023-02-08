%define isl_ver 2

%def_without check

Name: isa-l_crypto
Version: 2.24.0
Release: alt1

Summary: Intelligent Storage Acceleration Library with crypto

License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/intel/isa-l_crypto

Source: %url/archive/%version/%name-%version.tar.gz
Patch: isa-l_crypto-2.24.0-upstream-build-shared-libs.patch

# x86 fails to compile
ExcludeArch: i586

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

%%description -n libisal_crypto-devel
The package provides development files for %name.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
  --disable-static \
#
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
* Wed Feb 08 2023 Leontiy Volodin <lvol@altlinux.org> 2.24.0-alt1
- Initial build for ALT Sisyphus (thanks alpinelinux for the spec).
- Needed for spdk.
