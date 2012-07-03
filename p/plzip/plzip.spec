Name: plzip
Version: 0.9
Release: alt1

Summary: Plzip is a parallel version of the lzip data compressor
License: GPLv3+
Group: Archiving/Compression

Url: http://www.nongnu.org/lzip/plzip.html
Source: http://download.savannah.gnu.org/releases-noredirect/lzip/plzip-%version.tar.gz

# Automatically added by buildreq on Wed Jan 27 2010
BuildRequires: gcc-c++ lzlib-devel

%description
Plzip is a parallel version of the lzip data compressor based on the LZMA
algorithm. The files produced by plzip are fully compatible with lzip-1.4 or
newer. Plzip is intended for faster compression/decompression of big files on
multiprocessor machines.

%prep
%setup

%build
%configure CXXFLAGS="%optflags %optflags_nocpp"
%make_build
make check

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%_infodir/*.info*

%changelog
* Sun Apr 15 2012 Victor Forsiuk <force@altlinux.org> 0.9-alt1
- 0.9

* Sun Jan 29 2012 Victor Forsiuk <force@altlinux.org> 0.8-alt1
- 0.8

* Mon Dec 06 2010 Victor Forsiuk <force@altlinux.org> 0.7-alt1
- 0.7

* Fri Jun 18 2010 Victor Forsiuk <force@altlinux.org> 0.6-alt2
- Rebuild with liblz.so.1.

* Mon Mar 22 2010 Victor Forsiuk <force@altlinux.org> 0.6-alt1
- 0.6

* Thu Feb 11 2010 Victor Forsiuk <force@altlinux.org> 0.5-alt1
- 0.5

* Mon Feb 01 2010 Victor Forsyuk <force@altlinux.org> 0.4-alt1
- 0.4

* Wed Jan 27 2010 Victor Forsyuk <force@altlinux.org> 0.3-alt1
- Initial build.
