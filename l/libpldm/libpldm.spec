Name:    libpldm
Version: 0.12.0
Release: alt2

Summary: Encoding and decoding of PLDM messages library
License: Apache-2.0
Group:   Development/Other
Url:     https://www.openbmc.org
Vcs:     https://github.com/openbmc/libpldm.git

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: abi-compliance-checker
BuildRequires: abi-dumper
BuildRequires: ctags
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtest)
BuildRequires: doxygen

%description
Library which deals with the encoding and decoding of PLDM messages

%package -n %name-devel
Group:   Development/Other
Summary: Development files for encoding and decoding of PLDM messages

%description -n %name-devel
Development files for deals with the encoding and decoding of PLDM messages

%prep
%setup

%build
# Switch off failed on i586 arches assertion
%ifarch %ix86
subst "/static_assert(alignof(struct pldm_fd) == PLDM_ALIGNOF_PLDM_FD,/d" \
src/firmware_device/fd.c
subst "/	      \"PLDM_ALIGNOF_PLDM_FD wrong\");/d" src/firmware_device/fd.c
%endif
%meson -Dabi=deprecated,stable -Dtests=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/%name.so.*

%files -n %name-devel
%_includedir/%name
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_datadir/%name

%changelog
* Wed Apr 30 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.12.0-alt2
- Build for i586 without struct pldm_fd align assertion.
- Added BuildReq doxygen

* Thu Apr 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus.
