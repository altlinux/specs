%define dist Encode-IMAPUTF7
Name: perl-%dist
Version: 1.05
Release: alt1

Summary: Modification of UTF-7 encoding for IMAP
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

Provides: perl-Encode-IMAPUtf7 = %version
Obsoletes: perl-Encode-IMAPUtf7 < %version

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-Encode perl-Test-NoWarnings

%description
IMAP mailbox names are encoded in a modified UTF7 when names contains
international characters outside of the printable ASCII range. The
modified UTF-7 encoding is defined in RFC2060 (section 5.1.3).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Encode

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt1
- 1.04 -> 1.05
- renamed to proper CPAN name: IMAPUtf7 -> IMAPUTF7

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri May 22 2009 Afanasov Dmitry <ender@altlinux.org> 1.04-alt1
- first build for ALT Linux Sisyphus
