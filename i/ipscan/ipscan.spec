%ifarch %ix86
%define			platform linux
%else
%define			platform linux64
%endif

Summary:		Angry IP network scanner
Summary(de):		Angry IP Netzwerkscanner
Name:			ipscan
Version:		3.5.3
Release:		alt1
Group:			Security/Networking
License:		GPLv2
Url:			http://www.angryip.org/w/Home/
Source0:		http://sourceforge.net/projects/ipscan/files/%name-linux-%version.jar
Source1:		http://sourceforge.net/projects/ipscan/files/%name-linux64-%version.jar
Source2:		%name.png

BuildRequires:		/usr/bin/convert /usr/bin/java

%description
Angry IP Scanner is an IP address scanner tool. It is used for scanning of IP addresses
with the goal of finding alive hosts and gathering interesting information about each of them.
It is very extensible, allowing it to be used for very wide range of purposes, with the primary
goal of being useful to network administrators

%description -l de
Angry IP Scanner ist ein IP-Adressenscanner, dieser wird mit dem Ziel eingesetzt, verfügbare
Hosts im Netzwerk zu finden und interessante Informationen über diese zu sammeln. Angry IP ist
in hohem Maß erweiterbar, erlaubt es in einem großen Bereich eingesetzt zu werden, mit dem
Primärziel nützlich für Netzwerkadministratoren zu sein.

%prep
%install

mkdir -p %buildroot%_libdir/%name/
%ifarch %ix86
cp -af %SOURCE0 %buildroot/%_libdir/%name/
%else
cp -af %SOURCE1 %buildroot/%_libdir/%name/
%endif

# launcher
mkdir -p %buildroot%_bindir/
cat > %buildroot%_bindir/%name << EOF
#!/bin/sh
cd %_libdir/%name
java -jar %name-%platform-%version.jar $@
cd /
EOF

chmod a+x %buildroot%_bindir/%name

# menu-entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Angry IP scanner
GenericName=Angry IP scanner
Comment=Fast and friendly network scanner.
Comment[de]=Schneller und freundlicher Netzwerkscanner.
Exec=%name
Icon=%name.png
Terminal=0
Type=Application
Categories=System;Monitor;
EOF

#icons
# Icons
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 %SOURCE2 %buildroot%_liconsdir/%name.png
convert -resize 32x32 %SOURCE2 %buildroot%_niconsdir/%name.png
convert -resize 16x16 %SOURCE2 %buildroot%_miconsdir/%name.png

%files
%_bindir/%name
%_libdir/%name/%name-%platform-%version.jar
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Thu Sep 06 2018 Motsyo Gennadi <drool@altlinux.ru> 3.5.3-alt1
- 3.5.3

* Thu Sep 06 2018 Motsyo Gennadi <drool@altlinux.ru> 3.5.1-alt1
- initial build for ALT Linux from PCLinuxOS src.rpm
