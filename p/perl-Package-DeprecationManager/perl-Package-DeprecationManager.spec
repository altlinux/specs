%define _unpackaged_files_terminate_build 1
%define dist Package-DeprecationManager
Name: perl-%dist
Version: 0.16
Release: alt1

Summary: Manage deprecation warnings for your distribution
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DR/DROLSKY/Package-DeprecationManager-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 09 2011
BuildRequires: perl-List-MoreUtils perl-Test-Fatal perl-Test-Output perl-Test-Requires perl(Test/Warnings.pm) perl(Package/Stash.pm) perl(namespace/autoclean.pm) perl(Sub/Name.pm)

%description
This module allows you to manage a set of deprecations for one or more modules.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/Package*

%changelog
* Wed Mar 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt1
- 0.11 -> 0.13
- fixed build with Carp >= 1.25

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Sun Jan 09 2011 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- initial revision, for Moose-1.09+
