Name: mytetra
Version: 1.42.2
Release: alt1

Summary: Simple cross-platform manager for data collecting
Summary(ru_RU.UTF-8): несложный кроссплатформенный менеджер накопления информации
License: GPLv3
Group: Office
Url: http://webhamster.ru/site/page/index/articles/projectcode/105
Packager: Malo Skryleve <malo@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5
# Automatically added by buildreq on Wed Mar 16 2011
BuildRequires: gcc-c++ phonon-devel desktop-file-utils
BuildRequires: qt5-base-devel qt5-svg-devel

%description
MyTetra is open source and cross platform personal manager for information
accumulation. It is powerful program for data memorization and structuring
notes. All notes are organized in tree structure (usually by "basic"
attribute), and also supplies with keywords(tags). The main task of Mytetra
is to provide a natural, intuitive interface for writing notes and provide
the ability to quickly navigate through the tree and convenient search.

%description -l ru_RU.UTF-8
Программа MyTetra — это открытый и кроссплатформенный менеджер накопления
информации. Программа предназначена для хранения статей и заметок.
Все записи организуются в древовидную структуру (обычно по «основному»
признаку), а так же снабжаются ключевыми словами-тегами. Основная задача
MyTetra — предоставить естественный, интуитивно-понятный интерфейс для
написания заметок, обеспечить возможность быстрой навигации по дереву и
удобный поиск.

%prep
%setup

%build
sed 's,\(mytetra_binary.path=\).*,\1%_bindir,g' -i %name.pro
sed 's,/usr/local/bin,%_bindir,g' -i %name.pro
echo "QMAKE_CXXFLAGS = %optflags" >> %name.pro
qmake-qt5 %name.pro

%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot BINARY_INSTALL_PATH=%_bindir install
rm -f %buildroot/usr/share/icons/hicolor/scalable/apps/mytetra.svg

%files
%doc readme.txt
%_bindir/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png

%changelog
* Mon Jan 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.42.2-alt1
- Build new version (Closes: #34426).
- Transfer to qt5.
- Add eng description.

* Fri Dec 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.30.1-alt1.1
- Fixed build with glibc 2.16

* Thu Nov 17 2011 Malo Skryleve <malo@altlinux.org> 1.30.1-alt1
- repocop cronbuild 20111117. At your service.

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.28-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for mytetra

* Fri Apr 15 2011 Malo Skryleve <malo@altlinux.org> 1.28-alt3
- Fixed spec file

* Thu Mar 31 2011 Malo Skryleve <malo@altlinux.org> 1.28-alt2
- Fixed %%files section

* Wed Mar 16 2011 Malo Skryleve <malo@altlinux.org> 1.28-alt1
- initial build for ALT Linux Sisyphus

