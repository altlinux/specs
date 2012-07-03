%define module Unicode-IMAPUtf7
%define m_distro Unicode-IMAPUtf7
%define m_name Unicode::IMAPUtf7
%define m_author_id unknown
%define _enable_test 1

Name: perl-%module
Version: 2.01
Release: alt1.1

Summary: Perl extension to deal with IMAP UTF7

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Afanasov Dmitry <ender@altlinux.org>

BuildArch: noarch
Source: %m_distro-%version.tar

BuildRequires: perl-devel perl(Unicode/String.pm)

%description
IMAP mailbox names are encoded in a modified UTF7 when names contains
international characters outside of the printable ASCII range. The modified
UTF-7 encoding is defined in RFC2060 (section 5.1.3).

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed May 20 2009 Afanasov Dmitry <ender@altlinux.org> 2.01-alt1
- first build for ALT Linux Sisyphus

