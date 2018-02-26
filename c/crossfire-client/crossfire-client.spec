# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: crossfire-client.spec,v 1.5 2006/03/10 16:27:33 eugene Exp $
#
# Grab the crossfire-images archive of the sourceforge files list.  If
# you have a copy of the arch directory, you can run the
# adm/collect_images -archive from the lib directory of the server and
# it will make the archive.

%define base_name crossfire
%define version 1.11.0
# %define image_version 1.7.1
%define snd_version 1.11.0
# %define doc_version 1.6.0
# %define snd_release alt4
# %define doc_release alt2

Name: %base_name-client
Version: %version
Release: alt1%{?cvsbuild:.cvs%cvsbuild}.qa4
Summary: Client for connecting to crossfire servers
Summary(ru_RU.UTF-8): Клиент для подключения к серверам crossfire
License: GPL
Group: Games/Adventure
URL: http://crossfire.real-time.com

Packager: Eugene Vlasov <eugvv@altlinux.ru>

%ifdef cvsbuild
Source0: %name-%cvsbuild.tar.bz2
%else
Source0: %name-%version.tar.gz
%endif
Source1: %name-sounds-%snd_version.tar.gz
# Source2: %name-images-%image_version.tar.gz
# Source4: %base_name-%doc_version.doc.tar.gz
Source5: %name-x11.alternatives
Source6: %name-gtk.alternatives
Source7: %name-gtk2.alternatives
Source8: %name.desktop
Patch0: %name-1.11.0-alt-DSO.patch

Requires: crossfire-client-gui

# Automatically added by buildreq on Sat Feb 16 2008
BuildRequires: gtk+-devel imake libICE-devel libSDL-devel libSDL_image-devel libaudio-devel libcurl-devel libgtk+2-devel libX11-devel libXext-devel libpng-devel makedepend subversion xorg-cf-files

%description
Crossfire is a highly graphical role-playing adventure game with
characteristics reminiscent of rogue, nethack, omega, and gauntlet. 
It has multiplayer capability and presently runs under X11.

Client for playing the new client/server based version of Crossfire.
This package allows you to connect to crossfire servers around the world.
You do not need install the crossfire program in order to use this
package.

%description -l ru_RU.UTF-8
Crossfire - графическая ролевая приключенческая игра с характеристиками,
напоминающая rogue, nethack, omega и gauntlet. 
Имеет возможность многопользовательской игры и работает под X11.

Этот пакет содержит общие файлы клиентской части новой клиент/серверной
версии Crossfire и позволяет подключатся к серверам crossfire, 
расположенным по всему миру.


%package x11
Summary: X11 client for crossfire
Summary(ru_RU.UTF-8): GTK клиент для подключения к серверам crossfire
Group: Games/Adventure

Provides: crossfire-client-gui
Requires: crossfire-client = %version-%release

%description x11
X11 version of the crossfire client.

%description -l ru_RU.UTF-8 x11
X11-версия клиента для подключения к серверам crossfire.


%package gtk
Summary: GTK client for crossfire
Summary(ru_RU.UTF-8): GTK клиент для подключения к серверам crossfire
Group: Games/Adventure

Provides: crossfire-client-gui
Requires: crossfire-client = %version-%release

%description gtk
GTK version of the crossfire client.

%description -l ru_RU.UTF-8 gtk
GTK-версия клиента для подключения к серверам crossfire.


%package gtk2
Summary: GTK2 client for crossfire
Summary(ru_RU.UTF-8): GTK2 клиент для подключения к серверам crossfire
Group: Games/Adventure

Provides: crossfire-client-gui
Requires: crossfire-client = %version-%release

%description gtk2
Experimental GTK2 version of the crossfire client.

%description -l ru_RU.UTF-8 gtk2
Экспериментальная GTK2-версия клиента для подключения к серверам crossfire.


%package sounds
Version: %version
Release: %release
Summary: Sound effects for the crossfire game
Summary(ru_RU.UTF-8): Звуковые эффекты для клиента crossfire
Group: Games/Adventure
Requires: crossfire-client

%description sounds
Sound effects for people who want sounds with their game.

%description -l ru_RU.UTF-8 sounds
Пакет для желающих играть в crossfire со звуковым сопровождением.


#%package -n %base_name-doc
#Version: %doc_version
#Release: %doc_release
#Summary: Documentation for the crossfire game
#Summary(ru_RU.UTF-8): Документация для игры crossfire
#Group: Games/Adventure
#Requires: crossfire-client

#%description -n %base_name-doc
#This package contains documentation for the crossfire game.

#%description -l ru_RU.UTF-8 -n %base_name-doc
#Пакет содержит полный комплект документации для игры в crossfire.


#Not supported yet
#%package gnome
#Summary:gnome client for %name
#Group: X11/Games
#Provides: crossfire-client
#
#%description gnome
#gnome version of the crossfire client


%prep
%setup -q -a 1
# -a 4
%patch0 -p2

%build
CFLAGS="${CFLAGS:-%optflags}" ./configure \
	--prefix=%_prefix \
	--mandir=%_mandir \
	--bindir=%_gamesbindir \
	--datadir=%_gamesdatadir \
	--disable-alsa9 \
	--disable-alsa \
	--with-sound-dir=%_gamesdatadir/crossfire/sounds
%make_build

