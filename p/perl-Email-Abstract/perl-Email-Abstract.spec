%define dist Email-Abstract
Name: perl-%dist
Version: 3.004
Release: alt1

Summary: unified interface to mail representations
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-Email-MIME perl-MRO-Compat perl-Mail-Box perl-Module-Pluggable perl-devel

%description
"Email::Abstract" provides module writers with the ability to write
representation-independent mail handling code. For instance, in the
cases of "Mail::Thread" or "Mail::ListDetector", a key part of the
code involves reading the headers from a mail object. Where previously
one would either have to specify the mail class required, or to build a
new object from scratch, "Email::Abstract" can be used to perform
certain simple operations on an object regardless of its underlying
representation.

"Email::Abstract" currently supports "Mail::Internet",
"MIME::Entity", "Mail::Message", "Email::Simple" and "Email::MIME".
Other representations are encouraged to create their own
"Email::Abstract::*" class by copying "Email::Abstract::EmailSimple".
All modules installed under the "Email::Abstract" hierarchy will be
automatically picked up and used.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Email

%changelog
* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 3.004-alt1
- 2.134 -> 3.004

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 2.134-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Sep 17 2008 Vitaly Lipatov <lav@altlinux.ru> 2.134-alt1
- new version 2.134 (with rpmrb script)

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.131-alt2
- fix directory ownership violation

* Mon Dec 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.131-alt1
- first build for ALT Linux Sisyphus

