%global svnrev  2592

Name:           inxi
Version:        2.2.19
Release:        alt1
Summary:        A full featured system information script
Summary(ru):    Скрипт вывода полной информации об оборудовании и системе

License:        GPLv3
Group:		Monitoring
URL:            http://code.google.com/p/inxi/
Source0:        http://inxi.googlecode.com/svn-history/r%{svnrev}/trunk/%{name}.tar.gz

BuildArch:      noarch

Requires:       net-tools
Requires:       pciutils
Requires:       procps
Requires:       lm_sensors
Requires:       usbutils
Requires:       hddtemp

%description
Inxi offers a wide range of built-in options, as well as a good number of extra
features which require having the script recommends installed on the system.


%description -l ru
Inxi позволяет выводить различную информацию об используемом оборудовании и о
работе системы.


%prep
%setup -q -c
chmod -x %{name}.changelog
#Disable update option
sed -i "s/B_ALLOW_UPDATE='true'/B_ALLOW_UPDATE='false'/" inxi

%build


%install
install -p -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
install -p -D -m 644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz

%files
%doc %name.changelog
%_bindir/%name
%_man1dir/%name.1*


%changelog
* Sun Apr 26 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.19-alt1
- Initial build for Sisyphus (thanks Fedora team for the spec)

