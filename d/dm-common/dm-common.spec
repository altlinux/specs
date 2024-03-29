#define dmroot /usr/libexec
#define dmroot /usr/etc
%define dmroot /etc
%define dmdirname dm-sessions
%define dmbase %dmroot/%dmdirname
%define commonsessionsdir %dmbase/common
%define waylandsessionsdir %dmbase/wayland

Summary: Common files for Display Managers that lanch wayland-sessions.
Name: dm-common
Version: 0.03
Release: alt1
License: GPLv2+ or ALT-Public-Domain
Group: Graphical desktop/Other
Packager: Igor Vlasenko <viy@altlinux.org>
URL: http://wiki.altlinux.org/Display_Manager_Policy
BuildArch: noarch

Source: %name-%version.tar

%description
Common files for Display Managers that can lanch wayland-sessions.
For now this package has recommended wrapper for wayland-sessions
and owns its dirs wrapperdir{,/init.d,/profile.d}.

%prep
%setup

%build

%install
mkdir -p %buildroot%commonsessionsdir/{profile.d,init.d}
mkdir -p %buildroot%waylandsessionsdir/{profile.d,init.d}
sed 's,@WRAPPER_DIR@,%waylandsessionsdir,' wrapper.in > wrapper

install -m 755 wrapper %buildroot%waylandsessionsdir/wrapper

%files
%waylandsessionsdir/wrapper
%dir %dmbase
%dir %commonsessionsdir
%dir %commonsessionsdir/init.d
%dir %commonsessionsdir/profile.d
%dir %waylandsessionsdir
%dir %waylandsessionsdir/init.d
%dir %waylandsessionsdir/profile.d

%changelog
* Fri Apr 15 2022 Igor Vlasenko <viy@altlinux.org> 0.03-alt1
- Sisyphus release

* Sat Dec 04 2021 Igor Vlasenko <viy@altlinux.org> 0.02-alt1
- renamed to dm-common
- added common sessions' init.d, profile.d
