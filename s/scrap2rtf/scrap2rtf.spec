Name:		scrap2rtf
Version:	0.5
Release:	alt2
Summary:	A simple program to convert Shell Scrap Object File (.shs) to Rich Text Format

License:	GPLv3+
Group:		Office
URL:		https://itcrowd72.ru/project/scrap2rtf

Packager:	Andrey Cherepanov <cas@altlinux.org>

Source:		http://scrap2rtf.googlecode.com/files/%name-%version.tar.gz
Patch1:		%name-0.4-build-fix.patch
Patch2:		%name-fix-stream-output.patch

BuildRequires:	gcc-c++
BuildRequires:  qt6-base-devel

%description
%summary

%prep
%setup -q -n %name
%patch1 -p2
%patch2 -p2
qmake-qt6 scrap2rtf.pro

%build
%make

%install
%makeinstall_std INSTALL_ROOT=%buildroot
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README 
%_bindir/%name

%changelog
* Sun Sep 15 2024 Anton Midyukov <antohami@altlinux.org> 0.5-alt2
- NMU: rebuild with qmake-qt6

* Sun Jun 04 2017 Andrey Cherepanov <cas@altlinux.org> 0.5-alt1
- New version
- Fix project homepage

* Tue Nov 20 2012 Andrey Cherepanov <cas@altlinux.org> 0.4-alt1
- Initial build in Sisyphus

