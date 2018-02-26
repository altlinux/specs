%define dist Term-UI
Name: perl-%dist
Version: 0.26
Release: alt1

Summary: User interfaces via Term::ReadLine made easy
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-Log-Message-Simple perl-Term-ReadLine-Gnu perl-devel

%description
Term::UI provides methods to ask both elaborate questions as well
as simple yes/no questions via a Term::ReadLine interface using a
template. It can also parse options per unix style.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/Term

%changelog
* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.26-alt1
- 0.20 -> 0.26
- fixed unpackaged directory

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt2
- fix directory ownership violation

* Fri Jun 13 2008 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt1
- new version 0.18 (with rpmrb script)
- update buildreq

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt1
- first build for ALT Linux Sisyphus
