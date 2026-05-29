%define _unpackaged_files_terminate_build 1

%global import_path github.com/xyproto/gendesk
Name: gendesk
Version: 1.0.14
Release: alt1

Summary: Generate desktop-files and download png-icons
License: BSD-3-Clause
Group: Graphical desktop/Other
Url: https://github.com/xyproto/gendesk

Source: %name-%version.tar
Source1: gendesk.png

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Generate desktop-files and download-png icons by specifying a minimum
of information.

%prep
%setup

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor

%install
install -Dpm755 %name %buildroot%_bindir/%name
install -Dpm644 %{name}.1 %buildroot/%_man1dir/%{name}.1
install -Dpm644 %SOURCE1 %buildroot/%_pixmapsdir/%{name}.png

%files
%doc LICENSE README.md
%_bindir/*
%_man1dir/*
%_pixmapsdir/*

%changelog
* Fri May 29 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.14-alt1
- New version 1.0.14.

* Thu May 21 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.13-alt1
- New version 1.0.13.

* Sun Jan 18 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.11-alt1
- New version 1.0.11.

* Sun Jun 29 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.10-alt1
- Initial build for Sisyphus
