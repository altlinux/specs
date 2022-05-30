Name:		repraptor
Version:	0.3.8
Release:	alt2
Summary:	A Qt RepRap gcode sender/host controller

License:	GPLv2
Group:		Graphics
URL:		https://github.com/NeoTheFox/RepRaptor

Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:	%name-%version.tar

BuildRequires:  gcc-c++ qt5-base-devel qt5-serialport-devel

%description
A Qt RepRap gcode sender/host controller aimed to be fast and
minimalistic.

Right now the project is in early stage. This means some features are
still absent, but it is already usable.

%prep
%setup -q

%build
%qmake_qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" PREFIX=%_prefix RepRaptor.pro
%make_build

%install
%installqt5

%files
%doc README.md
%_bindir/RepRaptor
%_desktopdir/*.desktop
%_iconsdir/%name.png

%changelog
* Mon May 30 2022 Andrey Cherepanov <cas@altlinux.org> 0.3.8-alt2
- Packaged desktop file and icons (ALT #42871).

* Tue Jul 25 2017 Anton Midyukov <antohami@altlinux.org> 0.3.8-alt1
- New version 0.3.8

* Fri Mar 13 2015 Andrey Cherepanov <cas@altlinux.org> 0.3.5-alt1
- New version

* Thu Mar 05 2015 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Initial build in Sisyphus
