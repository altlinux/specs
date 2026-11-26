%define dotnetver 10.0
%define dotnetenv \\\
	DOTNET_CLI_TELEMETRY_OPTOUT=1 \\\
	DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1 \\\
	DOTNET_NUGET_SIGNATURE_VERIFICATION=false \\\
	NUGET_PACKAGES=${PWD}/vendor

Name:    marksman
Version: 2026.02.08
Release: alt2
Summary: Write Markdown with code assist and intelligence in the comfort of your favourite editor

License: MIT
Group:   Development/Other
URL:     https://github.com/artempyanykh/marksman
VCS:     https://github.com/artempyanykh/marksman

Source0: %name-%version.tar
Source1: vendor.tar
Patch0: marksman-net10.patch

ExclusiveArch: %_dotnet_archlist

BuildRequires(pre): rpm-macros-dotnet
BuildRequires: /proc
BuildRequires: dotnet-sdk-%dotnetver

Requires: dotnet-%dotnetver

%description
Marksman is a program that integrates with your editor to assist you in writing
and maintaining your Markdown documents. Using LSP protocol it provides
completion, goto definition, find references, rename refactoring, diagnostics,
and more. In addition to regular Markdown, it also supports wiki-link-style
references that enable Zettelkasten-like note taking.

%prep
%setup -a1
%patch0 -p1
sed -i 's/9.0.100/10.0.100/' global.json
# Restore dependencies from the vendored NuGet packages only.
cat > NuGet.Config <<'EOF'
<?xml version="1.0" encoding="utf-8"?>
<configuration>
	<packageSources>
		<clear />
		<add key="vendor" value="vendor" />
	</packageSources>
</configuration>
EOF
# Replace git command with actual version
sed -i 's/git describe --tags --always --dirty/echo %version/' \
		Marksman/Marksman.fsproj

%build
export %dotnetenv

mkdir %_target_platform
dotnet publish \
	-c Release \
	--self-contained false \
	--use-current-runtime \
	-p:TargetFramework=net10.0 \
	-p:DebugType=embedded \
	-p:RestoreConfigFile=NuGet.Config \
	Marksman/Marksman.fsproj \
	-o %_target_platform

%install
mkdir -p %buildroot%_libdir/%name
cp -a %_target_platform/* %buildroot%_libdir/%name/
mkdir -p %buildroot%_bindir
ln -s ../%_lib/%name/marksman %buildroot%_bindir/marksman

%check
export %dotnetenv
dotnet test -p:TargetFramework=net10.0 -p:RestoreConfigFile=NuGet.Config

%files
%doc *.md
%_bindir/marksman
%_libdir/%name/*

%changelog
* Thu Nov 05 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.02.08-alt2
- Build with the system .NET 10 runtime (closes: #61281).
- Use dotnet-sdk-10.0 instead of dotnet-sdk-9.0 for framework builds.
- Use the vendored NuGet source for offline builds.

* Fri Aug 14 2026 Ilya Sorochan <k0tran@altlinux.org> 2026.02.08-alt1
- Initial build for ALT Linux.
