Name: botiktools
Version: 1.6.1
Release: alt2

Summary: Botik Tools is a collection of utilities for botik.ru users
License: BSD
Group: Communications

Url: http://www.botik.ru/~botik/tools
Source: %name-%version.tar.gz
Patch: botiktools-1.6.1-alt-desktop-file.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: %name-common = %version-%release
Requires: botik-key = %version-%release

# Automatically added by buildreq on Wed Jan 28 2009 (-bi)
BuildRequires: tk

BuildArch: noarch

%define botikdir %_datadir/%name

%description
Botik Tools is a collection of utilities for botik.ru users;
this is a metapackage to pull in all the subpackages

%package common
Summary: Shared code for Botik Tools
Group: System/Libraries
Requires: tclx tk

%description common
Shared code and images for Botik Tools

%package -n botik-key
Summary: Client-side authenticator for botik.ru WAN
Group: Communications
Requires: %name-common = %version-%release
Requires: tcllib

%description -n botik-key
This package provides Linux client for botik.ru password-based
LAN/internet access system

%prep
%setup
%patch -p1

%build
find -name '*.tcl' -o -name '*.txt' \
| while read i; do
	echo "recoding $i... "	# FIXME: comment with number sign in BotikMap.tcl
	iconv -f cp1251 -t utf-8 -rN < "$i" \
	| tr -d '\r' > _ \
	&& mv _ "$i"
done

%install
install -d %buildroot{%_bindir,%botikdir/{img,}}
install -pm644 *.tcl %buildroot%botikdir/
install -pm644 img/*.gif %buildroot%botikdir/img/
#install -pm755 linux/botik-key %buildroot%_bindir/botik-key
install -pDm644 linux/botik_key.png %buildroot%_pixmapsdir/botik_key.png
install -pDm644 linux/botik-key.desktop %buildroot%_desktopdir/botik-key.desktop

cat > %buildroot%_bindir/botik-key << EOF
#!/bin/sh
cd %botikdir
exec wish ./botikkey.tcl $@
EOF
chmod 755 %buildroot%_bindir/botik-key

%files

%files common
%doc doc/changelog doc/copyright
%botikdir/botikUts.tcl
%botikdir/botikHlp.tcl
%botikdir/report.tcl
%botikdir/net.tcl
%botikdir/img/next.gif
%botikdir/img/prev.gif
%botikdir/img/help.gif
%botikdir/img/yes.gif
%botikdir/img/yes_write.gif

%files -n botik-key
%_bindir/botik-key
%_pixmapsdir/botik_key.png
%_desktopdir/botik-key.desktop
%botikdir/img/botik_local.gif
%botikdir/img/botik_none.gif
%botikdir/img/botik_wait.gif
%botikdir/img/botik_world.gif
%botikdir/img/fig1.gif
%botikdir/img/GREEN.gif
%botikdir/img/GREEN_LOCAL.gif
%botikdir/img/logfile.gif
%botikdir/img/pswd_read.gif
%botikdir/img/pswd_write.gif
%botikdir/img/RED.gif
%botikdir/img/refresh.gif
%botikdir/img/setup.gif
%botikdir/img/no.gif
%botikdir/img/save_as.gif
%botikdir/img/stop.gif
%botikdir/img/YELLOW.gif
%botikdir/botikkey.tcl
%botikdir/bkClient.tcl
%botikdir/bkHelp.tcl
%botikdir/bkInit.tcl
%botikdir/bkLog.tcl
%botikdir/bkMWin.tcl
%botikdir/bkOptions.tcl
%botikdir/pswd2key.tcl

# TODO:
# - update source

%changelog
* Sat Oct 31 2009 Michael Shigorin <mike@altlinux.org> 1.6.1-alt2
- applied desktop file patch by icesik@

* Wed Jan 28 2009 Michael Shigorin <mike@altlinux.org> 1.6.1-alt1
- repackaged tarball
- use utf-8 from now on

* Wed Jan 28 2009 Michael Shigorin <mike@altlinux.org> 1.6-alt1
- built for ALT Linux
  + spec created from scratch using Debian packages for reference
