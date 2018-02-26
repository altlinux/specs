Name: ranger
Version: 1.4.1
Release: alt2.git.c8f870.1

Summary: Console file manager 
Summary(ru_RU.UTF-8): Консольный файл-менеджер
License: GPLv3
Group: File tools
Url: http://ranger.nongnu.org

Source0: %name-%version.tar

BuildRequires: python-dev
BuildArch: noarch

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


%prep
%setup

%build

%install
%makeinstall_std

%files 
%_bindir/%name
%doc CHANGELOG README COPYING
%_man1dir/%{name}*
%python_sitelibdir/%name
%python_sitelibdir/*.egg-info

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.1-alt2.git.c8f870.1
- Rebuild with Python-2.7

* Tue Feb 08 2011 Denis Klimov <zver@altlinux.org> 1.4.1-alt2.git.c8f870
- add BuildArch: noarch

* Wed Feb 02 2011 Denis Klimov <zver@altlinux.org> 1.4.1-alt1.git.c8f870
- Initial build for ALT Linux

