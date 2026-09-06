%define _unpackaged_files_terminate_build 1

%global import_path github.com/singularityos-lab/vetro

Name: vetro
Version: 1.0.0
Release: alt1

Summary: Vetro is a declarative GTK4 UI transpiler with a built-in Language Server Protocol (LSP) server
License: MIT
Group: Development/GNOME and GTK+
Url: https://github.com/singularityos-lab/vetro

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-build-golang

BuildRequires: golang

%description
%summary.

%prep
%setup -a1

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor

%install
install -Dpm755 %name %buildroot%_bindir/%name

%files
%doc LICENSE README.md
%_bindir/vetro

%changelog
* Sat Sep 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
