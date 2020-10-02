Name: deepin-desktop-base
Version: 2020.07.31
Release: alt1
Summary: Base component for Deepin
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-desktop-base
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-desktop-base_2020.07.31_alt_fix-multiarch-build.patch

BuildArch: noarch
#Recommends:     deepin-wallpapers
#Recommends:     deepin-screensaver
#Recommends:     plymouth-theme-deepin

%description
This package provides some components for Deepin desktop environment.

- deepin logo
- deepin desktop version
- login screen background image
- language information

%package -n deepin-manual-directory
Summary: Package that owns the Deepin manual directory
Group: Graphical desktop/Other

%description -n deepin-manual-directory
This package owns the Deepin manual directory. This is a workaround
before deepin-manual actually comes into Fedora to unblock packaging.

%prep
%setup
%patch -p2

# Remove Deepin distro's lsb-release
# Don't override systemd timeouts
# Remove apt-specific templates
sed -E '/lsb-release|systemd|apt|back/d' Makefile

# Fix data path
%__subst 's|/usr/lib|%_datadir|' Makefile

# Set deepin type to ALT Linux
%__subst 's|Type=.*|Type=ALT Linux|; /Type\[/d' files/desktop-version*.in

%build
%make_build

%install
%makeinstall_std

# Make a symlink for deepin-version
mkdir -p %buildroot/etc/
ln -sfv ..%_datadir/deepin/desktop-version %buildroot/etc/deepin-version

mkdir -p %buildroot%_datadir/dman
echo "This package owns the Deepin manual directory. This is a workaround
before deepin-manual actually comes into ALT Linux to unblock packaging." > %buildroot%_datadir/dman/README.altlinux

%files
%doc LICENSE
%config(noreplace) %_sysconfdir/appstore.json
%_sysconfdir/deepin-version
%exclude %_sysconfdir/os-version
%dir %_datadir/deepin/
%_datadir/deepin/desktop-version
%_datadir/deepin/dde-desktop-watermask.json
%_datadir/i18n/i18n_dependent.json
%_datadir/i18n/language_info.json
%dir %_datadir/plymouth
%_datadir/plymouth/deepin-logo.png
%exclude %_datadir/deepin/uos_logo.svg
%exclude %_sysconfdir/lsb-release
%exclude %_sysconfdir/systemd/system.conf.d/deepin-base.conf
%exclude %_sysconfdir/systemd/logind.conf.d/deepin-base.conf
%exclude %_datadir/python-apt/templates/Deepin.info
%exclude %_datadir/python-apt/templates/Deepin.mirrors
%exclude %_var/uos/os-license

%files -n deepin-manual-directory
%_datadir/dman

%changelog
* Tue Aug 04 2020 Leontiy Volodin <lvol@altlinux.org> 2020.07.31-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
