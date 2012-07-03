%define m_distro Class-Adapter
Name: perl-Class-Adapter
Version: 1.08
Release: alt1
Summary: Class::Adapter - Perl implementation of the "Adapter" Design Pattern

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~adamk/Class-Adapter/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Class/Adapter*
%doc Changes README 

%changelog
* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Thu Apr 15 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- New version 1.07

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.06-alt1
- initial build
