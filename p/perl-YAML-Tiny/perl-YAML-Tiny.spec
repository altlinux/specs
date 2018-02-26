%define dist YAML-Tiny
Name: perl-%dist
Version: 1.50
Release: alt1

Summary: Read/Write YAML files with as little code as possible
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/A/AD/ADAMK/YAML-Tiny-1.50.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-YAML perl-YAML-Syck perl-devel

%description
YAML::Tiny is a perl class for reading and writing YAML-style files,
written with as little code as possible, reducing load time and
memory overhead.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/YAML*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.46-alt1
- 1.41 -> 1.46

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 1.41-alt1
- 1.40 -> 1.41

* Thu Aug 06 2009 Alexey Tourbin <at@altlinux.ru> 1.40-alt1
- 1.32 -> 1.40

* Wed Sep 24 2008 Alexey Tourbin <at@altlinux.ru> 1.32-alt1
- initial revision (for new Module::Install)
