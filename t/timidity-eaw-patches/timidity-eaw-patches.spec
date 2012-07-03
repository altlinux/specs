Name: timidity-eaw-patches
Version: 1.2
Release: alt2

%define title eawpats

Summary: Patch set for the timidity midi->wave converter/player
License: Free
Group: Sound

Url: http://www.stardate.bc.ca/eawpatches/html/default.htm
Source: http://madchat.org/music/%{title}12_full.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: timidity-instruments >= 1.0-alt1

%description
Eawpatches is the best GUS patch set for TiMidity++. Eawpatches is
maintained (tweaked and tuned) by Eric A Welsh.

%define customdocdir %_docdir/%name-%version

%install
mkdir -p %buildroot%_datadir/timidity
tar -jxvf %SOURCE0 -C %buildroot%_datadir/timidity/

# Creating eawpats.cfg
cat <<EOF > %buildroot%_datadir/timidity/%title.cfg
dir %_datadir/timidity/%title
source gravis.cfg
source gsdrums.cfg
source gssfx.cfg
source xgmap2.cfg
EOF

rm -rf %buildroot%_datadir/timidity/%title/{linuxconfig,winconfig}

# docs 
mkdir -p %buildroot%customdocdir
mv `find %buildroot%_datadir/timidity/%title -iname *.txt` %buildroot%customdocdir/

%define conf_string source %title.cfg
%define config %_sysconfdir/timidity.cfg

%post
if [ -f %config ]; then
        grep -qs '^%conf_string$' %config ||
        echo '%conf_string' >> %config
fi

%postun
[ $1 = 0 ] || exit 0
if [ -f %config ]; then
	sed '/%conf_string/d' < %config > %config.new
	mv %config.new %config
fi ||:

%triggerin -- TiMidity++
if [ -f %config ]; then
        grep -qs '^%conf_string$' %config ||
        echo '%conf_string' >> %config
fi

%triggerpostun -- %name < 1.1-alt2
[ $2 != 0 ] || exit 0
if [ -f %config ]; then
        grep -qs '^%conf_string$' %config ||
        echo '%conf_string' >> %config
fi

%files
%_datadir/timidity/%title/*
%_datadir/timidity/%title.cfg
%doc %customdocdir

%changelog
* Mon Dec 25 2006 Michael Shigorin <mike@altlinux.org> 1.2-alt2
- fixed requires
- minor spec cleanup

* Wed Nov 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2-alt1
- new version

* Fri May 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1-alt2
- Improvements in post* and trigger* sections. 

* Sun May 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1-alt1
- first build for Sisyphus.
