%define module	Convert-TNEF

Name: perl-%module
Version: 0.18
Release: alt2
Summary: %module (module for perl)

License: GPL or Artistic
Group: Development/Perl
Url: %CPAN %module

BuildArch: noarch
Source: http://www.cpan.org/authors/id/D/DO/DOUGW/Convert-TNEF-%{version}.tar.gz

BuildRequires: perl-IO-stringy perl-MIME-tools perl-devel

%description
TNEF stands for Transport Neutral Encapsulation Format, and if you've
ever been unfortunate enough to receive one of these files as an email
attachment, you may want to use this module.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc MANIFEST README Changes
%perl_vendor_privlib/Convert*

%changelog
* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2
- fixed url

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.17-alt2
- drop %%perl_vendor_man3dir

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.17-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Mar 19 2004 Alexey Shabalin <shaba@altlinux.ru> 0.17-alt1
- fix spec

* Thu Dec 04 2003 Alexey Shabalin <shaba@altlinux.ru> 0.17-alt0.1
- First release for ALT
