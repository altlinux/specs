%define _optlevel s

Name: knetstats
Version: 1.6.2
Release: alt4

Group: Monitoring
Summary: Network monitor applet for KDE
Url: http://knetstats.sourceforge.net/
License: GPL

Requires: kdelibs >= %{get_version kdelibs}

Source: %name-%version.tar.bz2
Source1: knetstats-ru.po

Patch1: knetstats-1.6.2-alt-desktop.patch
Patch2: knetstats-1.6.1-alt-autostart.patch
Patch3: knetstats-1.6.1-alt-uniqueapp.patch
Patch4: knetstats-1.6.2-alt-gcc43.patch
Patch5: knetstats-1.6.2-alt-automake.patch

# Automatically added by buildreq on Fri Jan 26 2007
BuildRequires(pre): kdelibs-devel
BuildRequires: gcc-c++ libstdc++-devel libjpeg-devel xml-utils

%description
A simple KDE network monitor that show rx/tx LEDs of any network interface
on a system tray icon

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# update Russian translation
cat %SOURCE1 > translations/ru/messages/knetstats.po

#%__subst "s/\(Wl,--no-undefined\)/-Wl,--warn-unresolved-symbols \1/g" admin/acinclude.m4.in
#%__subst "s/\-lkdeui/-lkdeui -lpthread/g" admin/acinclude.m4.in
#%__subst "s/\-lkdecore/-lkdecore -lpthread/g" admin/acinclude.m4.in
#%__subst "s/\-lkdefx/-lkdefx -lpthread/g" admin/acinclude.m4.in
#%__subst 's,\.la,\.so,' admin/acinclude.m4.in
%make -f admin/Makefile.common cvs
#./autogen.sh

%build
export PATH="$PWD:$PATH"
%add_optflags -I%_includedir/tqtinterface
#add_optflags -I%_includedir/linux-libc-headers/include
#export CFLAGS="%optflags" CXXFLAGS="%optflags""
export QTDIR="%_qt3dir" KDEDIR="%prefix"
%K3configure

%make

%install
export PATH="$PWD:$PATH"
%K3install

pushd %buildroot/%_K3i18n/
for d in *
do
    new_d=`echo $d| sed "s|_.*||"`
    if [ "$d" != "$new_d" ]
    then
	rm -rf "$new_d"
	mv "$d" "$new_d"
    fi
done
popd

mkdir -p %buildroot/%_K3start
install -m 0644 %buildroot/%_K3xdg_apps/%name.desktop %buildroot/%_K3start/%name.desktop

%K3find_lang --with-kde %name


%files -f %name.lang
#%doc CHANGELOG README
%_K3bindir/%name
%_K3datadir/apps/%name
%_kde3_iconsdir/*/*/apps/*
%_K3xdg_apps/%name.desktop
%_K3start/%name.desktop

%changelog
* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt4
- move to alternate place

* Mon Jan 24 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt3
- fix to build

* Tue Aug 25 2009 Sergey V Turchin <zerg@altlinux.org> 1.6.2-alt2
- fix to build with new automake

* Tue Dec 02 2008 Sergey V Turchin <zerg at altlinux dot org> 1.6.2-alt1
- new version
- fix compile with gcc-4.3
- remove deprecated macroses from specfile

* Thu Jan 10 2008 Sergey V Turchin <zerg at altlinux dot org> 1.6.1-alt3
- update Russian translation (#13851)

* Fri Nov 30 2007 Sergey V Turchin <zerg at altlinux dot org> 1.6.1-alt2
- add autostart feature

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 1.6.1-alt1
- new version

* Thu Jul 20 2006 Sergey V Turchin <zerg at altlinux dot org> 1.6-alt1
- new version

* Tue Jan 24 2006 Sergey V Turchin <zerg at altlinux dot org> 1.5-alt1
- initial specfile
