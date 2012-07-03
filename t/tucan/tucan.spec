%define rel 1470
Name:		tucan
Version:	0.3.9
Release:	alt1.1.1
Summary:	Download and upload manager for file storage hosters
Group:		Networking/File transfer
License:	GPL
Source:		http://forja.rediris.es/frs/download.php/%rel/%name-%version.tar.gz
URL:		http://blog.tucaneando.com
BuildArch:	noarch
Packager:	Fr. Br. George <george@altlinux.ru>

BuildRequires:	python-dev

Requires:	tesseract tesseract-eng

%description
Tucan is a free and open source application designed for automatic
management of downloads and uploads at hosting sites like:

    * http://rapidshare.com/
    * http://megaupload.com/
    * http://gigasize.com/
    * http://mediafire.com/
    * http://4shared.com/
    * http://sendspace.com/
    * http://zshare.net/
    * http://filefactory.com/
    * http://easy-share.com/
    * http://badongo.com/
    * http://depositfiles.com/
    * http://hotfile.com/
    * ()

Main Features:

    * Written entirely in Python.
    * Graphical User Interface written in PyGTK (GTK+ toolkit).
    * Multiplatform (GNU/Linux, FreeBSD, Microsoft Windows).
    * Easy to expand with plugins.
    * Lightweight and fast.
    * Management of waits between downloads (anonymous access).
    * Captcha recognition where needed (like anonymous access to megaupload or gigasize).
    * Management of interchangeable links.

%prep
%setup -q

%install
make DESTDIR=%buildroot%prefix install
ln -sf $(relative $(realpath %buildroot%_bindir/%name) %buildroot%_bindir/%name) %buildroot%_bindir/%name 
rm -rf %buildroot%_pixmapsdir
install -D media/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
%find_lang %name

%files -f %name.lang
%doc CHANGELOG docs README TODO
%dir %_datadir/%name
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/%name.desktop
%_datadir/%name/*
%_man1dir/%name.*
%_bindir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.9-alt1.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt1.1
- Rebuilt with python 2.6

* Fri Oct 09 2009 Fr. Br. George <george@altlinux.ru> 0.3.9-alt1
- Version up

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 0.3.8-alt1
- Initial build from scratch

