%def_disable emacspeak

Name: homeros
Version: 20130412
Release: alt2
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildArch: noarch
License: GPL
Summary: The set of metapackages for Homeros installation
URL: http://homeros.altlinux.org
Group: Accessibility

%package -n speech-default
Group: Sound
License: GPL
Summary: Installs default speech output engines
Requires: voiceman voiceman-server voiceman-tools espeak RHVoice

%if_enabled emacspeak
%package emacspeak
Group: Accessibility
License: GPL
Summary: Installs emacspeak accessible environment for blind users
Requires: speech-default yasr
Requires: homeros-core homeros-emacs
Requires: emacs-nox emacspeak emacs24-gnus w3m emacs-w3m
%endif

%package orca
Group: Accessibility
License: GPL
Summary: Installs accessible environment based on GNOME and Orca screen reader
Requires: speech-default yasr
Requires: homeros-core
#FIXME: openoffice or libreoffice
#Requires: orca firefox firefox-ru

%description
The set of metapackages to prepare accessible 
environment for blind users.

%description -n speech-default
This package installs the set of utils to enable speech output. After
installation user must call voiceman-enable for each speech
synthesizer he wants to use (list of all available synthesizers can be
obtained with voiceman-available command). After that the server should be launched 
with "service voiceman start" command.

%if_enabled emacsspeak
%description emacspeak
This package installs accessible environment for blind people based on emacspeak audio desktop.
It also prepares general speech output.
%endif

%description orca
This package installs accessible environment for blind people based on GNOME and Orca.
(currently unmaintained)

%files -n speech-default
%if_enabled emacspeak
%files emacspeak
%endif
%files orca

%changelog
* Mon Mar 27 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 20130412-alt2
- Rebuilt without emacspeak

* Fri Apr 12 2013 Michael Pozhidaev <msp@altlinux.ru> 20130412-alt1
- The sets of required packages are updated to reflect changes in homeros-core package

* Wed Jul 18 2012 Michael Pozhidaev <msp@altlinux.ru> 20120718-alt1
- emacs23 req changed to emacs-nox
- ru_tts removed from speech-default
- Textlus added to speech-default
- emacs-easypim removed from emacspeak subpackage

* Fri May 27 2011 Michael Pozhidaev <msp@altlinux.ru> 20110527-alt1
- Remove dependencies to gnome-default and gnome-a11y from homeros-orca package (by aris@ ask)

* Tue Apr 05 2011 Michael Pozhidaev <msp@altlinux.ru> 20110405-alt1
- Added speech-default subpackage

* Sat Jan 08 2011 Michael Pozhidaev <msp@altlinux.ru> 20110108-alt1
- Removed dependency to openoffice.org
- General clean up

* Fri Oct 24 2008 Michael Pozhidaev <msp@altlinux.ru> 20081024-alt1
- Initial RPM

