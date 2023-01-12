%define _unpackaged_files_terminate_build 1
%define dist Email-MIME
Name: perl-%dist
Version: 1.953
Release: alt1

Summary: Easy MIME message parsing
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RJ/RJBS/%{dist}-%{version}.tar.gz

BuildArch: noarch

Provides: perl-Email-MIME-Modifier = 1.499 perl-Email-MIME-Creator = 1.499
Obsoletes: perl-Email-MIME-Modifier < 1.499 perl-Email-MIME-Creator < 1.499

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-Email-MIME-ContentType perl-Email-MIME-Encodings perl-Email-MessageID perl-Email-Simple perl-MIME-Types perl-Test-Pod perl-Test-Pod-Coverage perl(parent.pm) perl(Capture/Tiny.pm) perl(Email/Address.pm) perl(Module/Runtime.pm) perl(Email/Address/XS.pm)

%description
This is an extension of the Email::Simple module, to handle MIME
encoded messages. It takes a message as a string, splits it up into
its constituent parts, and allows you access to various parts of
the message. Headers are decoded from MIME encoding.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Email*

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 1.953-alt1
- automated CPAN update

* Wed Dec 15 2021 Igor Vlasenko <viy@altlinux.org> 1.952-alt1
- automated CPAN update

* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.949-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.946-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.940-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.937-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.936-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.929-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.928-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.926-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.925-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.924-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.922-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.911-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.910-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.906-alt1
- 1.903 -> 1.906

* Wed Apr 28 2010 Alexey Tourbin <at@altlinux.ru> 1.903-alt1
- 1.863 -> 1.903
- provides and obsoletes perl-Email-MIME-Modifier perl-Email-MIME-Creator

* Sun Apr 12 2009 Alexey Tourbin <at@altlinux.ru> 1.863-alt1
- 1.861 -> 1.863

* Mon Sep 01 2008 Alexey Tourbin <at@altlinux.ru> 1.861-alt1
- 1.85 -> 1.861

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 1.85-alt1
- initial revision
