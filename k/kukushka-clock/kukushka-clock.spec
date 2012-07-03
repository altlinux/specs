Summary: The amazing cuckoo clock
Name: kukushka-clock
Version: 0.3.2
Release: alt1
Group: Toys
License: LGPL
Packager: Ilya Mashkin <oddity at altlinux dot ru>

# Based on code from
URL: http://bash.org.ru/quote/323695
Source0: ftp://andriy.asplinux.com.ua/pub/people/andy/kc/%{name}-%{version}.tar.gz
#Source10: http://melody.mobru.com/pub/melodies/6159/33339.wav
#Source11: http://zeeman.ehc.edu/envs/Hopp/mod5.wav
#Source12: http://cool.berber.co.il/CoolStuff/Other%20Cool%20Stuff/WAV/Mic%20ICQ/EMail.wav
BuildRequires: sed
Requires: bash
Requires: coreutils
Requires: eject
Requires: alsa-utils
Requires: crontabs
BuildArch: noarch

%description
The amazing cuckoo clock simulator. It's using the
CD/DVD device and soundcard.

%prep
%setup -q

%build

%install


make install DESTDIR=${RPM_BUILD_ROOT} \
	BINDIR=%{_bindir} \
	CFGDIR=%{_sysconfdir}/sysconfig \
	PKGDATADIR=%{_datadir}/%{name} \
	TEMP_DIR=/var/run/%{name} \
#	SOUNDS="%{SOURCE10} %{SOURCE11} %{SOURCE12}"


%post
if [ $1 -eq 1 ]; then
    /bin/ln -sf %{_bindir}/%{name} %{_sysconfdir}/cron.hourly/%{name}
fi

%preun
if [ $1 -eq 0 ]; then
    /bin/rm -f %{_sysconfdir}/cron.hourly/%{name}
fi

%files

%doc LICENSE README sounds/README.sounds
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_datadir}/%{name}/
%attr(1777,root,root) %dir /var/run/%{name}

%changelog
* Sun Jun 17 2007 Ilya Mashkin <oddity at altlinux dot ru> 0.3.2-alt1
- Initial build for ALT Linux Sisyphus based on spec by Andy Shevchenko

* Sat Jun 16 2007 Andy Shevchenko <andy@smile.org.ua> 0.3.2-1
- fix post and preun scriptlets

* Fri Jun 15 2007 Andy Shevchenko <andy@smile.org.ua> 0.0.1-1
- initial build
