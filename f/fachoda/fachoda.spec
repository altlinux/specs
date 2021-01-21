Name: fachoda
Version: 2.1
Release: alt4

Summary: Flight simulator/arcade game
License: GPLv3
Group: Games/Arcade
Url: http://rixed.github.io/fachoda-complex/

Packager: Alexey Appolonov <alexey@altlinux.org>

# https://github.com/rixed/fachoda-complex/archive/release/2.1.zip
Source: %name-%version.tar
Source1: %name.desktop

Patch1: %name-2.1-alt-e2k-nested-func.patch

BuildRequires: libSDL-devel
BuildRequires: libopenal-devel
BuildRequires: libjpeg-devel

%description
Fachoda-complex is a flight simulator/arcade game for Linux,
tailored for small hardware configs.

%prep
%setup
%patch1 -p2

%build
export CFLAGS="$CFLAGS -fcommon"
%make_build PREFIX=%_prefix -C src

%install
%makeinstall_std PREFIX=%_prefix -C src
mkdir -p %buildroot%_desktopdir/
install -m0644 %SOURCE1 %buildroot%_desktopdir/

%files
%_gamesbindir/%name
%_libexecdir/games/%name
%_defaultdocdir/%name
%_desktopdir/%name.desktop

%changelog
* Thu Jan 21 2021 Leontiy Volodin <lvol@altlinux.org> 2.1-alt4
- Fixed build with gcc10.

* Thu Oct 12 2017 Alexey Appolonov <alexey@altlinux.org> 2.1-alt3
- Converted nested function to external (e2k).
- Added desktop file.
- Packed upstream sources instead of changed for alt2 release.
- Restored first changelog entry.

* Mon Oct 2 2017 Alexey Appolonov <alexey@altlinux.org> 2.1-alt2
- Second ALT Linux release.

* Tue Sep 27 2017 Alexey Appolonov <alexey@altlinux.org> 2.1-alt1
- Initial ALT Linux release.
