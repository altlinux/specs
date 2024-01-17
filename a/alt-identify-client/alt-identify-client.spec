%define _unpackaged_files_terminate_build 1

Name: alt-identify-client
Version: 1.0.0
Release: alt1

Summary: Client-side executable for ALT OS validation
Group: Other
License: Proprietary

Source: %name-%version.tar

BuildRequires: libssl-devel
BuildRequires: zlib-devel
BuildRequires: libbrotli-devel

ExclusiveArch: x86_64

%description
Client-side executable for ALT OS validation

%prep
%setup

%build

%install
mkdir -p %buildroot
cp -rp %_builddir/%name-%version/prefix/* %buildroot/

%files
%_bindir/perform_request_with_identification

%changelog
* Wed Oct 04 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.0-alt1
- Initial build for ALT

