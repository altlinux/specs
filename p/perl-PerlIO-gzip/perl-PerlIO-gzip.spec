%define dist PerlIO-gzip
Name: perl-%dist
Version: 0.18
Release: alt2

Summary: A layer for the PerlIO system to transparently gzip/gunzip files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel zlib-devel

%description
PerlIO::gzip provides a PerlIO layer that manipulates files
in the format used by the C<gzip> program.  Compression and
decompression are implemented, but not together.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/PerlIO
%perl_vendor_autolib/PerlIO

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.18-alt2
- rebuilt for perl-5.14
- rebuilt as plain src.rpm

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.18-alt1.1
- rebuilt with perl 5.12

* Tue Dec 16 2008 Alexey Tourbin <at@altlinux.ru> 0.18-alt1
- 0.17 -> 0.18

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.17-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Aug 09 2004 Alexey Tourbin <at@altlinux.ru> 0.17-alt1
- 0.15 -> 0.17

* Mon Apr 19 2004 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- initial revision
