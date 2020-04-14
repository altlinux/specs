Name:		cpu-g
Version:	0.16.2
Release:	alt1.1

License:	GPLv3
Group:		System/Kernel and hardware
Summary:	CPU-G is an application that shows useful information about your hardware
Url:		https://github.com/atareao/cpu-g

Source0:	%name-%version.tar.gz
Source1:	%name-uk_UA.po
Source2:	%name.desktop

Patch0:		%name-patch.patch
Patch1:		%name-0.16.2-alt_matplotlib.backends.patch

Requires:	/usr/bin/glxinfo

BuildArch: noarch

BuildRequires: /usr/bin/convert python3-dev python3-module-mpl_toolkits

%description
CPU-G is an application that shows useful information about your hardware.
It collects and displays information about your CPU, RAM, Motherboard, some
general information about your system and more.

%prep
%setup -n %name-%version
%patch0 -p1
%patch1 -p1
cp %SOURCE1 po/uk_UA.po

%install
%__mkdir -p %buildroot/%_datadir/{%name,applications,locale/{ca/LC_MESSAGES,es/LC_MESSAGES,eu_ES/LC_MESSAGES,uk_UA/LC_MESSAGES}}
%__mkdir -p $RPM_BUILD_ROOT/%_bindir

cp -a data/{distros,graphic_card,icons,logos} %buildroot/%_datadir/%name/
cp -a debian/changelog %buildroot/%_datadir/%name/
cp -a data/icons/%name.png %buildroot/%_datadir/%name/
cp -a src/*.py %buildroot/%_datadir/%name/
msgfmt po/ca.po -o %buildroot/%_datadir/locale/ca/LC_MESSAGES/%name.mo
msgfmt po/es.po -o %buildroot/%_datadir/locale/es/LC_MESSAGES/%name.mo
msgfmt po/eu_ES.po -o %buildroot/%_datadir/locale/eu_ES/LC_MESSAGES/%name.mo
msgfmt po/uk_UA.po -o %buildroot/%_datadir/locale/uk_UA/LC_MESSAGES/%name.mo

%__install -m 755 bin/%name %buildroot/%_datadir/%name
%__install -m 644 %SOURCE2 %buildroot/%_desktopdir
ln -s %_datadir/%name/%name $RPM_BUILD_ROOT%_bindir/%name

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 data/icons/cpu-g_192.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 data/icons/cpu-g_192.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 data/icons/cpu-g_192.png %buildroot%_miconsdir/%name.png

%files
%doc COPYING README.md
%dir %_datadir/%name
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_datadir/locale/*/LC_MESSAGES/*.mo
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

%changelog
* Tue Apr 14 2020 Motsyo Gennadi <drool@altlinux.ru> 0.16.2-alt1.1
- fix Requires

* Sat Apr 11 2020 Motsyo Gennadi <drool@altlinux.ru> 0.16.2-alt1
- 0.16.2

* Thu Mar 31 2016 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1
- initial build for ALT Linux
