%define _unpackaged_files_terminate_build 1

Name: alt-identify-client
Version: 1.0.6
Release: alt1

Summary: Client-side executable for ALT OS validation
Group: Other
License: Proprietary

Source: %name-%version.tar

BuildRequires: libssl-devel
BuildRequires: zlib-devel
BuildRequires: libbrotli-devel

ExclusiveArch: x86_64 aarch64

%description
Client-side executable for ALT OS validation

%prep
%setup

%build

%install
mkdir -p %buildroot
cp -rp %_builddir/%name-%version/%_arch/prefix/* %buildroot/

%files
%doc LICENSE
%_bindir/perform_request_with_identification

%changelog
* Tue Sep 24 2024 Oleg Solovyov <mcpain@altlinux.org> 1.0.6-alt1
- Update to new version

* Wed Apr 03 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.5-alt1
- Update to new version

* Wed Mar 27 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.4-alt1
- Update to new version

* Thu Mar 07 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.1-alt2
- Add license (closes: #49525)

* Thu Jan 18 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.1-alt1
- Update to new version
- Build for aarch64

* Wed Oct 04 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.0-alt1
- Initial build for ALT

