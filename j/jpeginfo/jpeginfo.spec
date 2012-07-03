Name: jpeginfo
Version: 1.6.1
Release: alt1

Summary: Utility to generate informative listings from jpeg files
License: GPLv2+
Group: Graphics

Url: http://www.kokkonen.net/tjko/projects.html
Source: http://www.kokkonen.net/tjko/src/jpeginfo-%version.tar.gz

# Automatically added by buildreq on Sat Mar 17 2012
BuildRequires: libjpeg-devel

%description
Utility to generate informative listings from jpeg files, and to check
jpeg files for errors.

%prep
%setup

%build
%configure
%make_build

%install
%make_install install INSTALL_ROOT=%buildroot

%files
%_bindir/*
%_man1dir/*

%changelog
* Sat Mar 17 2012 Victor Forsiuk <force@altlinux.org> 1.6.1-alt1
- Initial build.
