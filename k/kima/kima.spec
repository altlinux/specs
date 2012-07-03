Name:		kima
Version:	0.7.4
Release:	alt3
Summary:	A KDE3 Kicker Applet
Source0:	%name-%version.tar.gz
Url:		http://kima.sourceforge.net/
Group:		Monitoring
License:	GPLv2
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Patch0:		%name-0.7.4-admin-new-autotools.diff
Patch1:		%name-0.7.4-fix-autoconf-2.64.diff

# Automatically added by buildreq on Fri Oct 22 2010 (-bi)
BuildRequires: gcc-c++ imake kdelibs-devel libXt-devel libhal-devel libjpeg-devel libqt3-devel xml-utils xorg-cf-files libtqt-devel

%description
This applet monitors various temperature, frequency and fan sources in your kicker panel.
Make sure you have enabled a supported kernel module.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%add_optflags -I%_includedir/tqtinterface
make -f admin/Makefile.common
%K3configure --disable-rpath
%make_build

%install
%K3install
%K3find_lang %name --with-kde

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_libdir/kde3/lib%name.so
%_K3datadir/apps/kicker/applets/%name.desktop

%changelog
* Fri Mar 04 2011 Timur Aitov <timonbl4@altlinux.org> 0.7.4-alt3
- move to alternate place

* Wed Feb 16 2011 Motsyo Gennadi <drool@altlinux.ru> 0.7.4-alt2.2
- build without aRts

* Tue Nov 02 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.4-alt2.1
- remove provides & obsoletes to CPUInfo (It is alive!)

* Mon Oct 25 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.4-alt2
- add provides & obsoletes to CPUInfo (close #24384)

* Fri Oct 22 2010 Motsyo Gennadi <drool@altlinux.ru> 0.7.4-alt1
- initial build for ALT Linux
