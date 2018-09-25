%define _unpackaged_files_terminate_build 1

Name: dreampie
Version: 1.3.0
Release: alt1.git20171111
BuildArch: noarch

Summary: the Python shell you've always dreamed about
License: GPLv3
Group: Development/Python
Url: http://dreampie.sourceforge.net/

# https://github.com/noamraph/dreampie.git
Source: %name-%version.tar

BuildRequires: python-devel
BuildRequires: desktop-file-utils

%py_requires gtk.glade

%description
DreamPie is an interactive Python shell based on a new concept: the
window is divided into the history box, which lets you view previous
commands and their output, and the code box, where you write your
code. This allows you to edit any amount of code, just like in your
favorite editor, and execute it when it's ready. You can also copy
code from anywhere, edit it and run it instantly.

%prep
%setup

%build
%python_build

%install
%python_install

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=IDE \
	%buildroot%_desktopdir/dreampie.desktop

%files
%_bindir/%name
%_man1dir/%name.1*
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_pixmapsdir/%name.svg
%python_sitelibdir/%{name}lib
%python_sitelibdir/%name-*-*.egg-info

%changelog
* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.0-alt1.git20171111
- Updated to upstream version 1.3.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for dreampie

* Thu Aug 05 2010 Alexander Myltsev <avm@altlinux.ru> 1.1-alt1
- Initial build for Sisyphus.

