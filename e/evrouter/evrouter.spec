Name: evrouter
Version: 0.4
Release: alt1
Summary: An input layer event router for Linux
License: GPLv2
Group: System/Configuration/Hardware
Url: http://www.bedroomlan.org/projects/evrouter
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar
BuildRequires: gcc-c++ libICE-devel libXtst-devel

%description
Evrouter reads events from the Linux input layer, and, based on a  user-
specified set of rules, acts on them. Currently, evrouter can map events
to X11 key and button presses, XMMS commands, and can also run shell
commands.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README src/example
%_bindir/%name
%_man1dir/*

%changelog
* Wed Aug 24 2011 Egor Glukhov <kaman@altlinux.org> 0.4-alt1
- Initial build for Sisyphus
