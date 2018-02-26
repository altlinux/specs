Name: magicor
Version: 1.1
Release: alt1.1
Summary: Push ice blocks around to extenguish all fires
Group: Games/Puzzles
License: Public Domain
Url: http://magicor.sourceforge.net/
Source0: http://downloads.sourceforge.net/%name/%name-source-%version.tar.gz
Source1: http://downloads.sourceforge.net/%name/%name-data-%version.tar.gz
Source2: %name.desktop
Source3: %name.png
Packager: Fr. Br. George <george@altlinux.ru>

BuildArch: noarch

%description
The goal of the game is to annihilate all burning fires. You do this
by pushing blocks of ice until they collide with a burning fire.
When the ice blocks hit burning fire the block and the fire are destroyed.
Once all fires are extinguished the level is completed.

%prep
%setup -q -b 1
sed -i 's:###CONFIG_PATH###:%_sysconfdir/%name.conf:' *.py
sed -i 's:###SHARE_PATH###:%_datadir/%name:' etc/*.conf

%build
# nothing to build, python code + data only

%install
# We must do a DIY install as the makefile doesn't support installing into
# an install root
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%python_sitelibdir/%name
mkdir -p %buildroot%_datadir/%name
install -m 644 etc/*.conf %buildroot%_sysconfdir
install -D -m 755 Magicor.py %buildroot%_bindir/magicor
install -m 755 Magicor-LevelEditor.py %buildroot%_bindir/magicor-editor
cp -fr magicor/* %buildroot%python_sitelibdir/%name
cp -fr data/* %buildroot%_datadir/%name

# below is the desktop file and icon stuff.
install -D  %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -D -p -m 644 %SOURCE3 %buildroot%_liconsdir/%name.png

%files
%doc LICENSE README
%config(noreplace) %_sysconfdir/%{name}*.conf
%_bindir/%{name}*
%python_sitelibdir/%name
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/48x48/apps/%name.png

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1
- Rebuild with Python-2.7

* Sun Jan 17 2010 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Initial build from FC

* Thu Jan  7 2010 Hans de Goede <hdegoede@redhat.com> - 1.1-5
- Change python_sitelib macro to use %%global as the new rpm will break
  using %%define here, see:
  https://www.redhat.com/archives/fedora-devel-list/2010-January/msg00093.html

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-2
- Rebuild for Python 2.6

* Wed Jul  9 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-1
- New upstream release 1.1

* Wed Dec 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.1-0.1.rc1
- New upstream release 1.1-rc1
- Add python as BuildRequires so that %%python_sitelib gets expanded properly,
  this fixes magicor not working at all atm (bz 421211)

* Thu Dec 14 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.0-0.3.rc2
- Rebuild for new Python

* Fri Nov 24 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-0.2.rc2
- New upstream release 1.0-rc2

* Thu Nov  2 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-0.1.rc1
- New upstream release 1.0-rc1

* Sat Oct 21 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1-2
- Mark /etc/magicor.conf %%config(noreplace)

* Sat Oct 14 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1-1
- Initial Fedora Extras package
