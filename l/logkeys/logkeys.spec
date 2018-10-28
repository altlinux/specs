
Name: logkeys
Version: 0.1.1c
Release: alt2

Summary: A GNU/Linux keylogger that works!
Group: Development/Debug
License: GNU GPLv3
Url: https://github.com/kernc/logkeys

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: gcc-c++ kbd

%description
logkeys is a linux keylogger. It is no more advanced than other available linux
keyloggers, notably lkl and uberkey, but is a bit newer, more up to date, it
doesn't unreliably repeat keys and it shouldn't crash your X. All in all, it
just seems to work. It relies on event interface of the Linux input subsystem. 
Once completely set, it logs all common character and function keys, while also
being fully aware of Shift and AltGr key modifiers.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man8dir/*
%exclude %_sysconfdir/logkeys-kill.sh
%exclude %_sysconfdir/logkeys-start.sh
%exclude %_bindir/llk
%exclude %_bindir/llkk

%changelog
* Mon Oct 29 2018 Paul Wolneykien <manowar@altlinux.org> 0.1.1c-alt2
- Removed unused commands.

* Mon Oct 29 2018 Paul Wolneykien <manowar@altlinux.org> 0.1.1c-alt1
- Initial build for ALT.
