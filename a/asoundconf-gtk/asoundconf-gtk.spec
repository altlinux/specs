Summary: Applet to select the default ALSA sound card
Name: asoundconf-gtk
Version: 1.6
Release: alt1.1.1
Packager: Igor Vlasenko <viy@altlinux.ru>
License: GPL
Group: Sound
URL: https://code.launchpad.net/asoundconf-ui
Requires: asoundconf
BuildRequires: rpm-build-python
#http://packages.ubuntu.com/ru/source/gutsy/asoundconf-gtk
Source0: %name-%version.tar
Patch0: asoundconf-gtk_1.6-0ubuntu1.diff.gz
BuildArch: noarch

%description
Based on asoundconf code, but as a GTK+ front-end.
 Useful if you have two cards, and switch between the two.
 There is already this functionality in GNOME, but this is
 indeed useful if you do not use that desktop environment,
 and asoundconf-gtk also supports PulseAudio toggling.

%prep
%setup -q
%patch0 -p1

%build

%install
install -d ${RPM_BUILD_ROOT}%_bindir
install -m755 asoundconf-gtk/asoundconf-gtk ${RPM_BUILD_ROOT}%_bindir/

# installing debian man pages
install -d ${RPM_BUILD_ROOT}%_man8dir
install -m644 debian/asoundconf-gtk.8 ${RPM_BUILD_ROOT}%_man8dir/

install -d ${RPM_BUILD_ROOT}%_desktopdir
install -m644 asoundconf-gtk.desktop ${RPM_BUILD_ROOT}%_desktopdir/

%files 
%_bindir/asoundconf-gtk
%_man8dir/asoundconf-gtk.8*
%_desktopdir/asoundconf-gtk.desktop

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt1.1.1
- Rebuild with Python-2.7

* Mon Dec 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.1
- Rebuilt with python 2.6

* Wed Jan 28 2009 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1
- first build

