%define jog_name	jogdiald
%define jog_confdir	%_sysconfdir/%jog_name

Name: vaio-tools
Version: 0.0.1
Release: alt8.3

Summary: Tools for Sony Vaio Notebooks
License: GPL
Group: System/Configuration/Hardware

Packager: Fr. Br. George <george@altlinux.ru>
Source: %jog_name-0.2.4.tar.bz2
Source1: %jog_name-plugins.tar.bz2
Source2: spicctrl-1.2.tar.bz2
Source3: atitvout-0.4.tar.bz2
Source4: sonypid.tar.bz2
Source5: atitvout-0.4-alt-lrmi.patch

# This looks like upstart script, but it's better to keep it here
%add_findreq_skiplist %jog_confdir/irda

# Automatically added by buildreq on Wed Dec 10 2008
BuildRequires: libX11-devel libXext-devel libXtst-devel xorg-inputproto-devel libXi-devel

ExclusiveArch: %ix86

%description
Some tools for Sony Vaio notebooks:
- control jog dial
- change brightness
- change output (tv/ext monitor/lcd)

%prep
%setup -c
for i in %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4; do
	tar xjvf $i
done
pushd atitvout
	patch -p1 < %SOURCE5
popd

%build
for i in %jog_name-0.2.4 spicctrl-1.2 atitvout sonypid; do
	%make_build -C $i
done

%install
mkdir -p %buildroot/{%_bindir,%jog_confdir,%_man1dir}
cp -a %jog_name-plugins/* %buildroot/%jog_confdir/
install -m 0755 %jog_name-[0-9]*/%jog_name %buildroot/%_bindir/
install -m 0755 spicctrl-[0-9]*/spicctrl %buildroot/%_bindir/
install -m 0644 spicctrl-[0-9]*/spicctrl.1 %buildroot/%_man1dir/
install -m 0755 atitvout/atitvout %buildroot/%_bindir/
install -m 0755 sonypid/sonypid %buildroot/%_bindir/

mkdir -p docs/{atitvout,%jog_name}
cp -a atitvout/{COPYING,HARDWARE,README,mails,test.sh} docs/atitvout/
cp -a %jog_name-[0-9]*/{AUTHORS,CHANGES,README*} docs/%jog_name/

%files
%doc docs/*
%dir %jog_confdir
%config %jog_confdir/*
%_bindir/*
%_man1dir/*

%changelog
* Sun Apr 11 2010 Michael Shigorin <mike@altlinux.org> 0.0.1-alt8.3
- fixed build (added BR)

* Wed Dec 17 2008 Fr. Br. George <george@altlinux.ru> 0.0.1-alt8.2
- Remove upstart dependency

* Wed Dec 10 2008 Michael Shigorin <mike@altlinux.org> 0.0.1-alt8.1
- fixed FTBFS:
  + lrmi patch for atitvout
  + buildreq
- spec cleanup

* Tue Mar 06 2007 Grigory Milev <week@altlinux.ru> 0.0.1-alt8
- no updates found, only spec clean up

* Mon Feb 05 2007 Michael Shigorin <mike@altlinux.org> 0.0.1-alt7
- ExclusiveArch: %%ix86 due to atitvout VM86 asm

* Mon Feb 05 2007 Michael Shigorin <mike@altlinux.org> 0.0.1-alt6
- picked up an orphan
- fix build (update buildrequires)
- spec cleanup
- added Packager:
  + I don't own any Vaios, proper maintainer wanted
    (no sources updated)

* Fri Nov 15 2002 Grigory Milev <week@altlinux.ru> 0.0.1-alt5
- rebuild with gcc3.2
- minor spec cleanup

* Thu Sep 19 2002 Grigory Milev <week@altlinux.ru> 0.0.1-alt4
- update atitvout to version 0.4

* Wed Jul 10 2002 Grigory Milev <week@altlinux.ru> 0.0.1-alt3
- update atitvout to version 0.3

* Wed Jul 10 2002 Grigory Milev <week@altlinux.ru> 0.0.1-alt2
- corrected permitions for jogdiald plugins

* Wed Jul 10 2002 Grigory Milev <week@altlinux.ru> 0.0.1-alt1
- Initial build for ALT Linux distribution.
