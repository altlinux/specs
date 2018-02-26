%define dist Test-Class
Name: perl-%dist
Version: 0.36
Release: alt1

Summary: Easily create test classes in an xUnit/JUnit style
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-Attribute-Handlers perl-MRO-Compat perl-Module-Build perl-Test-Exception

%description
Test::Class provides a simple way of creating classes and objects
to test your code in an xUnit style.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test*

%changelog
* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 0.36-alt1
- 0.33 -> 0.36

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Nov 19 2009 Vitaly Lipatov <lav@altlinux.ru> 0.33-alt1
- initial build for ALT Linux Sisyphus
