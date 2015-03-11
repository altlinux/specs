%define git 20140513

Name: qconnman-ui
Version: 0
Release: alt1.%git

Summary: Qt GUI for Connman
License: LGPLv2.1+
Group: Networking/Other

Url: https://github.com/OSSystems/qconnman-ui
# git snapshot
Source0: %name-%git.tar.bz2
# from their git
Source1: qconnman-ui.png

BuildRequires: ImageMagick
BuildRequires: qt4-devel gcc-c++
BuildRequires: pkgconfig(qconnman)
Requires: connman

%description
Qt GUI for Connman. It requires that Connman is installed and running.

%prep
%setup -n %name-%git

%build
qmake-qt4
%make

%install
make install INSTALL_ROOT=%buildroot%prefix

# install menu entry
mkdir -p %buildroot%_datadir/applications/
cat > %buildroot%_datadir/applications/%name.desktop << EOF
[Desktop Entry]
Name=QConnMan-UI
Comment=GUI for Connman
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=Network;Utility;
EOF

# install menu icons
for N in 16 32 48 64; do
	convert %SOURCE1 -scale ${N}x${N} $N.png;
	install -pDm644 $N.png \
		%buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/qconnman/i18n/*.qm
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Wed Mar 11 2015 Michael Shigorin <mike@altlinux.org> 0-alt1.20140513
- built for ALT Linux (based on Rosa's 0-0.20140513.1 package)

