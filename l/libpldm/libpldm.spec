Name:    libpldm
Version: 0.12.0
Release: alt1

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

ExcludeArch: %ix86

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
* Thu Apr 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus.
