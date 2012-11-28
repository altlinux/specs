# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-gettextize pkgconfig(gtk+-2.0) python-devel
# END SourceDeps(oneline)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary: Constructionist learning platform
Name: sugar
Version: 0.96.1
Release: alt1_2
URL: http://sugarlabs.org/
License: GPLv2+
Group: Graphical desktop/Sugar
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.bz2
Patch0: sugar-gnomekeyring.patch

BuildRequires: gettext
BuildRequires: libGConf-devel
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: perl-XML-Parser
BuildRequires: python-module-pygtk-devel

Requires: dbus-tools-gui
Requires: ethtool
Requires: pam_gnome-keyring
Requires: gnome-python2-gconf
Requires: python-module-pygnome-wnck
Requires: gst-plugins-espeak
Requires: python-module-gst
Requires: metacity
Requires: NetworkManager
Requires: openssh
Requires: python-module-pygtksourceview
Requires: python-module-telepathy
Requires: python-module-xklavier
Requires: sugar-artwork
Requires: sugar-toolkit
Requires: sugar-toolkit-gtk3
Requires: telepathy-mission-control
Requires: upower
Requires: xdg-user-dirs
Requires: gvfs

BuildArch: noarch
Source44: import.info
Patch33: sugar-0.88.0-sugar-start-script.patch

%description
Sugar provides simple yet powerful means of engaging young children in the 
world of learning that is opened up by computers and the Internet. With Sugar,
even the youngest learner will quickly become proficient in using the 
computer as a tool to engage in authentic problem-solving.  Sugar promotes 
sharing, collaborative learning, and reflection, developing skills that help 
them in all aspects of life. 

Sugar is also the learning environment for the One Laptop Per Child project. 
See http://www.laptop.org for more information on this project.

%package emulator
Summary: The emulator for the Sugar Learning Platform
Group: Graphical desktop/Sugar
Requires: %{name} = %{version}-%{release}
Requires: xorg-xephyr
# for xdpyinfo
Requires: xorg-x11-utils

%description emulator
The emulator let's you test and debug sugar. For example it allows you to run 
multiple instances of sugar. 

%prep
%setup -q
%patch0 -p1 -b .keyring
%patch33 -p1

%build
%configure
make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=%{buildroot}
mkdir %{buildroot}/%{_datadir}/sugar/activities
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%find_lang %{name}

install -d -m 0755 %{buildroot}/%{_sysconfdir}/X11/wmsession.d/
cat <<__EOF__ > %{buildroot}/%{_sysconfdir}/X11/wmsession.d/08sugar
NAME=Sugar
ICON=%{_datadir}/sugar/data/icons/module-about_me.svg
DESC=Sugar window manager
EXEC=%{_bindir}/sugar
SCRIPT:
exec %{_bindir}/sugar
__EOF__


%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
	%{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/sugar.schemas > /dev/null || :
fi

%files -f %{name}.lang
%doc COPYING README

%config %{_sysconfdir}/dbus-1/system.d/nm-user-settings.conf
%config %{_sysconfdir}/gconf/schemas/sugar.schemas

%dir %{_datadir}/sugar
%dir %{_datadir}/sugar/activities
%{_datadir}/sugar/*

%{python_sitelibdir_noarch}/*

%{_datadir}/xsessions/sugar.desktop

%{_bindir}/*
%exclude %{_bindir}/sugar-emulator

%{_datadir}/mime/packages/sugar.xml
%config %{_sysconfdir}/X11/wmsession.d/*

%files emulator
%{_bindir}/sugar-emulator
%{_datadir}/applications/sugar-emulator.desktop
%{_datadir}/icons/hicolor/scalable/apps/sugar-xo.svg

%changelog
* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.96.1-alt1_2
- new version; import from fc17 release

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.88.0-alt1.1
- Rebuild with Python-2.7

* Tue Apr 06 2010 Aleksey Lim <alsroot@altlinux.org> 0.88.0-alt1
- Sucrose 0.88.0 release

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.84.5-alt1.1
- Rebuilt with python 2.6

* Tue Apr 28 2009 Aleksey Lim <alsroot@altlinux.org> 0.84.5-alt1
- update Sucrose to 0.84.2 version

* Wed Mar 18 2009 Aleksey Lim <alsroot@altlinux.org> 0.84.0-alt1
- update Sucrose to 0.84.0 version

* Sun Feb 15 2009 Aleksey Lim <alsroot@altlinux.org> 0.83.7-alt1
- new Sucrose 0.83.5 release

* Wed Jan 21 2009 Aleksey Lim <alsroot@altlinux.org> 0.83.5-alt2
- update gconf schemas

* Tue Jan 20 2009 Aleksey Lim <alsroot@altlinux.org> 0.83.5-alt1
- new Sucrose 0.83.4 release

* Tue Dec 23 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.4-alt1
- new upstream release

* Tue Dec 16 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.3-alt2
- altlinux #18214 fix
- setup TZ before sugar startup
- use sugar-72 theme by default
- use python-module-pygtk package instead of pygtk2
- sugar #81 fix
- hide OLPC register button
- olpc #8141 fix

* Sat Dec 13 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.3-alt1
- Sugar 0.84 release cycle

* Sun Nov 23 2008 Aleksey Lim <alsroot@altlinux.org> 0.82.2-alt2
- change group tag to "Graphical desktop/Sugar"
- make all links to child packages hard

* Tue Nov 18 2008 Aleksey Lim <alsroot@altlinux.org> 0.82.2-alt1
- first build for ALT Linux Sisyphus
