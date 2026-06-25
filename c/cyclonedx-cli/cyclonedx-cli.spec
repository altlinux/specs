%define _unpackaged_files_terminate_build 1
%define dotnetver 10.0

Name: cyclonedx-cli
Version: 0.32.0
Release: alt1

Summary: Tool for CycloneDX Software Bill of Materials (SBOM) analysis and modification.
Group: Development/Tools
License: Apache-2.0
URL: https://github.com/CycloneDX/cyclonedx-cli

ExclusiveArch: x86_64

# DOTNET_NUGET_SIGNATURE_VERIFICATION=false dotnet build --packages vendor
Source0: %name-%version.tar
Source1: vendor.tar
Source2: NuGet.Config

Requires: dotnet-%dotnetver

BuildRequires(pre): rpm-macros-dotnet

BuildRequires: /proc
BuildRequires: dotnet-sdk-%dotnetver
BuildRequires: patchelf

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
install -d %buildroot%_libdir/%name
cp -a src/cyclonedx/bin/Release/net%dotnetver/linux-x64/publish/. \
    %buildroot%_libdir/%name/

pushd %buildroot%_libdir/%name/
while read -r file; do
    if ! file "$file" | grep -q ' ELF '; then
        continue
    fi
    patchelf --set-rpath %_libdir/%name/ "$file"
done < <(find . -type f -name '*.so.*' -o -name '*.so')
popd

install -d %buildroot%_bindir
ln -srvf %_libdir/%name/cyclonedx %buildroot%_bindir/cyclonedx

%files
%doc README.md
%_bindir/cyclonedx
%_libdir/%name/

%changelog
* Thu Jun 25 2026 Alexander Kuznetsov <kuznetsovam@altlinux.org> 0.32.0-alt1
- Update to version 0.32.0.

* Thu May 14 2026 Alexander Kuznetsov <kuznetsovam@altlinux.org> 0.31.0-alt1
- Update to version 0.31.0.

* Sun Jan 25 2026 Alexander Kuznetsov <kuznetsovam@altlinux.org> 0.29.2-alt1
- Initial build.