%define dist JSON-Any
Name: perl-%dist
Version: 1.29
Release: alt2

Summary: Wrapper Class for the various JSON classes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-JSON perl-JSON-DWIW perl-JSON-PP perl-Pod-Escapes perl-YAML-Syck perl-devel

%description
This module tries to provide a coherent API to bring together the various
JSON modules currently on CPAN. This module will allow you to code to any
JSON API and have it work regardless of which JSON module is actually
installed.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/JSON

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 1.29-alt2
- rebuilt as plain src.rpm

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Apr 09 2010 Alexey Tourbin <at@altlinux.ru> 1.22-alt1
- 1.21 -> 1.22

* Sat Oct 03 2009 Michael Bochkaryov <misha@altlinux.ru> 1.21-alt1
- 1.21 version

* Sat Sep 06 2008 Michael Bochkaryov <misha@altlinux.ru> 1.17-alt1
- 1.17 version
- fix directory ownership violation

* Mon May 26 2008 Michael Bochkaryov <misha@altlinux.ru> 1.16-alt1
- first build for ALT Linux Sisyphus
