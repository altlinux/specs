Name: ranger
Version: 1.9.0
Release: alt1

Summary(ru_RU.UTF-8): Консольный файл-менеджер
Summary: Console file manager
License: GPLv3
Group: File tools
Url: http://ranger.nongnu.org

Source0: %name-%version.tar.gz

%setup_python_module %name

BuildRequires: python-dev
BuildArch: noarch
Requires: %packagename = %version-%release

%description
ranger is a free console file manager that gives you greater
flexibility and a good overview of your files without having to leave
your *nix console. It visualizes the directory tree in two dimensions:
the directory hierarchy on one, lists of files on the other, with a
preview to the right so you know where you'll be going.

%description -l ru_RU.UTF-8
Свободный файловый менеджер, который дает вам большую гибкость и
хороший обзор ваших файлов без необходимости покидать консоль. Он
визуализирует дерево каталогов в двух измерениях: иерархия директорий
в одном и список файлов на другом, с возможностью предпросмотра.

%package -n %packagename
Summary: Supplemental module for %name, %summary
Group: Development/Python

%description -n %packagename
%summary

%prep
%setup
sed -i 's@#!/usr/bin/python -O@#!/usr/bin/python@' ranger.py

%build
%install
%makeinstall_std

%files
%_bindir/*
%doc %_defaultdocdir/%name
%_man1dir/*
%_desktopdir/%name.desktop

%files -n %packagename
%python_sitelibdir/*

%changelog
* Tue Jan 30 2018 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- NMU: Build new version (Closes: #31346).
- Add desktop file packaging to spec.

* Mon May 22 2017 Fr. Br. George <george@altlinux.ru> 1.8.1-alt1
- Autobuild version bump to 1.8.1

* Tue Apr 21 2015 Fr. Br. George <george@altlinux.ru> 1.7.0-alt1
- Autobuild version bump to 1.7.0

* Tue Apr 21 2015 Fr. Br. George <george@altlinux.ru> 1.6.1-alt1
- Version up
- Separate python module

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.1-alt2.git.c8f870.1
- Rebuild with Python-2.7

* Tue Feb 08 2011 Denis Klimov <zver@altlinux.org> 1.4.1-alt2.git.c8f870
- add BuildArch: noarch

* Wed Feb 02 2011 Denis Klimov <zver@altlinux.org> 1.4.1-alt1.git.c8f870
- Initial build for ALT Linux

