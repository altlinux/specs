Name: wordtsar
Version: 0.3.719
Release: alt1

Summary: A WordStar 7.0D Document mode clone
License: AGPL-3.0-or-later
Group: Editors
Url: https://wordtsar.ca/

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5
BuildRequires: qt5-base-devel

%description
A WordStar 7.0D Document mode clone. It loads WordStar 4, WordStar 7, DOCX
and RTF files, and saves in WordStar 7 and RTF format.

%prep
%setup
sed -i 's!\.\./!!g' %name.pro
sed -i 's!Exec=WordTsar!Exec=%name!' linuxdeploy/WordTsar.desktop

%build
%qmake_qt5 %name.pro
%make_build

%install
install -D -m755 WordTsar %buildroot%_bindir/%name
install -D -m644 linuxdeploy/%name.png %buildroot%_datadir/pixmaps/%name.png
install -D -m644 linuxdeploy/WordTsar.desktop %buildroot%_datadir/applications/%name.desktop

%files
%doc LICENSE.md
%_bindir/%name
%_datadir/pixmaps/%name.png
%_datadir/applications/%name.desktop

%changelog
* Tue Sep 23 2025 Andrew A. Vasilyev <andy@altlinux.org> 0.3.719-alt1
- Initial build for ALT.

