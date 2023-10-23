%define _unpackaged_files_terminate_build 1
%define dist Mail-Box
# true for 3.010
# ERROR: spam-assassin version 4.000000 is not supported (only versions 2.x)
%def_disable spamassasin

Name: perl-%dist
Version: 3.010
Release: alt2

Summary: Manage a mailbox, a folder with messages
License: Artistic-2.0
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MA/MARKOV/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 23 2011 (-bi)
BuildRequires: perl-Email-Simple perl-File-FcntlLock perl-File-Remove perl-Font-AFM perl-IO-stringy perl-MIME-Types perl-MIME-tools perl-Mail-IMAPClient perl-Mail-Transport-Dbx perl-Object-Realize-Later perl-Storable perl-Test-Pod perl-Text-Autoformat perl-User-Identity perl(Devel/GlobalDestruction.pm) perl(HTML/TreeBuilder.pm) perl(Mail/Box/Parser/Perl.pm) perl(Mail/Message/Head/Complete.pm)
%if_enabled spamassasin
BuildRequires: perl-Mail-SpamAssassin
%endif

%description
The Mail::Box folder is a modern mail-folder manager.  It is written
to be a replacement of MailTools and Mail::Folder, an alternative to
the Email::* set of modules.

%package -n perl-Mail-Box-SpamAssassin
Summary: SpamAssassin support for Mail::Box
Group: Development/Perl
Requires: perl-Mail-Box = %EVR

%description -n perl-Mail-Box-SpamAssassin
SpamAssassin support for Mail::Box

%prep
%setup -q -n %{dist}-%{version}

# https://rt.cpan.org/Public/Bug/Display.html?id=150141
[ "%version" = 3.010 ] && rm t/505parser-bodymp.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%if_disabled spamassasin
rm %buildroot%perl_vendor_privlib/Mail/Message/Wrapper/SpamAssassin.{pm,pod}
rm %buildroot%perl_vendor_privlib/Mail/Box/Search/SpamAssassin.{pm,pod}
%endif

%files
%doc ChangeLog README README.todo examples README.md
%perl_vendor_privlib/Mail/
%if_enabled spamassasin
%exclude %perl_vendor_privlib/Mail/Message/Wrapper/SpamAssassin.p*
%exclude %perl_vendor_privlib/Mail/Box/Search/SpamAssassin.p*
%endif

%if_enabled spamassasin
%files -n perl-Mail-Box-SpamAssassin
%perl_vendor_privlib/Mail/Message/Wrapper/SpamAssassin.p*
%perl_vendor_privlib/Mail/Box/Search/SpamAssassin.p*
%endif

%changelog
* Mon Oct 23 2023 Igor Vlasenko <viy@altlinux.org> 3.010-alt2
- fixed build
- updated license
- added disabled SpamAssassin subpackage

* Wed Jul 26 2023 Vitaly Lipatov <lav@altlinux.ru> 3.010-alt1
- new version 3.010 (with rpmrb script)

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 3.009-alt1
- automated CPAN update

* Wed Apr 22 2020 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.008-alt3
- Reverted previous change.

* Sun Apr 19 2020 Igor Vlasenko <viy@altlinux.ru> 3.008-alt2
- dropped perl(arybase.pm) autodependency

* Mon Oct 07 2019 Igor Vlasenko <viy@altlinux.ru> 3.008-alt1
- automated CPAN update

* Sun May 12 2019 Igor Vlasenko <viy@altlinux.ru> 3.007-alt1
- automated CPAN update

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 3.006-alt1
- automated CPAN update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 3.005-alt1
- automated CPAN update

* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 3.004-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 3.003-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.120-alt1
- automated CPAN update

* Mon Apr 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.118-alt2
- build w/o HTML-Format

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 2.118-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.117-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 2.115-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 2.114-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.113-alt1
- automated CPAN update

* Sat Mar 15 2014 Igor Vlasenko <viy@altlinux.ru> 2.112-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.111-alt1
- automated CPAN update

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 2.110-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.109-alt1
- automated CPAN update

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.108-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.106-alt1
- automated CPAN update

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
