%define orig_name GNS3
Name: gns3
Version: 0.7.3
Release: alt1.1

Summary: GNS-3  is a graphical network simulator

License: GPL
Group: File tools
Url: http://www.gns3.net/

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: http://downloads.sourceforge.net/gns-3/%orig_name-%version-src.tar.bz2
Source1: GNS3-icons.tar.gz
Source2: gns3.desktop
Source3: GNS3-0.5-tutorial.pdf

BuildArch: noarch
Requires: python-module-sip dynamips

# Automatically added by buildreq on Sat Mar 22 2008
BuildRequires: python-devel


%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple
workstations to powerful Cisco routers. It is based on Dynamips, an IOS emulator
which allows users to run IOS binary images from Cisco Systems and Pemu, an
PIX firewall emulator based on Qemu.

%prep
%setup -q -n %orig_name-%version-src

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot
%__python setup.py install -O1 --skip-build --root %buildroot
mkdir -p %buildroot/%_man1dir
install -m 0644 docs/man/gns3.1 %buildroot/%_man1dir

#desktop
install -d %buildroot/%_desktopdir
install -m 0644 %SOURCE2 %buildroot/%_desktopdir/%name.desktop

# icons
install -d %buildroot/%_miconsdir
install -d %buildroot/%_niconsdir
install -d %buildroot/%_liconsdir
tar xvzf %SOURCE1 -C %buildroot/%_iconsdir
mv %buildroot/%_iconsdir/mini/*.xpm %buildroot/%_miconsdir
rmdir %buildroot/%_iconsdir/mini
mv %buildroot/%_iconsdir/*.xpm %buildroot/%_niconsdir
mv %buildroot/%_iconsdir/large/*.xpm %buildroot/%_liconsdir
rmdir %buildroot/%_iconsdir/large

#docs
install -d %buildroot/%_docdir/%name-%version
install -m 0644 %SOURCE3 %buildroot/%_docdir/%name-%version/
for f in  AUTHORS CHANGELOG README TODO; do
	install -m 0644 $f %buildroot/%_docdir/%name-%version/
done

%files
%dir %_docdir/%name-%version
%_docdir/%name-%version/*
%_bindir/gns3

%dir %python_sitelibdir/GNS3
%dir %python_sitelibdir/GNS3/Config
%dir %python_sitelibdir/GNS3/Defaults
%dir %python_sitelibdir/GNS3/Dynagen
%dir %python_sitelibdir/GNS3/External
%dir %python_sitelibdir/GNS3/Globals
%dir %python_sitelibdir/GNS3/Langs
%dir %python_sitelibdir/GNS3/Link
%dir %python_sitelibdir/GNS3/Node
%dir %python_sitelibdir/GNS3/Ui
%dir %python_sitelibdir/GNS3/Ui/ConfigurationPages

%python_sitelibdir/GNS3/*.py
%python_sitelibdir/GNS3/*/*.py
%python_sitelibdir/GNS3/*/*/*.py
%python_sitelibdir/GNS3/*.pyc
%python_sitelibdir/GNS3/*/*.pyc
%python_sitelibdir/GNS3/*/*/*.pyc

%python_sitelibdir/GNS3/Dynagen/configspec
%python_sitelibdir/GNS3/Langs/*.qm
%python_sitelibdir/GNS3-*.egg-info

%ghost %python_sitelibdir/GNS3/*.pyo
%ghost %python_sitelibdir/GNS3/*/*.pyo
%ghost %python_sitelibdir/GNS3/*/*/*.pyo

%_man1dir/*
%_desktopdir/%name.desktop
%_miconsdir/*.xpm
%_niconsdir/*.xpm
%_liconsdir/*.xpm

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.3-alt1.1
- Rebuild with Python-2.7

* Fri Dec 31 2010 Terechkov Evgenii <evg@altlinux.org> 0.7.3-alt1
- 0.7.3

* Mon Sep 27 2010 Ilya Mashkin <oddity@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.1
- Rebuilt with python 2.6

* Sun Jan 11 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 0.6-alt1
- 0.6

* Mon May 12 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.5-alt1
- 0.5

* Sat Apr 26 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gns3

* Sat Mar 22 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.4-alt1
- inital build for ALT

