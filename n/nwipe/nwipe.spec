%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: nwipe
Version: 0.41
Release: alt1

Summary: Utility to securely erase disks
License: GPL-2.0-only
Group: File tools
Url: https://github.com/martijnvanbrummelen/nwipe

Source: %name-%version.tar

BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(libconfig)
BuildRequires: pkgconfig(libparted)
BuildRequires: gcc-c++

Requires: /bin/readlink
Requires: /usr/sbin/smartctl
Requires: /sbin/hdparm
Requires: /usr/sbin/dmidecode
Requires: /usr/sbin/modprobe

%description
Nwipe is a command that will securely erase disks using a variety of
recognised methods. It is a fork of the dwipe command used by Darik's
Boot and Nuke (DBAN).

%package doc
Summary: Utility to securely erase disks (documentation)
Group: Documentation
BuildArch: noarch

%description doc
Nwipe is a command that will securely erase disks using a variety of
recognised methods. It is a fork of the dwipe command used by Darik's
Boot and Nuke (DBAN).

This package includes documentation files for the %name.

%prep
%setup
sed -i "s|/images/|images/|" README.md

%build
export CFLAGS="$CFLAGS -Wno-unused-function"
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc CHANGELOG.md COPYING
%_bindir/*
%_man8dir/*

%files doc
%doc README.md ssd-guide.md images/

%changelog
* Sun May 17 2026 Nikolay Strelkov <snk@altlinux.org> 0.41-alt1
- New version 0.41.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.40-alt1
- New version 0.40.

* Fri Oct 17 2025 Nikolay Strelkov <snk@altlinux.org> 0.39-alt1
- Initial build for Sisyphus
