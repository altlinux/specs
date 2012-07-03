Name: wondershaper
Version: 1.1a
Release: alt1

Summary: Helps to maintain interactive latency on modem/ADSL/cable
License: GPL
Group: System/Servers
Url: http://lartc.org/%name
BuildArch: noarch
Packager: Andy Gorev <horror@altlinux.ru>

Source: %url/%name-%version.tar.bz2

%description
This package attempts to implement
+ Maintain low latency for interfactive traffic at all times.
+ Allow 'surfing' at reasonable speeds while up or downloading.
+ Make sure uploads don't harm downloads, and the other way around.
+ Have the ability to mark certain hosts/ports as 'low priority'.

%prep
%setup -q

%install
%__mkdir_p $RPM_BUILD_ROOT{%_sbindir,%_sysconfdir/%name}
%__install -p -m755 wshaper* $RPM_BUILD_ROOT%_sysconfdir/%name/
for f in wshaper*; do
	%__ln_s "../..%_sysconfdir/%name/$f" $RPM_BUILD_ROOT%_sbindir/
done

%files
%_sbindir/*
%config %_sysconfdir/%name
%doc README TODO VERSION ChangeLog

%changelog
* Tue Oct 14 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1a-alt1
- Initial revision.
