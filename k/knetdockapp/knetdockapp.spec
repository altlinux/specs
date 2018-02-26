Name:		knetdockapp
Version:	0.82.3
Release:	alt3
Summary:	Network Monitor Systray Application
Source:		http://www.kde-apps.org/CONTENT/content-files/29398-%name-%version.tar.bz2
Patch0:		%name-0.82-alt_doc.diff
Patch1:		%name-0.82.3-admin-new-autotools.diff
Url:		http://www.kde-apps.org/content/show.php/KNetDockApp?content=29398
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Group:		Networking/Other
License:	GPLv2

# Automatically added by buildreq on Mon Jul 30 2007 (-bi)
BuildRequires: gcc-c++ imake kdelibs-devel libXext-devel libXt-devel libqt3-devel xorg-cf-files

%description
A small application that docks in the systray and monitors the activity of the
selected network interface.
It also monitors the link status - could detect if a networking cable is
attached to the nic or not...
Supports session management, and runs on next logins.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%__subst 's/\.la\>/.so/g' admin/acinclude.m4.in
%__subst 's/\(-Wl,--no-undefined\)/-Wl,--warn-unresolved-symbols \1/g' admin/acinclude.m4.in

%build
%add_optflags -I%_includedir/tqtinterface
make -f admin/Makefile.common
%K3configure

%make_build

%install
%K3install

%K3find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_K3bindir/%name
%_K3datadir/applnk/Utilities/%name.desktop
%_K3datadir/apps/%name
%_kde3_iconsdir/*/*/apps/%name.png

%changelog
* Fri Mar 04 2011 Timur Aitov <timonbl4@altlinux.org> 0.82.3-alt3
- move to alternate place

* Mon May 25 2009 Motsyo Gennadi <drool@altlinux.ru> 0.82.3-alt2.1
- fix for automake-1.11

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 0.82.3-alt2
- delete post/postun scripts (new rpm)

* Fri Jul 11 2008 Motsyo Gennadi <drool@altlinux.ru> 0.82.3-alt1
- new version
- change URL

* Tue Jan 01 2008 Motsyo Gennadi <drool@altlinux.ru> 0.82.1-alt1
- new version

* Mon Jul 30 2007 Motsyo Gennadi <drool@altlinux.ru> 0.82-alt1
- initial build for Sisyphus

* Mon Jul 30 2007 Motsyo Gennadi <drool@altlinux.ru> 0.82-alt0.M40.1
- new version build for M40

* Sat Apr 14 2007 Motsyo Gennadi <drool@altlinux.ru> 0.67.5.3-alt0.M24.1
- initial build for ALM-2.4

* Thu Jun 29 2006 Pascal Bleser <guru@unixtech.be> 0.67.5.3-1
- new package

# Local Variables:
# mode: rpm-spec
# tab-width: 3
# End:
