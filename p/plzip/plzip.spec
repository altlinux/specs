%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: plzip
Version: 1.10
Release: alt1
Summary: Plzip is a parallel version of the lzip data compressor
License: GPLv3+
Group: Archiving/Compression
Url: https://www.nongnu.org/lzip/plzip.html

# https://download.savannah.gnu.org/releases/lzip/plzip/plzip-%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++ lzlib-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

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

%install
%makeinstall_std

%check
make check

%files
%_bindir/*
%_man1dir/*
%_infodir/*.info*

%changelog
* Mon Feb 28 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10-alt1
- Updated to upstream version 1.10.

* Fri Jul 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8-alt1
- Updated to upstream version 1.8.

* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6-alt1
- Updated to upstream version 1.6.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1.1
- NMU: added BR: texinfo

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
