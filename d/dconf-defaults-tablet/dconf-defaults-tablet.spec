Name: dconf-defaults-tablet
Version: 0.1
Release: alt2
Summary: Dconf profile sceleton for tablet distro settings
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch

Source: %name-%version.tar


%description
Dconf profile sceleton for tablet distro settings

%package disable-lightbox
Summary: Disables the LightBox extension in Gnome-Shell
Group: System/Configuration/Other
Requires: %name = %version-%release

%description disable-lightbox
Disables the LightBox extension in Gnome-Shell.

%package caribou-fullscale
Summary: Set the 'fullscale' layout to be used with the onscreen keyboard Caribou
Group: System/Configuration/Other
Requires: %name = %version-%release

%description caribou-fullscale
Set the 'fullscale' layout to be used with the onscreen keyboard Caribou.

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/profile.d
install profile.d/dconf-tablet.sh %buildroot%_sysconfdir/profile.d

mkdir -p %buildroot%_sysconfdir/dconf/db/tablet.d/locks
install -m0644 dconf/db/tablet.d/use-lightbox %buildroot%_sysconfdir/dconf/db/tablet.d/
install -m0644 dconf/db/tablet.d/use-caribou-fullscale %buildroot%_sysconfdir/dconf/db/tablet.d/

mkdir -p %buildroot%_sysconfdir/dconf/profile
install -m0644 dconf/profile/tablet %buildroot%_sysconfdir/dconf/profile

%files
%_sysconfdir/profile.d/*
%_sysconfdir/dconf/profile/*
%dir %_sysconfdir/dconf/db/tablet.d/locks
%dir %_sysconfdir/dconf/db/tablet.d

%files disable-lightbox
%_sysconfdir/dconf/db/tablet.d/use-lightbox

%files caribou-fullscale
%_sysconfdir/dconf/db/tablet.d/use-caribou-fullscale

%post disable-lightbox
dconf update

%post caribou-fullscale
dconf update

%changelog
* Sat May 12 2012 Paul Wolneykien <manowar@altlinux.ru> 0.1-alt2
- Make subpackages depend on the main package.
- Fix/improve the LightBox disabling package.
- Add package to use the 'fullscale' layout with the onscreen keyboard Caribou.

* Wed Mar 14 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initital release

