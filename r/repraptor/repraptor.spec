Name:		repraptor
Version:	0.2
Release:	alt1
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
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" RepRaptor.pro

%build
%make_build

%install
install -Dm 0755 RepRaptor %buildroot%_bindir/RepRaptor

%files
%doc README.md
%_bindir/RepRaptor

%changelog
* Thu Mar 05 2015 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Initail build in Sisyphus

