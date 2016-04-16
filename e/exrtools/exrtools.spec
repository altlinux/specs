Name: exrtools
Version: 0.4
Release: alt1.qa3

Summary: Command line utilities for manipulating high dynamic range images
License: MIT/X Consortium
Group: Graphics

Url: http://scanline.ca/exrtools
Source: %url/exrtools-%version.tar.gz
Patch: exrtools-0.4-alt-libpng15.patch

# Automatically added by buildreq on Thu May 24 2007
BuildRequires: gcc-c++ libjpeg-devel libpng-devel openexr-devel

%description
exrtools is a set of simple command line utilities for manipulating high
dynamic range images in OpenEXR format. It was developed to help experiment
with batch processing of HDR images for tone mapping. Each application is
small and reasonably self-contained so that the source code may be of most
value to others.

%prep
%setup
%patch -p2

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README ChangeLog
%_bindir/*
%_man1dir/*

%changelog
* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4-alt1.qa3
- NMU: rebuilt due to libIlmImf.so.6 -> libIlmImf-2_2.so.22 soname change.

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.2
- Rebuilt with libpng15

* Fri Feb 29 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.4-alt1.1
- Rebuilt due to libIlmImf.so.4 -> libIlmImf.so.6 soname change.

* Thu May 24 2007 Victor Forsyuk <force@altlinux.org> 0.4-alt1
- Initial build.
