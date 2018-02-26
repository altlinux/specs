%define module POE-Component-Pluggable

Name: perl-%module
Version: 1.26
Release: alt2

Summary: A base class for creating plugin enabled POE Components

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: http://www.cpan.org/authors/id/B/BI/BINGOS/%module-%version.tar.gz

# Automatically added by buildreq on Fri Oct 23 2009
BuildRequires: perl-POE perl-Task-Weaken perl-Test-Pod perl-Test-Pod-Coverage

%description
POE::Component::Pluggable is a base class for creating plugin enabled
POE Components. It is a generic port of POE::Component::IRC's plugin
system.

If your component dispatches events to registered POE sessions, then
POE::Component::Pluggable may be a good fit for you.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/POE/Component/*

%changelog
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.26-alt2
- drop %%perl_vendor_man3dir

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.24-alt1
- 1.24

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 1.10-alt1
- initial build for ALT Linux Sisyphus

