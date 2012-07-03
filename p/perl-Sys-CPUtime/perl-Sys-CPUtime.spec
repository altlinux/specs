#################### WARNING! ######################
# this spec file is for ALT Linux distro only.     #
# other distro may have problems with rpm macro!!! #
####################################################

%define module Sys-CPUtime

Name: perl-%module
Version: 0.10
Release: alt2.2

Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Perl extension for SIGXCPU workaround
License: Artistic
Group: Development/Perl

Source: %module-%version.tar.gz

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: perl-devel

%description
The Defence from Provider module provides perl API for unix
syscalls getrusage and getrlimit as long as SIGXCPU workaround.

if we run on a system with enabled CPU time limit 
we can fork just before time limit will be exceeded.
it allows us to continue the same operations but with new pid
to create persistent daemons on a hosting with CPU time limits.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Sys
%perl_vendor_autolib/Sys

%changelog
* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.10-alt2.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt2.1
- rebuilt with perl 5.12

* Wed Sep 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- removed perl dir ownership

* Thu Jun 28 2007 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- First build for Sisyphus.
