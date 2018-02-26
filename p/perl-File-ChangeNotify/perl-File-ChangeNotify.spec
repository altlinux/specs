%define dist File-ChangeNotify
Name: perl-%dist
Version: 0.20
Release: alt1

Summary: Watch for changes to files, cross-platform style
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DR/DROLSKY/File-ChangeNotify-0.20.tar.gz

BuildArch: noarch

# On Linux, we use Inotify
%add_findreq_skiplist */File/ChangeNotify/Watcher/KQueue.pm

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-Linux-Inotify2 perl-Module-Build perl-Module-Pluggable perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-Test-Exception perl-namespace-autoclean

%description
This module provides an API for creating a File::ChangeNotify::Watcher
subclass that will work on your platform.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- 0.13 -> 0.19

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.13-alt1
- initial revision, for Catalyst
