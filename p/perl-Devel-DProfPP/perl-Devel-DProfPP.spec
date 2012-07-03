%define module Devel-DProfPP
%define _enable_test 1

Name: perl-%module
Version: 1.3
Release: alt2.1

Summary: Devel::DProfPP - Parse Devel::DProf output

License: Artistic
Group: Development/Perl
Url: %CPAN(%module)

Packager: Igor Vlasenko <viy@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/modules/by-module/Devel/%module-%version.tar.gz
#Source: %module-%version.tar.gz

# Automatically added by buildreq on Tue Nov 22 2005
BuildRequires: perl-devel

%description
This module takes the output file from Devel::DProf (typically tmon.out) 
and parses it. By hooking subroutines onto the 'enter' and 'leave' events, 
you can produce useful reports from the profiling data.

%prep
%setup -q -n %module-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Sep 03 2008 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2
- removed perl dir ownership

* Tue Nov 22 2005 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1.1
- BuildRequires fix

* Fri Nov 18 2005 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- first build for ALT Linux Sisyphus

