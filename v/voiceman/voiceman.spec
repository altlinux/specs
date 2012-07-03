Name: voiceman
Version: 1.5.0.1
Release: alt1

Packager: Michael Pozhidaev <msp@altlinux.ru>
License: %gpl3plus
URL: http://www.marigostra.ru/voiceman/

Summary: Universal server for processing speech output
Group: Sound

Source: %name-%version.tar.gz
Source1: %name
Source2: %name.conf

BuildRequires: rpm-build-licenses gcc-c++ libao-devel

%package server
Summary: The VoiceMan server
Group: Sound
Requires: iconv libao aplay 

%package -n libvmclient-devel
BuildArch: noarch
Summary: C/C++ development files for producing speech output with voicemand
Group: Development/C
Requires: libvmclient-devel-static

%package -n libvmclient-devel-static
Summary: The static library for libvmclient
Group: Development/C

%description
VoiceMan is the speech processing daemon designed to collect output
from screen reading software used by blind users in one central place
and translate it into speech with configured set of speech
synthesizers. Developing process was launched in 2003. The general
idea at the initial stage was creation flexible tool for automatic
switching between Russian and English TTSes based on cyrillic
character sequences analyzing. During the developing process goals
were extended and some new features were included like configuration
simplification, voice family switching and some general text
preprocessing.

%description server
This package contains daemon binary files to launch VoiceMan 
server on your computer. It is necessary if you want to process speech output locally.

%description -n libvmclient-devel
This package contains files used for developing applications with C/C++ language
and necessary to make connections with VoiceMan daemon.

%description -n libvmclient-devel-static
This package contains library used for static linking of libvmclient.

%prep
%setup -q
%build
%configure default_socket=/var/run/voiceman.socket
%make_build

%install
make DESTDIR=%buildroot install 

%__rm -f %buildroot%_sysconfdir/%name.conf
%__install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/%name.conf
%__install -pD -m755 %SOURCE1 %buildroot%_sysconfdir/rc.d/init.d/%name

%__install -d -m755 %buildroot%_sysconfdir/%name.d
%__install -d -m755 %buildroot%_datadir/sounds/%name

%__install -pD -m644 ./libvmclient/vmclient.h %buildroot%_includedir/vmclient/vmclient.h
%__install -pD -m644 ./libvmclient/libvmclient.a %buildroot%_libdir/libvmclient.a

for i in espeak ru_tts mbrola; do
%__rm -f %buildroot%_datadir/%name/replacements.$i
done

%preun server
%preun_service %name

%files
%_bindir/%name
%_bindir/%name-emacspeak
%_datadir/sounds/%name

%files server
%doc AUTHOR COPYING README ChangeLog NEWS THANKS
%_bindir/voicemand
%_bindir/%name-trim
%_bindir/%name-executor
%_bindir/%name-reload
%config(noreplace) %_sysconfdir/%name.conf
%_sysconfdir/%name.d
%_sysconfdir/rc.d/init.d/%name
%_datadir/%name

%files -n libvmclient-devel
%doc examples/libvmclient-api/example1.c examples/libvmclient-api/example2.c examples/libvmclient-api/example3.c examples/libvmclient-api/makefile
%_includedir/*

%files -n libvmclient-devel-static
%_libdir/libvmclient.a

%changelog
* Tue May 17 2011 Michael Pozhidaev <msp@altlinux.ru> 1.5.0.1-alt1
- New version

* Wed Mar 09 2011 Michael Pozhidaev <msp@altlinux.ru> 1.5.0-alt4
- Used exact library file name for _libdir

* Mon Dec 20 2010 Michael Pozhidaev <msp@altlinux.ru> 1.5.0-alt3
- Reload service operation now uses voiceman-reload utility

* Wed Oct 06 2010 Michael Pozhidaev <msp@altlinux.ru> 1.5.0-alt2
- Removed debugging information from binary files

* Tue Oct 05 2010 Michael Pozhidaev <msp@altlinux.ru> 1.5.0-alt1
- Updated to 1.5.0 release version

* Tue Jun 29 2010 Michael Pozhidaev <msp@altlinux.ru> 1.5.0-alt0.2
- Removed temporary voiceman-espeak symlink

* Tue Jun 29 2010 Michael Pozhidaev <msp@altlinux.ru> 1.5.0-alt0.1
- Update to 1.5.0pre4

* Wed Jul 01 2009 Michael Pozhidaev <msp@altlinux.ru> 1.2.0pre3-alt3
- Added errno.h to trim.cpp (gcc4.4 fix)

* Thu Nov 06 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0pre3-alt2
- Added -fpic to libvmclient.a

* Sun Oct 26 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0pre3-alt1
- Bugs fixes

* Thu Sep 04 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0pre2-alt1
- Added config and test to the init.d script
- Added --stop command to shell client

* Mon Aug 11 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0pre1-alt1
- Default configuration changed to mbrola+ru_tts
- emacspeak client renamed to voiceman-espeak
- package was splitted onto voiceman and voiceman-server
- fixed building scripts

* Wed Sep 26 2007 Michael Pozhidaev <msp@altlinux.ru> 1.1.0-alt3
- Fixed directory ownership

* Sun Sep 23 2007 Michael Pozhidaev <msp@altlinux.ru> 1.1.0-alt2
- Fixed bug with system directories ownership and added alsa output support

* Tue Jul 24 2007 Michael Pozhidaev <msp@altlinux.ru> 1.1.0pre1-alt0.1
- Removed boost dependences

* Thu Apr 26 2007 Michael Pozhidaev <msp@altlinux.org> 1.0.0-alt2
- Added package dependences

* Tue Apr 17 2007 Michael Pozhidaev <msp@altlinux.org> 1.0.0-alt1
- First stable release

* Mon Mar 26 2007 Michael Pozhidaev <msp@altlinux.org> 1.0.0-alt0.22
- initial publicated rpm
