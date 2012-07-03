%define dist Text-Bidi
Name: perl-%dist
Version: 0.03
Release: alt4

Summary: Unicode bidi algorithm for Perl using libfribidi
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-Text-Bidi-0.03-deb-fribidi_new.patch

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: libfribidi-devel perl-Test-Pod

%description
This is a perl interface to the libfribidi library that implements the
Unicode bidi algorithm.  The bidi algorithm is a specification for
displaying text that consists of both left-to-right and right-to-left
written languages.

%prep
%setup -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Text
%perl_vendor_autolib/Text

%changelog
* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt4
- rebuilt for perl-5.14

* Fri Jun 03 2011 Dmitry V. Levin <ldv@altlinux.org> 0.03-alt3
- Synced with libtext-bidi-perl-0.03-5 from Debian (fixes CPAN#42774).

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt2.1
- rebuilt with perl 5.12

* Mon Sep 08 2008 Anton Farygin <rider@altlinux.ru> 0.03-alt2
- fixed build

* Mon Apr 07 2008 Anton Farygin <rider@altlinux.ru> 0.03-alt1
- first build for Sisyphus
