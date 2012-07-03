%define origname cdparanoia-plugin

Name: xmms-in-cdparanoia
Version: 0.1
Release: alt3

Summary: Digital CD playback plugin for XMMS
License: GPL
Group: Sound

# host not found
Url: http://www02.u-page.so-net.ne.jp/ca2/kzmi/xmms/
Source: %origname-%version.tar.bz2

Requires: xmms

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Thu May 15 2008
BuildRequires: libcdparanoia-devel libxmms-devel

%description
This plugin reads CDDA sectors and passes them to XMMS directly. That
way you don't need a cable from the CD-ROM to the sound card and you
can use the usual effect and visualization plugins.

%prep
%setup -q -n %origname-%version

%build
unset CC CXX
%configure
%make

%install
install -pD -m755 Input/cdparanoia/.libs/libcdparanoia.so \
	%buildroot%xmms_inputdir/libcdparanoia.so

%files
%doc README
%xmms_inputdir/*.so

%changelog
* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 0.1-alt3
- add Packager tag
- buildreq

* Tue Nov 14 2006 Igor Zubkov <icesik@altlinux.org> 0.1-alt2
- NMU
- fix rebuild by removing mawk from buildreqs
- buildreq

* Mon Jan 19 2004 Michael Shigorin <mike@altlinux.ru> 0.1-alt1
- built for ALT Linux
- spec cleanup

* Wed Jun  4 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1-4mdk
- fix buildrequires
- fix build

* Wed Mar 12 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1-3mdk
- fix buildrequires

* Fri Dec 27 2002 Götz Waschk <waschk@linux-mandrake.com> 0.1-2mdk
- clean unpackaged file

* Mon Oct 14 2002 Götz Waschk <waschk@linux-mandrake.com> 0.1-1mdk
- initial package
