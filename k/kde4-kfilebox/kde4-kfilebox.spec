
%define tname Kfilebox
%define rname kfilebox
Name: kde4-kfilebox
Version: 0.4.9
Release: alt1

Group: Networking/File transfer
Summary: KDE front end for Dropbox
Url: http://sourceforge.net/projects/kdropbox/
License: GPLv2

Source0: %rname-%version.tar

# Automatically added by buildreq on Mon Jun 27 2011 (-bi)
# optimized out: elfutils fontconfig kde4libs kdelibs libdbusmenu-qt2 libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-sql libqt4-svg libqt4-xml libstdc++-devel phonon-devel
#BuildRequires: gcc-c++ glibc-devel-static kde4libs-devel kdelibs-devel
BuildRequires: gcc-c++ glibc-devel-static kde4libs-devel kde-common-devel

%description
KDE front end for Dropbox

%prep
%setup -qn %rname-%version
echo "QMAKE_CXXFLAGS += \$(RPM_OPT_FLAGS) -I%_K4includedir" >> %rname.pro
qmake-qt4

%build
SUBLIBS="-L%_K4link" %make


%install
mkdir -p %buildroot/{%_kde4_bindir,%_K4start,%_kde4_xdg_apps,%_K4apps/%rname,%_kde4_iconsdir}

install -m0755 bin/* %buildroot/%_kde4_bindir/
install -m 0644 kfilebox.notifyrc %buildroot/%_K4apps/%rname/
cp -ar img/*.png %buildroot/%_K4apps/%rname/
cp -ar img/{default,monochrome,white} %buildroot/%_K4apps/%rname/
chmod 0644 %buildroot/%_K4apps/%rname/*.png
chmod 0644 %buildroot/%_K4apps/%rname/*/*.png
cp -ar img/hicolor %buildroot/%_kde4_iconsdir/
chmod 0644 %buildroot/%_kde4_iconsdir/*/*/apps/*.png

# install translations
pushd locale
ls -1d * | \
while read d
do
    if [ -f $d/%rname.po ]; then
	[ -f $d/%rname.mo ] || msgfmt -o d/%rname.mo $d/%rname.po ||:
	mkdir -p %buildroot/%_K4i18n/$d/LC_MESSAGES
	install -m 0644 $d/%rname.mo %buildroot/%_K4i18n/$d/LC_MESSAGES/%rname.mo ||:
    fi
done
popd

%K4find_lang --with-kde %rname

cat > %buildroot/%_kde4_xdg_apps/%rname.desktop << EOF
[Desktop Entry]
Name=%tname
Comment=KDE front end for Dropbox
Exec=%rname
Icon=%rname
Terminal=false
Type=Application
StartupNotify=false
Categories=Network;FileTransfer;
X-KDE-autostart-after=panel
X-KDE-StartupNotify=false
X-DBUS-StartupType=Unique
X-KDE-UniqueApplet=true
X-KDE-autostart-condition=kfileboxrc:General:AutoStart:false
EOF
chmod 0755 %buildroot/%_kde4_xdg_apps/%rname.desktop

cp -ar %buildroot/%_kde4_xdg_apps/%rname.desktop %buildroot/%_K4start/%rname.desktop

cat > %buildroot/%_K4apps/%rname/%rname.notifyrc << EOF
[Global]
Comment=Kfilebox
Name=kfilebox
IconName=kfilebox

[Event/notify]
Name=Notification
Comment=Any notification
Action=Popup
EOF


%files -f %rname.lang
#%doc doc/readme.txt
%_kde4_bindir/%rname
%_kde4_xdg_apps/%rname.desktop
%_K4start/%rname.desktop
%_K4apps/%rname
%_kde4_iconsdir/hicolor/*/apps/%rname.*

%changelog
* Thu Mar 29 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.9-alt1
- new version

* Tue Jun 28 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.7-alt1
- initial build
