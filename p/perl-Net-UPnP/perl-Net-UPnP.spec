%define module Net-UPnP
%define m_distro Net-UPnP
%define m_name Net::UPnP
%define _enable_test 1

Name: perl-Net-UPnP
Version: 1.4.2
Release: alt1.1

Summary: Perl extension for UPnP

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Anton Farygin <rider@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/S/SK/SKONNO/%m_distro-%version.tar.gz

# Automatically added by buildreq on Wed Feb 06 2008
BuildRequires: perl-devel perl-version

%description
This package provides some functions to control UPnP devices.

Currently, the package provides only functions for the control point.
To control UPnP devices, see Net::UPnP::ControlPoint.

As a sample of the control point, the package provides
Net::UPnP::AV::MediaServer to control the devices such as
DLNA media servers. As the example, please dms2vodcast.pl
that converts from the MPEG2 movies to the MPEG4 one and
outputs the RSS file for Vodcasting.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Feb 15 2010 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- new version

* Tue Nov 25 2008 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- new version

* Wed Oct 15 2008 Anton Farygin <rider@altlinux.ru> 1.4-alt1
- new version

* Mon Sep 08 2008 Anton Farygin <rider@altlinux.ru> 1.2.4-alt1
- new version
- fixed build

* Wed Feb 06 2008 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- first build for ALT Linux Sisyphus

