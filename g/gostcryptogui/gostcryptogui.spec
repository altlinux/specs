%define gitrev 172e347

Name: gostcryptogui
Version: 0.1
Release: alt1.git%gitrev
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

Source0: %name-%version.tar

%description
A PyQt GUI for performing cryptographic operations over files using GOST algorithms

%prep
%setup -q

%build
%python_build

%install
%python_install
install -Dm 0755 gost-crypto-gui.py %buildroot%_bindir/gost-crypto-gui.py
install -Dm 0755 gost-crypto-gui-menu.py %buildroot%_datadir/nautilus-python/extensions/gost-crypto-gui-menu.py
install -Dm 0644 gost-crypto-gui.png %buildroot%_pixmapsdir/gost-crypto-gui.png
install -Dm 0644 gost-crypto-gui.desktop %buildroot%_desktopdir/gost-crypto-gui.desktop
install -Dm 0644 x-extension-enc.xml %buildroot%_xdgmimedir/applications/x-extension-enc.xml
install -Dm 0644 x-extension-sig.xml %buildroot%_xdgmimedir/applications/x-extension-sig.xml
install -Dm 0644 encrypted.png %buildroot%_iconsdir/encrypted.png
install -Dm 0644 signed.png %buildroot%_iconsdir/signed.png

%files
%doc README.md
%python_sitelibdir_noarch/*
%_bindir/gost-crypto-gui.py
%_datadir/nautilus-python/extensions/gost-crypto-gui-menu.py
%_pixmapsdir/gost-crypto-gui.png
%_desktopdir/gost-crypto-gui.desktop
%_xdgmimedir/applications/*.xml
%_iconsdir/encrypted.png
%_iconsdir/signed.png

%changelog
* Thu Nov 10 2016 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1.git172e347
- Initial build in Sisyphus
