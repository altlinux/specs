%define dist WWW-Mechanize
Name: perl-%dist
Version: 1.70
Release: alt1

Summary: Handy web browsing in a Perl object
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/J/JE/JESSE/WWW-Mechanize-1.70.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-HTML-Form perl-HTML-Tree perl-HTTP-Daemon perl-HTTP-Server-Simple perl-LWP-Protocol-https perl-Test-Exception perl-Test-NoWarnings perl-Test-Pod perl-Test-Pod-Coverage perl-Test-Warn

%description
"WWW::Mechanize", or Mech for short, helps you automate interaction
with a website.  It supports performing a sequence of page fetches
including following links and submitting forms. Each fetched page
is parsed and its links and forms are extracted. A link or a form
can be selected, form fields can be filled and the next page can
be fetched.  Mech also stores a history of the URLs you've visited,
which can be queried and revisited.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build --nolive

%install
%perl_vendor_install

%files
%doc	Changes
	%_bindir/mech-dump
%dir	%perl_vendor_privlib/WWW
	%perl_vendor_privlib/WWW/Mechanize.pm
%dir	%perl_vendor_privlib/WWW/Mechanize
	%perl_vendor_privlib/WWW/Mechanize/*.pm
%doc	%perl_vendor_privlib/WWW/Mechanize/*.pod

%changelog
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
