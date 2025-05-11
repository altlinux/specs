%global import_path github.com/nwg-piotr/gopsuinfo

%define _unpackaged_files_terminate_build 1

Name: gopsuinfo
Version: 0.1.9
Release: alt1

Summary: A gopsutil-based command to display customizable system info
License: BSD-2-Clause
Group: Graphical desktop/Other
Url: https://github.com/nwg-piotr/gopsuinfo

Source: %name-%version.tar
Source1: %name-development-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
A gopsutil-based command to display system usage info as text in panels
like Waybar or icon/text in tint2 and nwg-panel executors.

%prep
%setup -a1
%patch -p1

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor

%install
install -Dpm755 %name %buildroot%_bindir/%name
make install DESTDIR=%buildroot

%files
%doc LICENSE README.md
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.9-alt1
- Initial build for Sisyphus
