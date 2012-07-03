Name:		rviewer
Version:	0.5
Release:	alt1

Summary:	RViewer image viewer
License:	GPL
Group:		Graphics
URL:            http://rniamo.is-a-geek.com/mu/2009/05/16/rviewer-v05/
Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:	%name.tar.gz
Source1:	%name.desktop
Source2:	%name.png

BuildRequires:	gcc-c++, libqt4-devel

%description
RViewer image viewer

%prep
%setup -q -n trunk

%build
qmake-qt4
make

%install
%makeinstall release INSTALL_ROOT=%{buildroot}
install -Dp -m 0755 RViewer %{buildroot}%_bindir/%name
install -Dp -m 0644 %SOURCE1 %{buildroot}%_desktopdir/%name.desktop
install -Dp -m 0644 %SOURCE2 %{buildroot}%_pixmapsdir/%name.png

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Mon Feb 07 2011 Andrey Cherepanov <cas@altlinux.org> 0.5-alt1
- Initial build in Sisyphus

