%define module	Convert-TNEF

Name: perl-%module
Version: 0.17
Release: alt2
Summary: %module (module for perl)

License: GPL or Artistic
Group: Development/Perl
Url: http://www.cpan.org/modules/by-module/Convert/

BuildArch: noarch
Source: %url/%module-%version.tar.bz2

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
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.17-alt2
- drop %%perl_vendor_man3dir

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.17-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Mar 19 2004 Alexey Shabalin <shaba@altlinux.ru> 0.17-alt1
- fix spec

* Thu Dec 04 2003 Alexey Shabalin <shaba@altlinux.ru> 0.17-alt0.1
- First release for ALT
