%add_findpackage_path %_kde4_bindir

%define rname kde4-minimal-settings
Name: kde4-minimal-settings
Version: 4.7
Release: alt1

Group: Graphical desktop/KDE
Summary: Minimal KDE4 settings
Url: https://code.launchpad.net/kubuntu-low-fat-settings
License: GPLv3

BuildArch: noarch

Requires: gettext qmergeinifiles > 1.50

Source: %name-%version.tar
Source1: kubuntu-low-fat-settings.tar

BuildRequires: kde-common-devel qmergeinifiles gettext

%description
This package allow to set minimal KDE4 settings to gain additional system resources


%prep
%setup -q -a1
# cleanup
rm -f kubuntu-low-fat-settings/share/autostart/akonaditray.desktop

%build
# config
for conf in kubuntu-low-fat-settings/share/config/*
do
    outname=`basename $conf`
    qmergeinifiles --no-override share/config/$outname $conf
done
# autostart
mkdir -p share/autostart
for desktop in kubuntu-low-fat-settings/share/autostart/*.desktop
do
    outname=`basename $desktop`
    qmergeinifiles --no-override share/autostart/$outname $conf
    cp -ar $desktop share/autostart/$outname
done

%install
mkdir -p %buildroot/%_K4apps/%name/config
install -m 0644 share/config/* %buildroot/%_K4apps/%name/config
mkdir -p %buildroot/%_K4apps/%name/autostart/
install -m 0644 share/autostart/* %buildroot/%_K4apps/%name/autostart
mkdir -p %buildroot/%_K4bindir/
install -m 0755 bin/%name %buildroot/%_K4bindir/
mkdir -p %buildroot/%_K4xdg_apps/
install -m 0644 share/applications/*.desktop %buildroot/%_K4xdg_apps/
# translations
find po/* -type d | \
while read d
do
    lang=`basename $d`
    mkdir -p %buildroot/%_datadir/locale/$lang/LC_MESSAGES
    msgfmt -o %buildroot/%_datadir/locale/$lang/LC_MESSAGES/%name.mo $d/%name.po
done

%K4find_lang --with-kde %name

%files -f %name.lang
%_K4bindir/%name
%_K4apps/%name
%_K4xdg_apps/*-setup.desktop

%changelog
* Fri Oct 28 2011 Sergey V Turchin <zerg@altlinux.org> 4.7-alt1
- initial build
