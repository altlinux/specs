%define dist String-RewritePrefix
Name: perl-%dist
Version: 0.006
Release: alt1

Summary: Rewrite strings based on a set of known prefixes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/String-RewritePrefix-0.006.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 14 2010
BuildRequires: perl-Sub-Exporter perl-devel

%description
%summary.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/String*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- automated CPAN update

* Wed Apr 14 2010 Alexey Tourbin <at@altlinux.ru> 0.005-alt1
- initial reivision, for Catalyst
