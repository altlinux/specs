%global import_path github.com/Owloops/updo
Name:    updo
Version: 0.1.2
Release: alt1

Summary: Uptime monitoring CLI tool with alerting and advanced settings
License: MIT
Group:   Other
Url:     https://github.com/Owloops/updo

Packager: Aleksandr Shamaraev <shad@altlinux.org>

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md LICENSE
%_bindir/*

%changelog
* Mon Apr 21 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.2-alt1
- Initial build for ALT Linux.
