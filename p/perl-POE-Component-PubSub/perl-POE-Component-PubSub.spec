%define module POE-Component-PubSub

Name: perl-%module
Version: 0.05
Release: alt1

Summary: POE-Component-PubSub - Perl module

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: %module-%version.tar.gz

# Automatically added by buildreq on Mon Nov 15 2010
BuildRequires: perl-Module-Build perl-POE

%description
A generic publish/subscribe POE::Component that
enables POE::Sessions to publish events to which other POE::Sessions may
subscribe.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/POE/*

%changelog
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.05-alt1
- initial build for ALT Linux Sisyphus

