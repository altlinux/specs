%define _name pyNeighborhood

Name: pyneighborhood
Version: 0.4
Release: alt1.2.1

Summary: LinNeighborhood rewritten with GTK+2

License: %gpl2plus
Group: Networking/Other
Url: http://%name.sourceforge.net/
Packager: Alexey Rusakov <ktirf@altlinux.org>

Source: http://downloads.sourceforge.net/%name/%_name-%version.tar.bz2

BuildArch: noarch

BuildPreReq: rpm-build-licenses

BuildPreReq: python-devel

%description
pyNeighborhood is GTK+ 2 rewrite of a well-known GTK+ 1 tool LinNeighborhood(using pyGTK), so it is the GUI frontend for Samba tools, such as smbclient, smbmount etc. It's written in Python and uses the GTK+ 2 toolkit with pyGTK implementation. 

%prep
%setup -n %_name-%version

%build
./configure --prefix=%_prefix
%make_build

%install
%make_install DESTDIR=%buildroot install


%files
%_bindir/%_name
%_desktopdir/%_name.desktop
%dir %_datadir/%_name/icons
%_datadir/%_name/icons/*.png
%dir %_datadir/%_name/src
%_datadir/%_name/src/*.py
%_datadir/%_name/src/*.pyc

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.2
- Rebuilt with python 2.6

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for pyneighborhood

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt1.1
- Rebuilt with python-2.5.

* Mon Oct 08 2007 Alexey Rusakov <ktirf@altlinux.org> 0.4-alt1
- Initial Sisyphus package.

