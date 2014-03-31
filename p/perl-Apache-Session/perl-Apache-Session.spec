%filter_from_requires /^perl.Apache.pm./d
# TODO: drop apache2 dependency?
#filter_from_requires /^perl.Apache2.RequestUtil.pm./d
%define dist Apache-Session
Name: perl-%dist
Version: 1.92
Release: alt2

Summary: A persistence framework for session data
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/C/CH/CHORNY/Apache-Session-%{version}.tar.gz
# https://bugzilla.redhat.com/bugzilla/attachment.cgi?id=118577, from Chris Grau
Patch0:         Apache-Session-mp2.patch

BuildArch: noarch

# Automatically added by buildreq on Mon Oct 03 2011 (-bi)
BuildRequires: perl-CGI perl-DBI perl-DBM perl-IPC-SysV perl-Module-Build perl-Test-Deep perl-Test-Exception perl-Test-Pod

%description
Apache::Session is a persistence framework which is particularly useful
for tracking session data between httpd requests.  Apache::Session is
designed to work with Apache and mod_perl, but it should work under
CGI and other web servers, and it also works outside of a web server
altogether.

%prep
%setup -q -n %dist-%version
find -type f -exec perl -pi -e 's/\r\n/\n/g' {} \;
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/Apache

%changelog
* Mon Mar 31 2014 Igor Vlasenko <viy@altlinux.ru> 1.92-alt2
- dropped dependency on apache-mod_perl-base (closes: #29932)

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.92-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.91-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.90-alt1
- automated CPAN update

* Mon Oct 03 2011 Alexey Tourbin <at@altlinux.ru> 1.89-alt1
- 1.80 -> 1.89

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.80-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Mar 25 2006 Andrey Brindeew <abr@altlinux.org> 1.80-alt1
- 1.80 release

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.6-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sat Mar 06 2004 Andrey Brindeew <abr@altlinux.ru> 1.6-alt1
- 1.6

* Mon Oct 06 2003 Andrey Brindeew <abr@altlinux.ru> 1.54-alt3
- Both Packager and Summary tags was updated
- Url tag fixed

* Mon Sep 29 2003 Alexey Tourbin <at@altlinux.ru> 1.54-alt2.1
- BuildRequires updated (with buildreq -bi)

* Sun Sep 07 2003 Sir Raorn <raorn@altlinux.ru> 1.54-alt2
- Fix buildrequires
- Do not test Apache::Session::Flex and Apache::Session::Lock::Semaphore
- Add Url tag
- Add Packager tag

* Sat Jun 21 2003 Sir Raorn <raorn@altlinux.ru> 1.54-alt1
- Built for Sisyphus


