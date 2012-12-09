%define orig_name GNS3
Name: gns3
Version: 0.8.3.1
Release: alt1

Summary: GNS-3  is a graphical network simulator

License: GPL
Group: File tools
Url: http://www.gns3.net/

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: http://downloads.sourceforge.net/gns-3/%orig_name-%version-src.tar.bz2
Source1: GNS3-icons.tar.gz
Source2: gns3.desktop
Source3: virtualbox.pth

BuildArch: noarch
Requires: python-module-sip dynamips

BuildRequires: python-devel

%description
GNS3 is a graphical network simulator that allows you to design
complex network topologies. You may run simulations or configure
devices ranging from simple workstations to powerful Cisco and Juniper
routers. It is based on Dynamips, an IOS emulator which allows users
to run IOS binary images from Cisco Systems, Pemu, an PIX firewall
emulator, Qemu and VirtualBox.

See 'virtualbox' and 'qemu' subpackages for guest support.

%package -n python-module-virtualbox
Summary: VirtualBox management support for python
Group: File tools
Requires: virtualbox-sdk

%description -n python-module-virtualbox
VirtualBox management support for python

%package virtualbox
Summary: VirtualBox guest support for GNS3
Group: File tools
Requires: %name = %version
Requires: python-module-virtualbox

%description virtualbox
VirtualBox guest support for GNS3

%package qemu
Summary: Qemu guest support for GNS3
Group: File tools
Requires: %name = %version
Requires: qemu-system

%description qemu
Qemu guest support for GNS3

%prep
%setup -n %orig_name-%version-src

%build
python setup.py build

%install
python setup.py install --root %buildroot
python setup.py install -O1 --root %buildroot
pushd %buildroot/%_bindir
popd
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

# virtualbox
install -d %buildroot/%python_sitelibdir
install -m 0644 %SOURCE3 %buildroot/%python_sitelibdir/virtualbox.pth

%files
%doc baseconfig*txt AUTHORS CHANGELOG README TODO
%_bindir/gns3*

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

%files -n python-module-virtualbox
%python_sitelibdir/virtualbox.pth

%files virtualbox
/usr/lib/gns3/vboxcontroller_4_1.py
/usr/lib/gns3/vboxwrapper.py
/usr/lib/gns3/tcp_pipe_proxy.py

%files qemu
/usr/lib/gns3/qemuwrapper.py

%changelog
* Sat Oct 27 2012 Terechkov Evgenii <evg@altlinux.org> 0.8.3.1-alt1
- 0.8.3.1

* Sun Dec 25 2011 Terechkov Evgenii <evg@altlinux.org> 0.8.2-alt1.beta
- Drop old tutorial (see http://www.gns3.net/documentation/ for latest version)
- 0.8.2 BETA
- New package and subpackages

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

