Name: lazy_ips
Version: 20200706
Release: alt2
License: GPL-3.0-or-later
Group: Emulators
Url: https://github.com/btimofeev/lazy_ips
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.xz
Source1: %name.png
Summary: lazy_ips is an universal IPS patcher
BuildArch: noarch

BuildRequires: rpm-build-python3 rpm-build-gir
Requires: typelib(Gtk) = 3.0

%description
Universal IPS patcher.

%prep
%setup -n %name-%version

%install
mkdir -p %buildroot%_bindir
install -m 0755 %name.py %buildroot%_bindir/%name

mkdir -p %buildroot%_pixmapsdir
install -m 0644 %SOURCE1 %buildroot%_pixmapsdir/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Exec=%name
Icon=%name.png
Type=Application
Terminal=false
Name=Lazy_ips
GenericName=Universal IPS patcher
Comment=%summary
StartupNotify=false
Categories=Game;Emulator;
EOF

%files
%doc README.md
%_bindir/%name
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Sun May 14 2023 Anton Midyukov <antohami@altlinux.org> 20200706-alt2
- NMU: fix Requires
- NMU: fix License
- NMU: fix Categories in destop file
- NMU: cleanup spec

* Wed Jan 4 2022  Artyom Bystrov <arbars@altlinux.org> 20200706-alt1
- Import from PCLinuxOS srpm

* Wed Nov 13 2019  Agent Smith <ruidobranco@yahoo.com.br> 6255ba8-1pclos2017
- Updated the package lazy_ips-19048f9f-1pclos2019.noarch.rpm to Python3

* Wed Jul 12 2017  Agent Smith <ruidobranco@yahoo.com.br> 9048f9f-1pclos2017
- Created the package lazy_ips-9048f9f-1pclos2017.noarch.rpm, with latest source.

