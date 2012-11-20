Name:		scrap2rtf
Version:	0.4
Release:	alt1
Summary:	A simple program to convert Shell Scrap Object File (.shs) to Rich Text Format

License:	GPLv3+
Group:		Office
URL:		http://code.google.com/p/scrap2rtf/

Packager:	Andrey Cherepanov <cas@altlinux.org>

Source:		http://scrap2rtf.googlecode.com/files/%name-%version.tar.gz
Patch1:		%name-0.4-build-fix.patch

BuildRequires:	gcc-c++
BuildRequires:  libqt4-devel

%description
%summary

%prep
%setup -q -n %name
%patch1 -p2
qmake-qt4 scrap2rtf.pro

%build
%make

%install
%makeinstall_std INSTALL_ROOT=%buildroot
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README 
%_bindir/%name

%changelog
* Tue Nov 20 2012 Andrey Cherepanov <cas@altlinux.org> 0.4-alt1
- Initial build in Sisyphus

