Name:    flatpak-repo-flathub
Version: 1.1
Release: alt1

Summary: Central repository of Flatpak applications
License: GPL-2.0
Group: System/Configuration/Packaging
URL: https://flathub.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Source:   %name-%version.tar

Requires: flatpak
Requires(post,postun): flatpak

%description
Central repository of Flatpak applications.

%prep
%setup

%install
install -Dpm0644 config.core %buildroot%_sharedstatedir/flatpak/repo/config.core
install -Dpm0644 config.flathub %buildroot%_sharedstatedir/flatpak/repo/config.flathub
install -Dpm0644 flathub.trustedkeys.gpg %buildroot%_sharedstatedir/flatpak/repo/flathub.trustedkeys.gpg
mkdir -p %buildroot%_sharedstatedir/flatpak/repo/objects

%files
%_sharedstatedir/flatpak/repo/*

%postun
# Remove Flathub repository from Flatpack
flatpak remote-delete flathub 2>/dev/null ||:

%post
# Add Flathub repository to Flatpack config
grep -q '^\[remote "flathub"\]' %_sharedstatedir/flatpak/repo/config || cat %_sharedstatedir/flatpak/repo/config.flathub >> %_sharedstatedir/flatpak/repo/config
# Add parameters to [core]
grep -q '^\[core\]' %_sharedstatedir/flatpak/repo/config || cat %_sharedstatedir/flatpak/repo/config.core >> %_sharedstatedir/flatpak/repo/config

%changelog
* Mon Apr 11 2022 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Fix remote-ls (ALT #42393).

* Thu Dec 02 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
