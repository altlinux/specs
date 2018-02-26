%define dist podlators
Name: perl-%dist
Version: 2.4.0
Release: alt1

Summary: Convert POD data to various other formats
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Dec 23 2010 (-bi)
BuildRequires: perl-Pod-Parser perl-Term-ANSIColor perl-Term-Cap perl-Test-Pod

%description
This package contains the replacement for pod2text and Pod::Text in
versions of Perl 5.005 and earlier.  It also contains Pod::Man and
pod2man, the replacement for pod2man found in Perl distributions prior
to 5.6.0.  The modules contained in it use Pod::Simple rather than doing
the POD parsing themselves, and are designed to be object-oriented and
to subclass.

%prep
%setup -q -n %dist-%version

%build
export PERL5LIB=$PWD/blib/lib
%perl_vendor_build

%install
export PERL5LIB=$PWD/blib/lib
%perl_vendor_install

%files
%doc ChangeLog README
%_bindir/pod2man
%_bindir/pod2text
%perl_vendor_privlib/Pod*

%changelog
* Thu Dec 23 2010 Alexey Tourbin <at@altlinux.ru> 2.4.0-alt1
- 2.3.1 -> 2.4.0

* Mon Nov 15 2010 Vladimir Lettiev <crux@altlinux.ru> 2.3.1-alt2
- unbootsrap: added build dependency on perl-Pod-Parser

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 2.3.1-alt1
- initial revision, for perl-5.12
- disabled dependency on Pod::Usage, for bootstrap
