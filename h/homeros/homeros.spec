Name: homeros
Version: 20110527
Release: alt1
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildArch: noarch
License: GPL
Summary: The set of installing packages to prepare accessibility environment
URL: http://homeros.altlinux.org
Group: Accessibility

%package -n speech-default
Group: Sound
License: GPL
Summary: Installs VoiceMan speech server with default set of speech synthesizers
Requires: voiceman voiceman-server voiceman-tools espeak ru_tts RHVoice

%package emacspeak
Group: Accessibility
License: GPL
Summary: Installs accessible environment based on emacspeak audio desktop
Requires: speech-default
Requires: etcskel-homeros homeros-tools homeros-media homeros-emacs-menu emacs-easypim yasr
Requires: emacs23-X11-athena emacspeak emacs23-gnus w3m emacs-w3m

%package orca
Group: Accessibility
License: GPL
Summary: Installs accessible environment based on GNOME and Orca screen reader
Requires: speech-default
Requires: etcskel-homeros homeros-tools homeros-media yasr
#FIXME: openoffice or libreoffice
Requires: orca firefox firefox-ru

%description
The set of installing packages to prepare accessible 
environment for blind people.

%description -n speech-default
This package installs set of utils to enable speech output. After
installation user must call voiceman-enable for every speech
synthesizer he want to use (list of all available synthesizers can be
obtained with voiceman-available command) and than start the server
with command "service voiceman start".

%description emacspeak
This package installs accessible environment for blind people based on emacspeak audio desktop.
It also prepares general Homeros-specific instruments.

%description orca
This package installs accessible environment for blind people based on GNOME and Orca.
It also prepares general Homeros-specific instruments.

%files -n speech-default
%files emacspeak
%files orca

%changelog
* Fri May 27 2011 Michael Pozhidaev <msp@altlinux.ru> 20110527-alt1
- Remove dependencies to gnome-default and gnome-a11y from homeros-orca package (by aris@ ask)

* Tue Apr 05 2011 Michael Pozhidaev <msp@altlinux.ru> 20110405-alt1
- Added speech-default subpackage

* Sat Jan 08 2011 Michael Pozhidaev <msp@altlinux.ru> 20110108-alt1
- Removed dependency to openoffice.org
- General clean up

* Fri Oct 24 2008 Michael Pozhidaev <msp@altlinux.ru> 20081024-alt1
- Initial RPM

