%def_with libtool15
%define _emacspeakdir %_emacslispdir/%name

Name: emacspeak
Version: 35.0
Release: alt2

License: GPL
Group: Accessibility
Summary: emacspeak - The Complete Audio Desktop with GNU/Emacs
Url: http://emacspeak.sourceforge.net
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>

Requires: emacs-common emacsen-startscripts emacs-gnus voiceman

BuildRequires: emacs-devel emacs23-common emacs23-leim emacs23-gnus
BuildRequires: gcc-c++
BuildRequires: tcl-devel
BuildRequires: perl-libwww perl-HTML-TableExtract
BuildRequires: libalsa-devel libespeak-devel
%if_with libtool15
BuildRequires: libtool_1.5
%endif

Source: %name-%version.tar.gz
Source1: site-start.el
Source2: profile.sh
Source3: %name-script

Patch1: emacspeak-34.0-alt.patch
Patch2: emacspeak-34.0-alt-cyrillic.patch
Patch3: emacspeak-34.0-alt-unspeakable.patch
Patch4: emacspeak-34.0-alt-shell-command-output.patch

%package servers
Group: Accessibility
Summary: Speech servers for the emacspeak
Requires: %name = %version-%release

%description
Emacspeak is a speech interface that allows visually impaired users to
interact independently and efficiently with the computer. Available free of
cost on the Internet, Emacspeak has dramatically changed how the author and
hundreds of blind and visually impaired users around the world interact with
the personal computer and the Internet. A rich suite of task-oriented
speech-enabled tools provides efficient speech-enabled access to the evolving
semantic WWW. When combined with Linux running on low-cost PC hardware,
Emacspeak/Linux provides a reliable, stable speech-friendly solution that
opens up the Internet to visually impaired users around the world. 

%description servers
The espeak and outloud speech servers for %name from its original distribution.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%__subst 's:\$servers/linux-espeak:%_libdir/%name/linux-espeak:' servers/espeak
%__subst 's:\$servers/linux-outloud:%_libdir/%name/linux-outloud:' servers/outloud

%build
%if_with libtool15
export LIBTOOL_VERSION=1.5
%endif
make config SRC=`pwd`
make emacspeak prefix=%_prefix
cd servers/linux-outloud
make
cd ../linux-espeak
make
cd ../..
cd info
make info
make htm
cd ..

%install
make prefix=%buildroot%prefix install

#Config file installation;
%__install -d -m755 %buildroot%_emacs_sitestart_dir
%__install -pD -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/emacspeak.el
%__install -pD -m 755 %SOURCE2 %buildroot/%_sysconfdir/profile.d/emacspeak.sh

#Speech servers;
%__install -d -m755 %buildroot%_libdir/%name
%__install -pD -m644 servers/linux-espeak/tclespeak.so %buildroot%_libdir/%name/linux-espeak/tclespeak.so
%__install -d -m755 %buildroot%_libdir/%name/linux-outloud
%__cp \
servers/linux-outloud/ALSA \
servers/linux-outloud/asoundrc \
servers/linux-outloud/atcleci.so \
servers/linux-outloud/eci.ini \
servers/linux-outloud/VIAVOICE \
%buildroot%_libdir/%name/linux-outloud/
%__rm -rf %buildroot%_emacspeakdir/servers
%__mkdir -p %buildroot%_emacspeakdir/servers

cat <<EOF > %buildroot%_emacspeakdir/servers/.servers
espeak
outloud
EOF

%__cp servers/espeak servers/outloud %buildroot%_emacspeakdir/servers/