%install
#
# Sounds
#
install -d %buildroot%_gamesdatadir/crossfire/sounds
install -m 644 sounds/*.raw %buildroot%_gamesdatadir/crossfire/sounds
#
# Client images cd lib; adm/collect_images -archive
#
# install -d %buildroot%_gamesdatadir/crossfire
# install %name-images-%image_version/* %buildroot%_gamesdatadir/crossfire
#
# KDE
#
install -d %buildroot%_desktopdir
install -d %buildroot%_miconsdir
install -d %buildroot%_niconsdir
install -d %buildroot%_liconsdir

# %__make install \
#     DESTDIR=%buildroot \
#     bindir=%buildroot%_gamesbindir \
#     mandir=%buildroot%_man6dir

make install \
   DESTDIR=%buildroot

#
# KDE
#
#install -m 644 -c gtk/crossfire-client.desktop \
#	%{buildroot}%{_datadir}/applnk/Games/Roguelikes/crossfire.desktop
install -m 644 %SOURCE8 %buildroot%_desktopdir/%name.desktop
install -m 644 pixmaps/16x16.png %buildroot%_miconsdir/crossfire-client.png
install -m 644 pixmaps/32x32.png %buildroot%_niconsdir/crossfire-client.png
install -m 644 pixmaps/48x48.png %buildroot%_liconsdir/crossfire-client.png

mkdir -p %buildroot%_altdir

#install -d %{buildroot}%_defaultdocdir/%{base_name}-doc-%doc_version
#cp -R %{base_name}-doc/* \
#	%{buildroot}%_defaultdocdir/%{base_name}-doc-%doc_version
#install -d \
#	%{buildroot}%_defaultdocdir/%{base_name}-doc-%doc_version/Scripting/examples/script
#cp Documentation/Scripting.html \
#	%{buildroot}%_defaultdocdir/%{base_name}-doc-%doc_version/Scripting
#cp Documentation/examples/script/*.c \
#	%{buildroot}%_defaultdocdir/%{base_name}-doc-%doc_version/Scripting

install -p -m644 %SOURCE5 %buildroot%_altdir/%name-x11
install -p -m644 %SOURCE6 %buildroot%_altdir/%name-gtk
install -p -m644 %SOURCE7 %buildroot%_altdir/%name-gtk2

#install -d \
#	%{buildroot}%_defaultdocdir/%{base_name}-doc-%{doc_version}/Scripting
#cp -R Documentation/* \
#	%{buildroot}%_defaultdocdir/%{base_name}-doc-%{doc_version}/Scripting
gzip -f -9 ChangeLog

install -m755 gtk-v2/src/gcfclient2 %buildroot%_gamesbindir


%files
%doc ChangeLog.gz NOTES README TODO
#
# KDE
#
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%dir %_gamesdatadir/crossfire
%attr(0444,root,root) %_gamesdatadir/crossfire/*
%exclude %_gamesdatadir/crossfire/sounds


%files x11
%_gamesbindir/cfclient
%_man6dir/cfclient.6*
%_altdir/%name-x11


%files gtk
%_gamesbindir/gcfclient
%_man6dir/gcfclient.6*
%_altdir/%name-gtk

%files gtk2
%_gamesbindir/gcfclient2
%_altdir/%name-gtk2

# Not supported yet
#%files gnome
#%defattr(644,root,root,755)
#%doc CHANGES COPYING License NOTES README TODO
#%attr(755,root,root) /usr/X11R6/bin/gnome-cfclient
#/usr/X11R6/man/man1/gnome-cfclient.1*
# obsolete by %_desktopdir
#/usr/share/gnome/apps/Games/Tclug/crossfire.desktop
#/usr/share/pixmaps/shield.png


%files sounds
%dir %_gamesdatadir/crossfire/sounds
%attr(444,root,root) %_gamesdatadir/crossfire/sounds/*
%_gamesbindir/cfsndserv*


#%files -n %base_name-doc
#%_defaultdocdir/%base_name-doc-%doc_version


%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0-alt1.qa4
- Fixed build

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0-alt1.qa3
- Rebuilt with curl 7.21.7

* Sat Apr 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1.qa2
- NMU: 
  * .desktop file cleanup
  * updated buildreq against new sisyphus_check

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.11.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-alternatives-0.3 for crossfire-client-x11
  * update_menus for crossfire-client
  * obsolete-call-in-post-alternatives-0.3 for crossfire-client-gtk
  * obsolete-call-in-post-alternatives-0.3 for crossfire-client-gtk2
  * postclean-05-filetriggers for spec file

* Sat Feb 16 2008 Eugene Vlasov <eugvv@altlinux.ru> 1.11.0-alt1
- New version
- Removed unused menu entry (Source3)
- Updated build requires

* Thu Jun 07 2007 Eugene Vlasov <eugvv@altlinux.ru> 1.10.0-alt1
- New version
- Removed %%__ macro

* Sat Jul 15 2006 Eugene Vlasov <eugvv@altlinux.ru> 1.9.1-alt1
- New version
- Menu file replaced by desktop file
- Fixed macro warnings
- Updated BuildRequires

* Mon Oct 10 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.8.0-alt2
- Fixed macros name
- Cleanup spec

* Sun Aug 21 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.8.0-alt1
- New version
- Fixed alternatives unregistration
- Build experimental GTK2 client
- Updated BuildRequires

* Sat Mar 05 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.7.1-alt1
- New version

* Fri Jan 28 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.7.0-alt3.cvs20040919
- Build crossfire-doc from crossfire-1.7.0-alt1.src

* Thu Dec 23 2004 Eugene Vlasov <eugvv@altlinux.ru> 1.7.0-alt2.cvs20040919
- Updated to CVS snapshot 20040919
- Moved x11 client into a separate package
- Used alternatives to select x11/gtk client
- Added scripting documentation

* Sun Dec 12 2004 Eugene Vlasov <eugvv@altlinux.ru> 1.7.0-alt1
- First build for Sisyphus

