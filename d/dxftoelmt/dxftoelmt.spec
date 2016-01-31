# TODO: desktop file

Name:     dxftoelmt
Version:  151115
Release:  alt1

Summary:  Utility that converts a DXF element to a elmt element
License:  GPL-2.0+ and CC-BY-3.0
Group:    Engineering
Url:      http://qelectrotech.org/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel

%description
The converter element is a small utility that converts a DXF element.
to a elmt element.

%prep
%setup

%build
DESTDIR=%buildroot PREFIX=/usr qmake-qt5 DXFtoQET.pro
%make_build

%install
install -Dm 0755 DXFtoQET %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Sun Jan 31 2016 Andrey Cherepanov <cas@altlinux.org> 151115-alt1
- Initial build

