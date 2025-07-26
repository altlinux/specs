%define _unpackaged_files_terminate_build 1

Name: lomiri-wallpapers
Version: 20.04.0
Release: alt1

Summary: Wallpapers for the Lomiri Operating Environment
License: CC0-1.0 and CC-BY-4.0 and CC-BY-SA-3.0 and CC-BY-SA-4.0 and Expat
Group: Graphics
Url: https://gitlab.com/ubports/development/core/lomiri-wallpapers

Source: %name-%version.tar

BuildArch: noarch

%description
Lomiri is an operating environment optimized for touch based
human-machine interaction, but also supporting convergence (i.e.
switching between tablet/phone and desktop mode). Lomiri is the user
shell driving Ubuntu Touch based mobile devices.

This package contains the default Lomiri Operating Environment
wallpapers as shipped with current Ubuntu Touch.

%prep
%setup

%build
# nothing to build here

%install
mkdir -p %buildroot%_datadir/backgrounds

cp -av warty-final-ubuntu.png %buildroot%_datadir/backgrounds/
cp -avr 16.04/* %buildroot%_datadir/backgrounds/
cp -avr 20.04/* %buildroot%_datadir/backgrounds/

mv -v %buildroot%_datadir/backgrounds/warty-final-ubuntu.png \
      %buildroot%_datadir/backgrounds/warty-final-lomiri.png

cd %buildroot%_datadir/backgrounds/ && \
   ln -sv warty-final-lomiri.png lomiri-default-background.png

%files
%doc AUTHORS ChangeLog COPYING.CC0-1.0 COPYING.CC-BY-4.0 COPYING.CC-BY-SA-3.0 COPYING.CC-BY-SA-4.0 COPYING.Expat LICENSE README.md VERSION
%_datadir/backgrounds/*

%changelog
* Sun Jul 20 2025 Nikolay Strelkov <snk@altlinux.org> 20.04.0-alt1
- Initial build for Sisyphus
