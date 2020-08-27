%define py_fname python3-module-ranger

Name: ranger
Version: 1.9.3
Release: alt1

Summary(ru_RU.UTF-8): Консольный файл-менеджер
Summary: Console file manager
License: GPLv3
Group: File tools
Url: https://ranger.github.io/

BuildArch: noarch

Source0: %name-%version.tar.gz

BuildRequires(pre): python3-dev
Requires: %py_fname = %version-%release

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

%package -n %py_fname
Summary: Supplemental module for %name, %summary
Group: Development/Python3

%description -n %py_fname
%summary

%prep
%setup

grep -rl '#!.*python' * | xargs sed -i 's@\(#!.*\)python@\1python3@'
grep -rl ' python ' ranger | egrep '[.](conf|sh)' | xargs sed -i 's@ python @ python3 @g'
grep -rl ' pygmentize ' ranger | xargs sed -i 's@ pygmentize @ pygmentize3 @g'


%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%doc %_defaultdocdir/%name
%_man1dir/*
%_desktopdir/%name.desktop

%files -n %py_fname
%python3_sitelibdir/*

%changelog
* Thu Aug 27 2020 Fr. Br. George <george@altlinux.ru> 1.9.3-alt1
- Autobuild version bump to 1.9.3

* Tue Feb 25 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.9.1-alt2
- Porting to python3.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1.qa1
- NMU: applied repocop patch

* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 1.9.1-alt1
- Autobuild version bump to 1.9.1

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

