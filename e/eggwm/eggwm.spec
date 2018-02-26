Name:		eggwm
Version:	0.2
Release:	alt1
Summary:	Egg Windows Manager
License:	GPL
Vendor:		José Expósito <jose.exposito89@gmail.com>
URL:		http://code.google.com/p/eggwm/
Group:		Graphical desktop/Other	
Packager: 	Andrey Cherepanov <cas@altlinux.org>

Source0:	%{name}-%{version}.tar.gz
Source1:	%name.desktop
Patch:		%name.diff

BuildRequires:	gcc-c++, qt4-devel
Prefix:		/usr

%description
EggWM is a window manager based on Qt 4 and Xlib.

%prep
%setup -q
%patch -p 0

%build
lrelease-qt4 %name.pro
DESTDIR=%buildroot PREFIX=/usr qmake-qt4 EggWM.pro
make

%install
install -D -m0755 %name %buildroot%_bindir/%name
install -D -m0655 %SOURCE1 %buildroot%_datadir/xsessions/%name.desktop

%files
%doc README.TXT
%_bindir/%name
%_datadir/xsessions/%name.desktop

%changelog
* Sun Feb 13 2011 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- New version 0.2

* Thu Jan 20 2011 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial build in Sisyphus

* Sun Jan 09 2011 TI_Eugene <ti.eugene@gmail.com> 0.1
- initial package in OBS
