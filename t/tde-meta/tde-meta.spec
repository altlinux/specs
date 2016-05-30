Name: tde-meta
Version: 3.15.3.2
Release: alt1

Summary: TDE metapackage
License: public domain
Group: Graphical desktop/KDE
Url: http://en.altlinux.org/regular

%description
%summary handling differences
in package names across the branches

%package -n tde-regular
Summary: TDE metapackage for regular builds
License: public domain
Group: Graphical desktop/KDE

# taken from mkimage-profiles
Requires: kdebase
Requires: kde-icon-theme-nuvola
Requires: tango-icon-theme-extras
Requires: kkbswitch
Requires: kdegraphics-ksnapshot
Requires: kdegraphics-kview
Requires: kdeutils-laptop
Requires: kdepim-akregator
Requires: kdeutils-ark
# broken against current bluez, might be fixed in R14
#Requires: kdebluetooth
Requires: kdeutils-kcalc
Requires: kdegraphics-kpdf
Requires: kdeaddons-konqueror
Requires: krusader
Requires: kaffeine
Requires: kdemultimedia-kmix
Requires: kde3-amarok
Requires: kde3-k3b
#Requires: kde3-ktorrent

# rom_as@ said it's still needed
Requires: hal
Requires: arts

%description -n tde-regular
This package pulls in everything required
for the TDE Regular LiveCD (see %url).

%prep

%build

%files -n tde-regular

%changelog
* Mon May 30 2016 Michael Shigorin <mike@altlinux.org> 3.15.3.2-alt1
- initial release

