%define dist B-Lint
Name: perl-%dist
Version: 1.13
Release: alt1

Summary: Perl lint
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/F/FL/FLORA/B-Lint-1.13.tar.gz
Patch: perl-B-Lint-1.12-alt-install.patch

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 28 2011
BuildRequires: perl-Module-Pluggable perl-devel

%description
The B::Lint module is equivalent to an extended version of the -w option
of perl. It is named after the program lint which carries out a similar
process for C programs.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/B

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Thu Apr 28 2011 Alexey Tourbin <at@altlinux.ru> 1.12-alt1
- initial revision
