Name: jpegoptim
Version: 1.2.4
Release: alt1

Summary: Utility to optimize jpeg files
License: GPLv2+
Group: Graphics

Url: http://www.kokkonen.net/tjko/projects.html
Source: http://www.kokkonen.net/tjko/src/jpegoptim-%version.tar.gz

# Automatically added by buildreq on Thu Oct 01 2009
BuildRequires: libjpeg-devel

%description
Utility to optimize jpeg files. Provides lossless optimization (based on
optimizing the Huffman tables) and "lossy" optimization based on setting
maximum quality factor.

%prep
%setup

%build
libtoolize -i
%configure
%make_build

%install
%make_install install INSTALL_ROOT=%buildroot

%files
%_bindir/*
%_man1dir/*

%changelog
* Mon Apr 11 2011 Victor Forsiuk <force@altlinux.org> 1.2.4-alt1
- 1.2.4

* Thu Oct 01 2009 Victor Forsyuk <force@altlinux.org> 1.2.3-alt1
- Initial build.