# remove unneeded files
%__rm -rf %buildroot%_emacslispdir/emacspeak/user-guide
%__rm -rf %buildroot%_emacslispdir/emacspeak/install-guide
%__rm %buildroot%_emacslispdir/emacspeak/etc/NEWS*
%__rm %buildroot%_emacslispdir/emacspeak/etc/*.html
%__rm %buildroot%_emacslispdir/emacspeak/etc/emacspeak.*
%__rm %buildroot%_emacslispdir/emacspeak/etc/FAQ
%__rm %buildroot%_emacslispdir/emacspeak/etc/HELP
%__rm %buildroot%_emacslispdir/emacspeak/etc/COPYRIGHT
%__subst 's!%buildroot!!' %buildroot/usr/bin/emacspeak

# Removing since it uses rsh in script;
%__rm -f %buildroot%_emacspeakdir/etc/remote.txt
%__rm -f %buildroot%_emacspeakdir/servers/remote-tcl

%__install -pD -m755 %SOURCE3 %buildroot%_bindir/%name

%files
%doc install-guide user-guide info/html
%doc etc/NEWS* etc/*.html etc/emacspeak.* etc/FAQ etc/HELP etc/COPYRIGHT
%_bindir/*
%config(noreplace) %_emacs_sitestart_dir/*
%config %_sysconfdir/profile.d/*
%dir %_emacspeakdir
%_emacspeakdir/etc
%_emacspeakdir/js
%_emacspeakdir/lisp
%_emacspeakdir/realaudio
#%_emacspeakdir/sawfish
%_emacspeakdir/shoutcast
%_emacspeakdir/sounds 
%_emacspeakdir/xsl
%dir %_emacspeakdir/servers
%_emacspeakdir/servers/.servers
%_infodir/*

%files servers
%_emacspeakdir/servers/espeak
%_emacspeakdir/servers/outloud
%_libdir/%name

%changelog
* Sun Nov 27 2011 Michael Pozhidaev <msp@altlinux.ru> 35.0-alt2
- Fixed shell commands output processing

* Sat Nov 26 2011 Michael Pozhidaev <msp@altlinux.ru> 35.0-alt1
- New version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 34.0-alt3.1
- Rebuild with Python-2.7

* Sat May 21 2011 Michael Pozhidaev <msp@altlinux.ru> 34.0-alt3
- Fixed problem with silence on shell commands in dired

* Mon May 16 2011 Michael Pozhidaev <msp@altlinux.ru> 34.0-alt2
- Fixed rules for unspeakable lines (Thanks to Dmitri Paduchikh)

* Sat May 14 2011 Michael Pozhidaev <msp@altlinux.ru> 34.0-alt1
- New version

* Mon May 09 2011 Michael Pozhidaev <msp@altlinux.ru> 33.0-alt3
- General package clean up

* Tue Dec 21 2010 Michael Pozhidaev <msp@altlinux.ru> 33.0-alt2
- Fixed cyrillic characters processing

* Thu Dec 16 2010 Michael Pozhidaev <msp@altlinux.ru> 33.0-alt1
- Update to 33.0

* Sat Jan 02 2010 Michael Pozhidaev <msp@altlinux.ru> 31.0-alt1
- New version
- Speech servers espeak and outloud moved into separate package

* Tue Jul 28 2009 Michael Pozhidaev <msp@altlinux.ru> 30.0-alt1
- New version: 30.0

* Fri Jul 24 2009 Michael Pozhidaev <msp@altlinux.ru> 26.0-alt5
- Removed linux-outloud compilation because of libtool using problem (subject to fix in 30.0)

* Wed Dec 17 2008 Michael Pozhidaev <msp@altlinux.ru> 26.0-alt4
- Removed scripts with rsh calls (by ldv@ ask)

* Sat Aug 02 2008 Michael Pozhidaev <msp@altlinux.ru> 26.0-alt3
- Changed voiceman client file name 

* Tue Jul 15 2008 Michael Pozhidaev <msp@altlinux.ru> 26.0-alt2
- Added enable-emacspeak script and added some customizations

* Wed Sep 26 2007 Michael Pozhidaev <msp@altlinux.ru> 26.0-alt1
- Some bug fixes and readme file was added

* Mon Sep 24 2007 Michael Pozhidaev <msp@altlinux.ru> 26.0-alt0.5
- Preliminary release of new version

* Mon Dec 19 2005 Igor Vlasenko <viy@altlinux.ru> 23.0-alt1
- new version

* Sat Feb 21 2004 Ott Alex <ott@altlinux.ru> 19.0-alt2
- Fix gcc3.3 build

* Sat Dec 13 2003 Ott Alex <ott@altlinux.ru> 19.0-alt1
- New version

* Tue Sep 23 2003 Ott Alex <ott@altlinux.ru> 18.0-alt3
- Fixing spec deps 

* Mon Jun 02 2003 Ott Alex <ott@altlinux.ru> 18.0-alt2
- Fixing load of emacs modules

* Sun May 18 2003 Ott Alex <ott@altlinux.ru> 18.0-alt1
- Initial build
