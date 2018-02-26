Name: perl-MouseX-Getopt
Version: 0.34
Release: alt1

Summary: MouseX::Getopt - Mouse role for processing command line options
Group: Development/Perl
License: Perl

Url: %CPAN MouseX-Getopt
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Mouse perl-Getopt-Long-Descriptive perl-Test-Exception perl-Test-Warn

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/MouseX/Getopt*
%doc LICENSE ChangeLog README

%changelog
* Mon Apr 16 2012 Vladimir Lettiev <crux@altlinux.ru> 0.34-alt1
- 0.34

* Thu Feb 17 2011 Vladimir Lettiev <crux@altlinux.ru> 0.33-alt1
- initial build
