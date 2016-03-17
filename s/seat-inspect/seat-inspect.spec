Name: seat-inspect
Version: 1.0
Release: alt1.1
Summary: Understand and troubleshoot systemd

Group: System/Configuration/Other
License: GPLv3
Url: https://github.com/spanezz/seat-inspect

Source: %name-%version.tar
Patch: %name-%version-alt.patch
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
BuildRequires: python3-module-setuptools rpm-build-python3

%description
seat-inspect gives a status report of systemd facilities such as Multi-Seat,
Inhibitor Locks, Services, Targets, and other types of Unit.

The intent of running the code is to have an overview of the system status,
both to see what the new facilities are about, and to figure out if there is
something out of place.

seat-inspect is not a finished tool, but a starting point. Enrico Zini put the
first verison on github hoping that people would fork it and add their own
extra sanity checks and warnings, that it could grow not only into a standard
thing to run if a system acts weird, but also a standard thing to hack on for
those trying to learn more about Multi-Seat and systemd.

As it is now, it should be able to issue warnings if some bits are missing for
network-manager or shutdown functions to work correctly, or if some Devices or
Services are having problems. It all needs more testing by people with systems
that are experiencing such issues.

Tinkering with the code can be an interesting way to explore the new
functionalities that we recently grew. Ofcourse, the same can be done, and
in more detail, with loginctl, systemctl, and journalctl calls of various
configuration, but seat-inspect provides the only high-level view of
everything.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/*
%_man1dir/%name.1.*
%doc %name.html README.md TODO

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jun 17 2015 Terechkov Evgenii <evg@altlinux.org> 1.0-alt1
- Initial build for ALT Linux Sisyphus (git-1.0-1-gbc91524)
