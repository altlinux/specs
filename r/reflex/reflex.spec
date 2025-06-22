%define _unpackaged_files_terminate_build 1

%global import_path github.com/cespare/reflex
Name: reflex
Version: 0.3.1
Release: alt1

Summary: Run a command when files change
License: MIT
Group: Other
Url: https://github.com/cespare/reflex

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: %{name}.1

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Reflex is a small tool to watch a directory and rerun a command
when certain files change. It's great for automatically running
compile/lint/test tasks and for reloading your application when the
code changes.

%prep
%setup -a1
%patch -p1

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor

%install
install -Dpm755 %name %buildroot%_bindir/%name
# install man-page
install -pDm 644 %SOURCE2 %buildroot%_man1dir/%name.1

%files
%doc CONTRIBUTING.md LICENSE README.md
%_bindir/*
%_man1dir/%name.1*

%changelog
* Sun Jun 22 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus
