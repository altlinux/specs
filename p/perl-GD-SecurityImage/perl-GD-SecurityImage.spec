%define module GD-SecurityImage

Name: perl-%module
Version: 1.71
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Security image (captcha) generator as perl module
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/B/BU/BURAK/GD-SecurityImage-1.71.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 24 2010
BuildRequires: perl-GD perl-Magick perl-Test-Pod perl-Test-Pod-Coverage

%description
This module gives you a basic interface to create "security images". Most
internet software use these in their registration screens to block robot
programs (which may register tons of fake member accounts). This module
gives you a basic interface to create such an image.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/GD

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1
- automated CPAN update

* Wed Nov 24 2010 Victor Forsiuk <force@altlinux.org> 1.70-alt1
- Initial build.
