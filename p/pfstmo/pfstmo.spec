Name: pfstmo
Version: 1.4
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Tone mapping operators for High Dynamic Range (HDR) images
License: GPLv2+
Group: Graphics

Url: http://www.mpi-inf.mpg.de/resources/tmo/
Source: http://downloads.sourceforge.net/pfstools/pfstmo-%version.tar.gz
Patch1: pfstmo-1.4-missinginclude.patch

# Automatically added by buildreq on Thu Nov 26 2009
BuildRequires: gcc-c++ libfftw3-devel libgomp-devel libgsl-devel libpfs-devel

%description
pfstmo package contains the implementation of state-of-the-art tone mapping
operators. The motivation here is to provide an implementation of tone mapping
operators suitable for convenient processing of both static images and
animations.

%prep
%setup
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Thu Nov 26 2009 Victor Forsyuk <force@altlinux.org> 1.4-alt1
- 1.4

* Thu Sep 11 2008 Victor Forsyuk <force@altlinux.org> 1.3.2-alt1
- 1.3.2

* Wed Aug 27 2008 Victor Forsyuk <force@altlinux.org> 1.3.1-alt1
- 1.3.1
- Build with OpenMP support!

* Tue Jun 17 2008 Victor Forsyuk <force@altlinux.org> 1.3-alt1
- 1.3

* Tue Feb 26 2008 Victor Forsyuk <force@altlinux.org> 1.2-alt1
- 1.2

* Mon Jul 23 2007 Victor Forsyuk <force@altlinux.org> 1.1-alt1
- 1.1

* Fri Jun 08 2007 Victor Forsyuk <force@altlinux.org> 1.0-alt1
- Initial build.
