Version:	0.5.2
Name:		quassel
Release:	alt1
Summary:	Quassel - IRC client
License: 	GPLv3
Group: 		Networking/IRC
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://www.quassel-irc.org/
Source0:	http://www.quassel-irc.org/pub/%name-%version.tar.bz2

# Automatically added by buildreq on Wed May 20 2009 (-bi)
BuildRequires: cmake gcc-c++ libqt4-devel

%description
Quassel IRC is a modern, cross-platform, distributed IRC client based on the Qt4 framework.
Distributed means that one (or multiple) client(s) can attach to and detach from a central
core that stays permanently online -- much like the popular combination of screen and a
text-based IRC client such as WeeChat, and similar to (but much more featureful than) so-called BNCs.
Re-attaching your client will show your IRC session in the same state as you left it in
(plus whatever happened while you were gone), and this even when you re-attach from a different
location. In addition, Quassel IRC can be used like a traditional client, with providing both
client and core functionality in one binary. An optional Beginner's Mode completely hides
this feature, so Quassel IRC can be setup very easily.

%prep
%setup -q

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"

%install
%make DESTDIR=%buildroot install
cp -rf icons/hicolor %buildroot%_iconsdir/

%files
%dir %_datadir/apps/%name
%_bindir/*
%_datadir/apps/%name
%_desktopdir/*.desktop
%_iconsdir/*/*/apps/%name.png

%changelog
* Sat Apr 10 2010 Motsyo Gennadi <drool@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Wed Nov 18 2009 Motsyo Gennadi <drool@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Wed May 20 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1
- initial build for ALT Linux
