%define dist Mail-Box
Name: perl-%dist
Version: 2.101
Release: alt1

Summary: Manage a mailbox, a folder with messages
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MA/MARKOV/Mail-Box-2.101.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 23 2011 (-bi)
BuildRequires: perl-Email-Simple perl-File-FcntlLock perl-File-Remove perl-Font-AFM perl-HTML-Format perl-IO-stringy perl-MIME-Types perl-MIME-tools perl-Mail-IMAPClient perl-Mail-Transport-Dbx perl-Object-Realize-Later perl-Storable perl-Test-Pod perl-Text-Autoformat perl-User-Identity

%description
The Mail::Box folder is a modern mail-folder manager.  It is written
to be a replacement of MailTools and Mail::Folder, an alternative to
the Email::* set of modules.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
# only < 3 SpamAssassin is supported
rm %buildroot%perl_vendor_privlib/Mail/Message/Wrapper/SpamAssassin.{pm,pod}
rm %buildroot%perl_vendor_privlib/Mail/Box/Search/SpamAssassin.{pm,pod}

%files
%doc ChangeLog README README.FAQ
%perl_vendor_privlib/Mail/

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.101-alt1
- automated CPAN update

* Sun Jan 23 2011 Alexey Tourbin <at@altlinux.ru> 2.096-alt1
- 2.086 -> 2.096

* Thu Jan 08 2009 Vitaly Lipatov <lav@altlinux.ru> 2.086-alt1
- new version 2.086 (with rpmrb script)

* Fri Oct 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.084-alt1
- new version 2.084 (with rpmrb script)

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.063-alt2
- fix directory ownership violation

* Sat Feb 04 2006 Vitaly Lipatov <lav@altlinux.ru> 2.063-alt1
- initial build for ALT Linux Sisyphus
