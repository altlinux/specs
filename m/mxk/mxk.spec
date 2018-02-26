Name: mxk
Version: 1.8
Release: alt1

Summary: An evdev/uinput input mangling server
License: GPLv3+
Group: System/Configuration/Hardware
Url: http://welz.org.za/projects/mxk

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %name-%version.tar

BuildPreReq: groff-ps

%description
mxk is a reasonably sophisticated input rewriting server. It picks up
where conventional keyboard mappings reach their limits. mxk uses the
linux evdev/uinput infrastructure. This means that mxk runs entirely in
userspace, it doesn't require a special kernel driver or patch.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall etcdir=%buildroot%_sysconfdir

%files
%_sbindir/*
%_sysconfdir/%name/
%_man8dir/*
%doc README

%changelog
* Sat Apr 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.8-alt1
- 1.8

* Mon Mar 09 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.7-alt1
- initial build

