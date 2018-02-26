#################### WARNING! ######################
# this spec file is for ALT Linux distro only.     #
# other distro may have problems with rpm macro!!! #
####################################################

%define module Data-Array2ArrayMap-Hash-XSTree

Name: perl-%module
Version: 0.13
Release: alt2.2

Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: a Perl interface to multiple tree data structures.
License: GPL or Artistic
Group: Development/Perl
Source: %module-%version.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: perl-Clone perl-devel

%description
%{summary}

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc README Changes README.ru FAQ
%perl_vendor_archlib/Data
%perl_vendor_autolib/Data

%changelog
* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt2.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt2.1
- rebuilt with perl 5.12

* Tue Sep 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- perl packaging fix

* Tue Oct 23 2007 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- new version

* Tue Oct 16 2007 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- First build for Sisyphus.
