%define dist Net-Daemon
Name: perl-%dist
Version: 0.48
Release: alt1

Summary: Perl extension for portable daemons
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MN/MNOONING/Net-Daemon-0.48.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Mar 02 2011
BuildRequires: perl-devel perl-threads

%description
Net::Daemon is an abstract base class for implementing portable
server applications.

%prep
%setup -q -n %dist-%version

%build
%if "%(logger -d -u /dev/log -p user.debug test &>/dev/null || echo no)" == "no"
: syslog not available
%def_without test
%endif

%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Net

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Wed Mar 02 2011 Alexey Tourbin <at@altlinux.ru> 0.47-alt1
- 0.46 -> 0.47

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 0.46-alt1
- 0.38 -> 0.46

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.38-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Apr 15 2004 Alexey Tourbin <at@altlinux.ru> 0.38-alt1
- 0.37 -> 0.38

* Mon Oct 20 2003 Alexey Tourbin <at@altlinux.ru> 0.37-alt2
- skip test when syslog not available

* Fri Nov 01 2002 Stanislav Ievlev <inger@altlinux.ru> 0.37-alt1
- Inital release for ALT
