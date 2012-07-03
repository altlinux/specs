Name: timelimit
Version: 1.5
Release: alt1

Summary: Limit a process's absolute execution time

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://devel.ringlet.net/sysutils/timelimit/
License: BSD
Group: Monitoring

Source: http://devel.ringlet.net/sysutils/timelimit/%name-%version.tar

%description
timelimit executes a command and terminates the spawned process after
a given time with a given signal. A "warning" signal is sent first,
then, after a timeout, a "kill" signal, similar to the way init(8)
operates on shutdown.

%prep
%setup

%build
%make_build

%install
install -m755 -D %name %buildroot%_bindir/%name
install -m644 -D %name.1 %buildroot%_man1dir/%name.1

%files
%doc ChangeLog
%_bindir/%name
%_man1dir/*

%changelog
* Sun Mar 21 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- initial release for ALT Linux Sisyphus
