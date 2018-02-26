Name:		easypaint
Version:	0.6.0
Release:	alt1
Summary:	Easy graphic editing program
License:	GPL
Group:		Graphics
URL:		http://qt-apps.org/content/show.php?content=140877
Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:	easyPaint.tar.gz
Source1:	%name.desktop

BuildRequires:	gcc-c++, qt4-devel

%description
Easy graphic editing program

%prep
%setup -q -n easyPaint

%build
qmake-qt4 PREFIX=/usr
make

%install
install -Dp -m0755 easyPaint %buildroot%_bindir/%name
install -Dp -m0644 icons/about/about.png %buildroot%_pixmapsdir/%name.png
install -Dp -m0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Fri Apr 15 2011 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build in Sisyphus

* Fri Apr 15 2011 TI_Eugene <ti.eugene@gmail.com>
- 0.6.0, initial OBS release
