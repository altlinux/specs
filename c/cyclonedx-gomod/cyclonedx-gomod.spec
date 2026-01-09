%define _unpackaged_files_terminate_build 1

Name: cyclonedx-gomod
Version: 1.9.0
Release: alt1

Summary: Tool to create CycloneDX Software Bill of Materials (SBOM) from Go modules.
Group: Development/Tools
License: Apache-2.0
URL: https://github.com/CycloneDX/cyclonedx-gomod

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang rpm-macros-golang

%description
cyclonedx-gomod creates CycloneDX Software Bill of Materials (SBOM) from Go modules.

%prep
%setup
%setup -a 1

%build
%make_build

%install
install -D -m755 bin/cyclonedx-gomod -t %buildroot%_bindir/

%files
%doc README.md
%_bindir/cyclonedx-gomod

%changelog
* Thu Jan 08 2026 Alexander Kuznetsov <kuznetsovam@altlinux.org> 1.9.0-alt1
- Initial build.
