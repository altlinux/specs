Summary: Command-line Python utility to select the default ALSA sound card
Name: asoundconf
Version: 0.0.bzr8
Release: alt1.1.1
Packager: Igor Vlasenko <viy@altlinux.ru>
License: GPL
Group: Sound
URL: https://code.launchpad.net/~motu/asoundconf-ui
# rev 8 of http://bazaar.launchpad.net/~crimsun/asoundconf-ui/asoundconf-trunk

Requires: alsa-utils
BuildRequires: rpm-build-python
Source0: %name-%version.tar
BuildArch: noarch

%description
Command-line Python utility to configure a user's alsa-lib asoundrc
 Useful if you have two cards, and switch between the two.
 There is already this functionality in GNOME, but this is
 indeed useful if you do not use that desktop environment,
 and asoundconf also supports PulseAudio toggling.

It is part of Ubnutu's alsa-utils package.

%prep
%setup -q

%build

%install
install -d ${RPM_BUILD_ROOT}%_bindir
install -m755 asoundconf ${RPM_BUILD_ROOT}%_bindir/

# installing debian man pages
install -d ${RPM_BUILD_ROOT}%_man1dir
install -m644 asoundconf.1 ${RPM_BUILD_ROOT}%_man1dir/

%files 
%_bindir/asoundconf
%_man1dir/asoundconf.1*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.bzr8-alt1.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.bzr8-alt1.1
- Rebuilt with python 2.6

* Wed Jan 28 2009 Igor Vlasenko <viy@altlinux.ru> 0.0.bzr8-alt1
- initial build

