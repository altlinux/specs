Name: perceptualdiff
Version: 1.1.1
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: An image comparison utility
License: GPLv2+
Group: Graphics

URL: http://pdiff.sourceforge.net/
Source: http://downloads.sourceforge.net/pdiff/perceptualdiff-%version-src.tar.gz
Patch1: PerceptualDiff-1.1.1-stdio.patch

# Automatically added by buildreq on Thu Jul 03 2008
BuildRequires: cmake gcc-c++ libfreeimage-devel

%description
perceptualdiff is an image comparison utility that makes use of a
computational model of the human visual system to compare two images.

%prep
%setup -c -n PerceptualDiff-%version
%patch1 -p1

%build
export CC=gcc
cmake -DCMAKE_INSTALL_PREFIX:PATH=%_prefix .
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*

%changelog
* Mon Jun 22 2009 Victor Forsyuk <force@altlinux.org> 1.1.1-alt1
- 1.1.1

* Wed Oct 29 2008 Victor Forsyuk <force@altlinux.org> 1.0.2-alt2
- Fix FTBFS with gcc4.3.

* Thu Jul 03 2008 Victor Forsyuk <force@altlinux.org> 1.0.2-alt1
- 1.0.2

* Fri Jun 08 2007 Victor Forsyuk <force@altlinux.org> 1.0.1-alt1
- Initial build.
