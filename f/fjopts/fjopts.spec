%global import_path go.aides.space/fjopts
%global _unpackaged_files_terminate_build 1

Name: fjopts
Version: 0.1.0
Release: alt1

Summary: fjopts is a application that allows users to enable or disable predefined options in Firejail profiles
License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: https://altlinux.space/aides-community/fjopts
Vcs: https://altlinux.space/aides-community/fjopts.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
%golang_build cmd/fjopts

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/%name

%changelog
* Wed Jan 07 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.1.0-alt1
- Initial build.
