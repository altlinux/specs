%define _unpackaged_files_terminate_build 1
%define dotnetver 8.0

Name: cyclonedx-cli
Version: 0.29.2
Release: alt1

Summary: Tool for CycloneDX Software Bill of Materials (SBOM) analysis and modification.
Group: Development/Tools
License: Apache-2.0
URL: https://github.com/CycloneDX/cyclonedx-cli

ExclusiveArch: x86_64

Source0: %name-%version.tar
Source1: vendor.tar
Source2: NuGet.Config

BuildRequires(pre): rpm-macros-dotnet

BuildRequires: /proc
BuildRequires: dotnet-sdk-%dotnetver

%description
CycloneDX CLI tool for BOM analysis, modification, diffing, merging,
format conversion, signing and verification.

%prep
%setup -a1

%build
export DOTNET_CLI_TELEMETRY_OPTOUT="true"

dotnet restore \
    --configfile %SOURCE2 \
	--packages vendor \
	--ignore-failed-sources \
	--use-current-runtime

dotnet publish --packages vendor \
    --no-restore \
	--use-current-runtime \
	--no-self-contained

%install
install -D -m755 src/cyclonedx/bin/Release/net%dotnetver/linux-x64/publish/cyclonedx -t %buildroot%_bindir/

%files
%doc README.md
%_bindir/cyclonedx

%changelog
* Sun Jan 25 2026 Alexander Kuznetsov <kuznetsovam@altlinux.org> 0.29.2-alt1
- Initial build.