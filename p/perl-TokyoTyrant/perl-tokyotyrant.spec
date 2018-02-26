%define bname tokyotyrant
%define Name TokyoTyrant

%define module %Name
%define m_distro %bname-perl
%define m_name %module
%define m_author_id Mikio Hirabayashi
%def_disable test

Name: perl-%module
Version: 1.8
Release: alt1.1
Summary: Pure Perl Interface of Tokyo Tyrant
License: %lgpl2plus
Group: Development/Perl
Url: http://tokyocabinet.sourceforge.net
Source: %m_distro-%version.tar
BuildArch: noarch
Provides: perl-%bname = %version-%release
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses

BuildRequires: perl-devel perl-Encode

%description
This module implements the pure Perl client which connects to the
server of Tokyo Tyrant and speaks its original binary protocol.


%prep
%setup -n %m_distro-%version


%build
%perl_vendor_build


%install
%perl_vendor_install
rm -f %buildroot%perl_vendorlib/*.pl


%files
%doc tcrtest.pl doc/* example
%perl_vendorlib/%module.*


%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Mar 11 2009 Led <led@altlinux.ru> 1.8-alt1
- 1.8

* Mon Feb 16 2009 Led <led@altlinux.ru> 1.7-alt1
- 1.7

* Sun Feb 15 2009 Led <led@altlinux.ru> 1.6-alt1
- 1.6

* Sat Dec 27 2008 Led <led@altlinux.ru> 1.4-alt1
- 1.4

* Sun Dec 14 2008 Led <led@altlinux.ru> 1.3-alt1
- 1.3

* Thu Oct 30 2008 Led <led@altlinux.ru> 1.2-alt1
- initial build
