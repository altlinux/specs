%define _unpackaged_files_terminate_build 1
%define dist MailTools
Name: perl-%dist
Version: 2.20
Release: alt1

Summary: Perl modules related to mail applications
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MA/MARKOV/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012 (-bi)
BuildRequires: perl-Net-SMTP-SSL perl-TimeDate perl-devel sendmail-common

%description
This is MailTools, a set of perl modules related to mail applications.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	ChangeLog README README.demos examples README.md
%dir	%perl_vendor_privlib/Mail
	%perl_vendor_privlib/Mail/*.pm
%doc	%perl_vendor_privlib/Mail/*.pod
%dir	%perl_vendor_privlib/Mail/Field
	%perl_vendor_privlib/Mail/Field/*.pm
%doc	%perl_vendor_privlib/Mail/Field/*.pod
%dir	%perl_vendor_privlib/Mail/Mailer
	%perl_vendor_privlib/Mail/Mailer/*.pm
	%perl_vendor_privlib/MailTools.pm
	%perl_vendor_privlib/MailTools.pod

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.20-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.19-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.18-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.16-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1
- automated CPAN update

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 2.11-alt1
- 2.08 -> 2.11

* Tue Aug 09 2011 Alexey Tourbin <at@altlinux.ru> 2.08-alt1
- 2.07 -> 2.08

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 2.07-alt1
- 2.06 -> 2.07

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 2.06-alt1
- 2.04 -> 2.06
- requires perl-Net-SMTP-SSL due to support for smtps

* Tue Sep 16 2008 Alexey Tourbin <at@altlinux.ru> 2.04-alt1
- 2.03 -> 2.04

* Tue May 06 2008 Alexey Tourbin <at@altlinux.ru> 2.03-alt1
- 1.76 -> 2.03

* Tue Apr 10 2007 Alexey Tourbin <at@altlinux.ru> 1.76-alt1
- 1.74 -> 1.76
- fixed perl syntax in qmail.pm (rt.cpan.org #26237)

* Thu Apr 20 2006 Alexey Tourbin <at@altlinux.ru> 1.74-alt1
- 1.67 -> 1.74

* Wed Apr 06 2005 Alexey Tourbin <at@altlinux.ru> 1.67-alt1
- 1.66 -> 1.67

* Tue Jan 25 2005 Alexey Tourbin <at@altlinux.ru> 1.66-alt1
- 1.64 -> 1.66
- manual pages not packaged (use perldoc)

* Thu Aug 19 2004 Alexey Tourbin <at@altlinux.ru> 1.64-alt1
- 1.62 -> 1.64

* Wed Mar 24 2004 Alexey Tourbin <at@altlinux.ru> 1.62-alt1
- 1.61 -> 1.62, testfile detection fixed upstream

* Sun Mar 14 2004 Alexey Tourbin <at@altlinux.ru> 1.61-alt1
- 1.61
- fixed testfile detection

* Fri Oct 03 2003 Alexey Tourbin <at@altlinux.ru> 1.60-alt1
- 1.60

* Thu Sep 04 2003 Alexey Tourbin <at@altlinux.ru> 1.59-alt1
- 1.59
- buildreq re-applied (fixes build in the hasher)

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 1.58-alt1
- 1.58

* Tue Nov 05 2002 Alexey Tourbin <at@altlinux.ru> 1.51-alt1
- 1.51
- perl-5.8 build with new rpm macros

* Wed Apr 03 2002 Stanislav Ievlev <inger@altlinux.ru> 1.44-alt1
- 1.44

* Tue Nov 27 2001 Stanislav Ievlev <inger@altlinux.ru> 1.40-alt1
- 1.40

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.15-ipl4mdk
- Rebuilt with perl-5.6.1

* Fri Mar 30 2001 Peter 'Nidd' Novodvorsky <nidd@altlinux.ru> 1.15-ipl3mdk
- Spec Global Cleanup

* Sun Feb 4 2001 AEN <aen@logic.ru>
- RE adaptation

* Thu Oct 12 2000 François Pons <fpons@mandrakesoft.com> 1.15-1mdk
- removed typo patch as now applied.
- 1.15.

* Mon Aug 07 2000 François Pons <fpons@mandrakesoft.com> 1.14.1-3mdk
- added missing clean.

* Thu Aug 03 2000 François Pons <fpons@mandrakesoft.com> 1.14.1-2mdk
- macroszifications.
- noarch.
- add doc.

* Tue Jul 18 2000 François Pons <fpons@mandrakesoft.com> 1.14.1-1mdk
- created patch to solve typo in Cap.pm.
- avoid using version naming conventions from package.
- 1.1401.

* Mon Apr  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.14-1mdk
- 1.14
- fixed group
