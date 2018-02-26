%define module		MPlayer
%define m_distro	MPlayer
%define m_name		MPlayer

Name: perl-%module
Version: 0.04
Release: alt3

Summary: A perl module for MPlayer control
Group: Development/Perl
License: GPL

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://www.mplayertv.tk/
Source: http://mplayertv.zer0.hu/downloads/%m_distro-%version.tar.bz2

BuildArch: noarch

# nvidia_glx_173.14.12 
# Automatically added by buildreq on Fri Nov 21 2008
BuildRequires: mplayer perl-devel perl-threads

%description
An OO interface to MPlayer for Perl

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/MPlayer.pm
%doc README Changes

%changelog
* Fri Nov 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt3
- fix directory ownership violation
- disable man packaging
- update buildreqs

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt2
- remove glib/gtk+ from build requires

* Sun Apr 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- first build for ALT Linux Sisyphus
