%define _unpackaged_files_terminate_build 1
%define dist MooseX-NonMoose
Name: perl-%dist
Version: 0.26
Release: alt1.2

Summary: Easy subclassing of non-Moose classes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DO/DOY/MooseX-NonMoose-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Moose perl-Test-Fatal perl-Test-Script perl(List/MoreUtils.pm)

%description
MooseX::NonMoose allows for easily subclassing non-Moose classes with
Moose, taking care of the annoying details connected with doing this,
such as setting up proper inheritance from Moose::Object and installing
(and inlining, at "make_immutable" time) a constructor that makes sure
things like "BUILD" methods are called.  It tries to be as non-intrusive
as possible - when this module is used, inheriting from non-Moose classes
and inheriting from Moose classes should work identically, aside from the
few caveats mentioned below.  One of the goals of this module is that
including it in a Moose::Exporter-based package used across an entire
application should be possible, without interfering with classes that
only inherit from Moose modules, or even classes that don't inherit from
anything at all.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX

%changelog
* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1.2
- fixed build

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1.1
- rebuild to restore role requires

* Fri Feb 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Sat Feb 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- initial revision
