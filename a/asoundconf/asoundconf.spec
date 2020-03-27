Summary: utility to read and change the user's ALSA library configuration
Epoch: 1
Name: asoundconf
Version: 1.2
Release: alt1
Packager: Igor Vlasenko <viy@altlinux.ru>
License: GPLv2+
Group: Sound
# OLDURL: https://code.launchpad.net/~motu/asoundconf-ui
# OLDURL: https://code.launchpad.net/asoundconf-ui
# (patches) https://git.archlinux.org/svntogit/community.git/tree/trunk?h=packages/asoundconf
# https://git.archlinux.org/svntogit/community.git/tree/trunk?h=packages/asoundconf
Requires: alsa-utils
BuildRequires: rpm-build-python3
Source0: %name-%version.tar
BuildArch: noarch

Patch1: 0001-python3-syntax.patch
Patch2: 0002-python3-spaces.patch
Patch3: 0003-python3-gobject.patch

%description
Command-line Python utility to configure a user's alsa-lib asoundrc
 Useful if you have two cards, and switch between the two.
 There is already this functionality in GNOME, but this is
 indeed useful if you do not use that desktop environment,
 and asoundconf also supports PulseAudio toggling.

%package gtk
Summary: gtk utility to read and change the user's ALSA library configuration
Group: Sound
Requires: asoundconf = %EVR

%description gtk
Based on asoundconf code, but as a GTK+ front-end.
 Useful if you have two cards, and switch between the two.
 There is already this functionality in GNOME, but this is
 indeed useful if you do not use that desktop environment,
 and asoundconf-gtk also supports PulseAudio toggling.


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

#sed -i 1s,python,python3, asoundconf

%build
%python3_build


%install
%python3_install

#install -d %buildroot%_bindir
#install -m755 asoundconf %buildroot%_bindir/

# installing debian man pages
#install -d %buildroot%_man1dir
#install -m644 asoundconf.1 %buildroot%_man1dir/

#install -d %buildroot%_bindir
#install -m755 asoundconf-gtk/asoundconf-gtk %buildroot%_bindir/

# installing debian man pages
#install -d %buildroot%_man8dir
#install -m644 debian/asoundconf-gtk.8 %buildroot%_man8dir/

#install -d %buildroot%_desktopdir
#install -m644 asoundconf-gtk.desktop %buildroot%_desktopdir/

%files gtk
%_bindir/asoundconf-gtk
#%_man8dir/asoundconf-gtk.8*
%_desktopdir/asoundconf-gtk.desktop

%files
%_bindir/asoundconf
%_man1dir/asoundconf.1*
%python3_sitelibdir/*

%changelog
* Fri Mar 27 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.2-alt1
- new version
- merged asoundconf-gtk
- python3 build

* Sat Dec 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2
- fixed build

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- synced changes from aur.archlinux.org/packages/asoundconf (1.0.1-3)
  (see also http://wiki.marklesh.com/How-to/Asoundconf)
- (closes: #29795)

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.bzr8-alt1.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.bzr8-alt1.1
- Rebuilt with python 2.6

* Wed Jan 28 2009 Igor Vlasenko <viy@altlinux.ru> 0.0.bzr8-alt1
- initial build

