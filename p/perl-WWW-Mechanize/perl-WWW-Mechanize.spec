%define _unpackaged_files_terminate_build 1
%define dist WWW-Mechanize
Name: perl-%dist
Version: 2.16
Release: alt1

Summary: Handy web browsing in a Perl object
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/S/SI/SIMBABQUE/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-HTML-Form perl-HTML-Tree perl-HTTP-Daemon perl-HTTP-Server-Simple perl-LWP-Protocol-https perl-Test-Exception perl-Test-NoWarnings perl-Test-Pod perl-Test-Pod-Coverage perl-Test-Warn perl(Test/Output.pm) perl(Test/RequiresInternet.pm) perl(Test/Fatal.pm) perl(Tie/RefHash.pm) perl(Test/Warnings.pm) perl(Test/Deep.pm) perl(Path/Tiny.pm)

%description
"WWW::Mechanize", or Mech for short, helps you automate interaction
with a website.  It supports performing a sequence of page fetches
including following links and submitting forms. Each fetched page
is parsed and its links and forms are extracted. A link or a form
can be selected, form fields can be filled and the next page can
be fetched.  Mech also stores a history of the URLs you've visited,
which can be queried and revisited.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build --nolive

%install
%perl_vendor_install

%files
%doc	Changes CONTRIBUTORS README.md
	%_bindir/mech-dump
	%_man1dir/mech-dump*
%dir	%perl_vendor_privlib/WWW
	%perl_vendor_privlib/WWW/Mechanize.pm
%dir	%perl_vendor_privlib/WWW/Mechanize
	%perl_vendor_privlib/WWW/Mechanize/*.pm
%doc	%perl_vendor_privlib/WWW/Mechanize/*.pod

%changelog
* Sun Feb 12 2023 Igor Vlasenko <viy@altlinux.org> 2.16-alt1
- automated CPAN update

* Mon Aug 22 2022 Igor Vlasenko <viy@altlinux.org> 2.15-alt1
- automated CPAN update

* Mon Aug 01 2022 Igor Vlasenko <viy@altlinux.org> 2.13-alt1
- automated CPAN update

* Mon Jul 25 2022 Igor Vlasenko <viy@altlinux.org> 2.12-alt1
- automated CPAN update

* Wed Jul 06 2022 Igor Vlasenko <viy@altlinux.org> 2.10-alt1
- automated CPAN update

* Wed Jun 15 2022 Igor Vlasenko <viy@altlinux.org> 2.09-alt1
- automated CPAN update

* Wed Jun 01 2022 Igor Vlasenko <viy@altlinux.org> 2.08-alt1
- automated CPAN update

* Sun May 01 2022 Igor Vlasenko <viy@altlinux.org> 2.07-alt1
- automated CPAN update

* Tue Oct 26 2021 Igor Vlasenko <viy@altlinux.org> 2.06-alt1
- automated CPAN update

* Fri Sep 24 2021 Igor Vlasenko <viy@altlinux.org> 2.05-alt1
- automated CPAN update

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 2.04-alt1
- automated CPAN update

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1
- automated CPAN update

* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1
- automated CPAN update

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.99-alt1
- automated CPAN update

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 1.96-alt1
- automated CPAN update

* Thu Oct 31 2019 Igor Vlasenko <viy@altlinux.ru> 1.95-alt1
- automated CPAN update

* Sun Oct 13 2019 Igor Vlasenko <viy@altlinux.ru> 1.94-alt1
- automated CPAN update

* Mon Oct 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.93-alt1
- automated CPAN update

* Sun Aug 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.92-alt1
- automated CPAN update

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 1.91-alt1
- automated CPAN update

* Tue Nov 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.90-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.89-alt1
- automated CPAN update

* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.88-alt1
- automated CPAN update

* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.87-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.86-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.84-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.83-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.79-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.75-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.73-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.70-alt1
- automated CPAN update

* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 1.68-alt1
- 1.66 -> 1.68

* Wed Mar 23 2011 Alexey Tourbin <at@altlinux.ru> 1.66-alt1
- 1.34 -> 1.66

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.34-alt1.1
- rebuilt with perl 5.12

* Tue Jun 17 2008 Alexey Tourbin <at@altlinux.ru> 1.34-alt1
- 1.18 -> 1.34

* Sun May 28 2006 Alexey Tourbin <at@altlinux.ru> 1.18-alt1
- 1.14 -> 1.18

* Wed Aug 31 2005 Alexey Tourbin <at@altlinux.ru> 1.14-alt1
- 1.12 -> 1.14
- disabled live tests

* Sun Mar 20 2005 Alexey Tourbin <at@altlinux.ru> 1.12-alt1
- 1.10 -> 1.12

* Thu Feb 03 2005 Alexey Tourbin <at@altlinux.ru> 1.10-alt1
- 1.02 -> 1.10
- manual pages not packaged (use perldoc)

* Sat Apr 17 2004 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- initial revision, inspired by Randal Schwartz
