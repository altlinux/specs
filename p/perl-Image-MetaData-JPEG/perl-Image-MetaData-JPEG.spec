%define dist Image-MetaData-JPEG
Name: perl-%dist
Version: 0.153
Release: alt2

Summary: Perl extension for showing/modifying JPEG (meta)data
License: GPLv2
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: %name-fixpod.patch

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-Encode perl-Pod-Parser perl-devel

%description
This package provides an interface for reading and interpreting the content of
JPEG segments, in particular of those segments containing metadata (like TIFF
headers, thumbnails, Exif info, IPTC info, comments). Some segments can even be
modified and rewritten to disk.

%prep
%setup -n %dist-%version
%patch -p2

%build
%perl_vendor_build

%install
%perl_vendor_install

# XXX Global symbol "$UNDEF" requires explicit package name
%add_findreq_skiplist */Image/MetaData/JPEG/*/*.pl

%files
%doc Changes README
%perl_vendor_privlib/Image

%changelog
* Thu Jun 14 2012 Vladimir Lettiev <crux@altlinux.ru> 0.153-alt2
- Fixed pod lib/Image/MetaData/JPEG/Structures.pod

* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 0.153-alt1
- 0.15 -> 0.153

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Apr 07 2008 Victor Forsyuk <force@altlinux.org> 0.15-alt3
- Disable tests as they will fail with current perl.

* Fri Apr 13 2007 Victor Forsyuk <force@altlinux.org> 0.15-alt2
- Fix test suite to work with latest perl. Patch by Alexey Tourbin <at@altlinux>.

* Wed Dec 13 2006 Victor Forsyuk <force@altlinux.org> 0.15-alt1
- Initial build.
