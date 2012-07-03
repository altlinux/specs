Name: mytetra
Version: 1.30.1
Release: alt1

Summary: Simple cross-platform manager for data collecting
Summary(ru_RU.UTF-8): несложный кроссплатформенный менеджер накопления информации
License: GPLv3
Group: Office
Url: http://webhamster.ru/site/page/index/articles/projectcode/105
Packager: Malo Skryleve <malo@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt4
# Automatically added by buildreq on Wed Mar 16 2011
BuildRequires: gcc-c++ libqt4-network libqt4-svg libqt4-xml phonon-devel
BuildRequires: desktop-file-utils

%description
No desc.

%description -l ru_RU.UTF-8
Программа MyTetra — это несложный кроссплатформенный менеджер накопления
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
PATH=$PATH:%_qt4dir/bin qmake %name.pro
%make

%install
%make_install INSTALL_ROOT=%buildroot \
	BINARY_INSTALL_PATH=%_bindir install
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=TextTools \
	%buildroot%_desktopdir/mytetra.desktop

%files
%doc readme.txt
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/scalable/apps/*

%changelog
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

