Name: exrtools
Version: 0.4
Release: alt1.1

Summary: Command line utilities for manipulating high dynamic range images
License: MIT/X Consortium
Group: Graphics

Url: http://scanline.ca/exrtools
Source: %url/exrtools-%version.tar.gz

# Automatically added by buildreq on Thu May 24 2007
BuildRequires: gcc-c++ libjpeg-devel libpng-devel openexr-devel

%description
exrtools is a set of simple command line utilities for manipulating high
dynamic range images in OpenEXR format. It was developed to help experiment
with batch processing of HDR images for tone mapping. Each application is
small and reasonably self-contained so that the source code may be of most
value to others.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc README ChangeLog
%_bindir/*
%_man1dir/*

%changelog
* Fri Feb 29 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.4-alt1.1
- Rebuilt due to libIlmImf.so.4 -> libIlmImf.so.6 soname change.

* Thu May 24 2007 Victor Forsyuk <force@altlinux.org> 0.4-alt1
- Initial build.
