Name: evrouter
Version: 0.4
Release: alt3
Summary: An input layer event router for Linux
License: GPLv2
Group: System/Configuration/Hardware
Url: http://www.bedroomlan.org/projects/evrouter
Packager: Egor Glukhov <kaman@altlinux.org>

Source0: %name-%version.tar
Patch: evrouter-0.4-gcc10.patch
Patch1: evrouter-0.4-autoconf2.71.patch

BuildRequires: gcc-c++ libICE-devel libXtst-devel

%description
Evrouter reads events from the Linux input layer, and, based on a  user-
specified set of rules, acts on them. Currently, evrouter can map events
to X11 key and button presses, XMMS commands, and can also run shell
commands.

%prep
%setup
%patch -p1
%patch1 -p1

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
* Wed Aug 02 2023 Leontiy Volodin <lvol@altlinux.org> 0.4-alt3
- Fixed build with autoconf 2.71.

* Thu Jan 21 2021 Leontiy Volodin <lvol@altlinux.org> 0.4-alt2
- Fixed build with gcc10.

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Wed Aug 24 2011 Egor Glukhov <kaman@altlinux.org> 0.4-alt1
- Initial build for Sisyphus
