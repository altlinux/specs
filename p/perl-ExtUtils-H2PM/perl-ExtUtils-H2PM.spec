Name: perl-ExtUtils-H2PM
Version: 0.10
Release: alt1

Summary: automatically generate perl modules to wrap C header files
Group: Development/Perl
License: perl

Url: %CPAN ExtUtils-H2PM
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl(ExtUtils/CBuilder.pm) perl(Module/Build.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/ExtUtils/H2PM*
%doc Changes LICENSE README

%changelog
* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- initial build for ALTLinux

