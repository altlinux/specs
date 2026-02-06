%define _unpackaged_files_terminate_build 1
%def_with check

Name: cyclonedx-gomod
Version: 1.10.0
Release: alt1

Summary: Tool to create CycloneDX Software Bill of Materials (SBOM) from Go modules.
Group: Development/Tools
License: Apache-2.0
URL: https://github.com/CycloneDX/cyclonedx-gomod

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

Requires:  golang

BuildRequires(pre): rpm-build-golang rpm-macros-golang

%description
cyclonedx-gomod creates CycloneDX Software Bill of Materials (SBOM) from Go modules.

%prep
%setup
%setup -a 1

%build
%make_build

%check
# only run specific tests that do not require internet connection
go test -v -short -cover ./internal/cli/cmd/app ./internal/cli/cmd/bin \
    ./internal/cli/cmd/mod ./internal/cli/options ./internal/sbom/convert/file \
    ./internal/sbom/convert/pkg ./internal/util ./pkg/generate/...

%install
install -D -m755 bin/cyclonedx-gomod -t %buildroot%_bindir/

%files
%doc README.md
%_bindir/cyclonedx-gomod

%changelog
* Fri Feb 06 2026 Alexander Kuznetsov <kuznetsovam@altlinux.org> 1.10.0-alt1
- Update to version 1.10.0.
- Add golang BR.
- Enable tests.

* Thu Jan 08 2026 Alexander Kuznetsov <kuznetsovam@altlinux.org> 1.9.0-alt1
- Initial build.
