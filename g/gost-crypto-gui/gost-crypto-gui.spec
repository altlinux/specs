%define gitrev 4b7a47a

Name: gost-crypto-gui
Version: 0.3
Release: alt0.5.a.git%gitrev
Summary: A PyQt GUI for performing cryptographic operations over files using GOST algorithms

License: MIT
Packager: Andrey Cherepanov <cas@altlinux.org>
Group: Security/Networking
Url: http://github.com/bmakarenko/gost-crypto-gui

BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-xdg
BuildRequires: python-module-setuptools

%filter_from_requires /^python2.7(nautilus)/d
Requires: nautilus-python

BuildArch: noarch

Source0: %name.tar

Provides:  gostcryptogui = %EVR
Obsoletes: gostcryptogui < %EVR

%description
A PyQt GUI for performing cryptographic operations over files using GOST
algorithms. Requires CryproPro (http://www.cryptopro.ru).

%prep
%setup -q

%build
%python_build
for dir in nautilus caja; do
  pushd "$dir"
  chmod +x gost-crypto-gui-emblem.py
  python -m py_compile gost-crypto-gui-menu.py
  python -m py_compile gost-crypto-gui-emblem.py
  popd
done

%install
%python_install
install -Dm 0755 gost-crypto-gui.py %buildroot%_bindir/gost-crypto-gui.py

for dir in nautilus caja; do
  pushd "$dir"
  mkdir -p %buildroot%_datadir/$dir-python/extensions
  cp gost-crypto-gui-menu.py* gost-crypto-gui-emblem.py* %buildroot%_datadir/$dir-python/extensions
  popd
done

install -Dm 0644 gost-crypto-gui.png %buildroot%_pixmapsdir/gost-crypto-gui.png
install -Dm 0644 gost-crypto-gui.desktop %buildroot%_desktopdir/gost-crypto-gui.desktop
mkdir -p %buildroot%_xdgmimedir/application
cp x-extension-*.xml %buildroot%_xdgmimedir/application
mkdir -p %buildroot%_iconsdir
cp -av *.png %buildroot%_iconsdir
rm -f %buildroot%_iconsdir/gost-crypto-gui.png

%files
%doc README.md
%python_sitelibdir_noarch/*
%_bindir/gost-crypto-gui.py
%_datadir/nautilus-python/extensions/*.py*
%_datadir/caja-python/extensions/*.py*
%_pixmapsdir/gost-crypto-gui.png
%_desktopdir/gost-crypto-gui.desktop
%_xdgmimedir/application/*.xml
%_iconsdir/*.png

%changelog
* Fri Apr 20 2018 Andrey Cherepanov <cas@altlinux.org> 0.3-alt0.5.a.git4b7a47a
- New version (ALT #34836).

* Sun Sep 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.3-alt0.4.a.git201ea87
- Rename to gost-crypto-gui as original upstream name

* Thu Aug 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.3-alt0.3.a.git201ea87
- (upstream fix) Single quote in certificate fields

* Thu Jun 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.3-alt0.2.a.git0c6d930
- [upstreram fix] 'Open in folder' and 'send via email' buttons on messagebox

* Tue May 30 2017 Andrey Cherepanov <cas@altlinux.org> 0.3-alt0.1.a.gita283bf5
- New version
- Fix mime type location

* Tue Dec 20 2016 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1.git5d1e7ad
- New version

* Thu Nov 10 2016 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1.git172e347
- Initial build in Sisyphus
