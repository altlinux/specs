%define        _unpackaged_files_terminate_build 1

Name:          mytetra
Version:       1.44.161
Release:       alt0.1

Summary:       Simple cross-platform manager for data collecting
Summary(ru_RU.UTF-8): несложный кроссплатформенный менеджер накопления информации
License:       GPLv3
Group:         Office
Url:           http://webhamster.ru/site/page/index/articles/projectcode/105
Vcs:           https://github.com/xintrea/mytetra_dev

Source:        %name-%version.tar
Patch:         fix-compilation-1.4.161.patch
BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel

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
%autopatch
echo "QMAKE_CXXFLAGS = %optflags" >> %name.pro
subst 's/^TARGET_OS=.*$/TARGET_OS=ANY_OS/' app/*.pro
subst 's|/usr/local/bin|%_bindir|' app/*.pro

%build
qmake-qt5 %name.pro
%make_build

%install
%makeinstall_std TARGET_OS=ANY_OS INSTALL_ROOT=%buildroot BINARY_INSTALL_PATH=%_bindir install
rm -f %buildroot/usr/share/icons/hicolor/scalable/apps/mytetra.svg
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=TextTools \
	%buildroot%_desktopdir/mytetra.desktop

%files
%doc *.txt *.md
%_bindir/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png

%changelog
* Thu Oct 19 2023 Pavel Skrylev <majioa@altlinux.org> 1.44.161-alt0.1
- ^ 1.44.160 -> 1.44[.161]
- ! fixed compilation to avoid incompatible types bug

* Tue May 16 2023 Andrey Cherepanov <cas@altlinux.org> 1.44.160-alt1
- New version.

* Wed Jun 30 2021 Grigory Ustinov <grenka@altlinux.org> 1.42.2-alt2
- Fixed BuildRequires.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.42.2-alt1.qa1
- NMU: applied repocop patch

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

