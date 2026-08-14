%define dotnetver 9.0
%define dotnetenv \\\
	DOTNET_CLI_TELEMETRY_OPTOUT=1 \\\
	DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1 \\\
	DOTNET_NUGET_SIGNATURE_VERIFICATION=false \\\
	NUGET_PACKAGES=${PWD}/vendor

Name:    marksman
Version: 2026.02.08
Release: alt1
Summary: Write Markdown with code assist and intelligence in the comfort of your favourite editor

License: MIT
Group:   Development/Other
URL:     https://github.com/artempyanykh/marksman
VCS:     https://github.com/artempyanykh/marksman

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %_dotnet_archlist

BuildRequires(pre): rpm-macros-dotnet
BuildRequires: /proc
BuildRequires: dotnet-sdk-%dotnetver

%description
Marksman is a program that integrates with your editor to assist you in writing
and maintaining your Markdown documents. Using LSP protocol it provides
completion, goto definition, find references, rename refactoring, diagnostics,
and more. In addition to regular Markdown, it also supports wiki-link-style
references that enable Zettelkasten-like note taking.

%prep
%setup -a1
# Replace git command with actual version
sed -i 's/git describe --tags --always --dirty/echo %version/' \
		Marksman/Marksman.fsproj

%build
export %dotnetenv

mkdir %_target_platform
dotnet publish \
	-c Release \
	-p:PublishSingleFile=true \
	-p:PublishTrimmed=true \
	-p:TrimMode=partial \
	-p:DebugType=embedded \
	-p:EnableCompressionInSingleFile=true \
	-p:UseAppHost=true \
	Marksman/Marksman.fsproj \
	-o %_target_platform

%install
install -Dm755 -T %_target_platform/marksman %buildroot%_bindir/marksman

%check
export %dotnetenv
dotnet test

%files
%doc *.md
%_bindir/marksman

%changelog
* Fri Aug 14 2026 Ilya Sorochan <k0tran@altlinux.org> 2026.02.08-alt1
- Initial build for ALT Linux.
