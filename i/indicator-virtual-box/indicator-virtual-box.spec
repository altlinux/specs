%define _unpackaged_files_terminate_build 1

Name: indicator-virtual-box
Version: 1.0.74
Release: alt1

Summary: Application indicator for VirtualBox virtual machines
License: GPL-3.0
Group: Graphical desktop/Other
URL: https://launchpad.net/~thebernmeister/+archive/ubuntu/ppa

BuildRequires(pre): rpm-build-python3

Requires: virtualbox
Requires: typelib(AyatanaAppIndicator3)
Requires: wmctrl
Requires: python3(notify2)

ExclusiveArch: x86_64

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
A user can start any of their virtual machines from the indicator
or select any virtual machine to be automatically started.

%prep
%setup
%patch -p1

%build
# nothing to build here

%install
# main components
install -Dm 644 indicator-virtual-box.py.desktop -t %buildroot%_desktopdir/

install -Dm 755 src/indicatorbase.py -t %buildroot/%_datadir/indicator-virtual-box/
install -Dm 755 src/indicator-virtual-box.py -t %buildroot/%_datadir/indicator-virtual-box/
install -Dm 755 src/virtualmachine.py -t %buildroot/%_datadir/indicator-virtual-box/

install -Dm 644 po/ru/indicator-virtual-box.mo -t %buildroot/%_datadir/locale/ru/LC_MESSAGES

# icons
install -Dm 644 icons/hicolor/indicator-virtual-box.svg -t %buildroot/%_iconsdir/hicolor/scalable/apps/
install -Dm 644 icons/hicolor/indicator-virtual-box.svg -t %buildroot/%_iconsdir/hicolor/apps/16/
install -Dm 644 icons/hicolor/indicator-virtual-box.svg -t %buildroot/%_iconsdir/hicolor/apps/22/
install -Dm 644 icons/hicolor/indicator-virtual-box.svg -t %buildroot/%_iconsdir/hicolor/apps/24/
install -Dm 644 icons/hicolor/indicator-virtual-box.svg -t %buildroot/%_iconsdir/hicolor/apps/48/

install -Dm 644 icons/Adwaita/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Adwaita/scalable/apps/
install -Dm 644 icons/Adwaita/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Adwaita/apps/16/
install -Dm 644 icons/Adwaita/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Adwaita/apps/22/
install -Dm 644 icons/Adwaita/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Adwaita/apps/24/
install -Dm 644 icons/Adwaita/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Adwaita/apps/48/

install -Dm 644 icons/Ambiant-MATE/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Ambiant-MATE/scalable/apps/
install -Dm 644 icons/Ambiant-MATE/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Ambiant-MATE/apps/16/
install -Dm 644 icons/Ambiant-MATE/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Ambiant-MATE/apps/22/
install -Dm 644 icons/Ambiant-MATE/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Ambiant-MATE/apps/24/
install -Dm 644 icons/Ambiant-MATE/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Ambiant-MATE/apps/48/

install -Dm 644 icons/breeze/indicator-virtual-box.svg -t %buildroot/%_iconsdir/breeze/scalable/apps/
install -Dm 644 icons/breeze/indicator-virtual-box.svg -t %buildroot/%_iconsdir/breeze/apps/16/
install -Dm 644 icons/breeze/indicator-virtual-box.svg -t %buildroot/%_iconsdir/breeze/apps/22/
install -Dm 644 icons/breeze/indicator-virtual-box.svg -t %buildroot/%_iconsdir/breeze/apps/24/
install -Dm 644 icons/breeze/indicator-virtual-box.svg -t %buildroot/%_iconsdir/breeze/apps/48/

install -Dm 644 icons/breeze-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/breeze-dark/scalable/apps/
install -Dm 644 icons/breeze-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/breeze-dark/apps/16/
install -Dm 644 icons/breeze-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/breeze-dark/apps/22/
install -Dm 644 icons/breeze-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/breeze-dark/apps/24/
install -Dm 644 icons/breeze-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/breeze-dark/apps/48/

install -Dm 644 icons/elementary-xfce-darker/indicator-virtual-box.svg -t %buildroot/%_iconsdir/elementary-xfce-darker/scalable/apps/
install -Dm 644 icons/elementary-xfce-darker/indicator-virtual-box.svg -t %buildroot/%_iconsdir/elementary-xfce-darker/apps/16/
install -Dm 644 icons/elementary-xfce-darker/indicator-virtual-box.svg -t %buildroot/%_iconsdir/elementary-xfce-darker/apps/22/
install -Dm 644 icons/elementary-xfce-darker/indicator-virtual-box.svg -t %buildroot/%_iconsdir/elementary-xfce-darker/apps/24/
install -Dm 644 icons/elementary-xfce-darker/indicator-virtual-box.svg -t %buildroot/%_iconsdir/elementary-xfce-darker/apps/48/

install -Dm 644 icons/ePapirus/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ePapirus/scalable/apps/
install -Dm 644 icons/ePapirus/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ePapirus/apps/16/
install -Dm 644 icons/ePapirus/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ePapirus/apps/22/
install -Dm 644 icons/ePapirus/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ePapirus/apps/24/
install -Dm 644 icons/ePapirus/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ePapirus/apps/48/

install -Dm 644 icons/Lubuntu/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Lubuntu/scalable/apps/
install -Dm 644 icons/Lubuntu/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Lubuntu/apps/16/
install -Dm 644 icons/Lubuntu/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Lubuntu/apps/22/
install -Dm 644 icons/Lubuntu/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Lubuntu/apps/24/
install -Dm 644 icons/Lubuntu/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Lubuntu/apps/48/

install -Dm 644 icons/Papirus/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Papirus/scalable/apps/
install -Dm 644 icons/Papirus/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Papirus/apps/16/
install -Dm 644 icons/Papirus/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Papirus/apps/22/
install -Dm 644 icons/Papirus/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Papirus/apps/24/
install -Dm 644 icons/Papirus/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Papirus/apps/48/

install -Dm 644 icons/Papirus-Light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Papirus-Light/scalable/apps/
install -Dm 644 icons/Papirus-Light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Papirus-Light/apps/16/
install -Dm 644 icons/Papirus-Light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Papirus-Light/apps/22/
install -Dm 644 icons/Papirus-Light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Papirus-Light/apps/24/
install -Dm 644 icons/Papirus-Light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Papirus-Light/apps/48/

install -Dm 644 icons/Pocillo/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Pocillo/scalable/apps/
install -Dm 644 icons/Pocillo/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Pocillo/apps/16/
install -Dm 644 icons/Pocillo/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Pocillo/apps/22/
install -Dm 644 icons/Pocillo/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Pocillo/apps/24/
install -Dm 644 icons/Pocillo/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Pocillo/apps/48/

install -Dm 644 icons/ubuntu-mono-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ubuntu-mono-dark/scalable/apps/
install -Dm 644 icons/ubuntu-mono-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ubuntu-mono-dark/apps/16/
install -Dm 644 icons/ubuntu-mono-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ubuntu-mono-dark/apps/22/
install -Dm 644 icons/ubuntu-mono-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ubuntu-mono-dark/apps/24/
install -Dm 644 icons/ubuntu-mono-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ubuntu-mono-dark/apps/48/

install -Dm 644 icons/ubuntu-mono-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ubuntu-mono-light/scalable/apps/
install -Dm 644 icons/ubuntu-mono-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ubuntu-mono-light/apps/16/
install -Dm 644 icons/ubuntu-mono-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ubuntu-mono-light/apps/22/
install -Dm 644 icons/ubuntu-mono-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ubuntu-mono-light/apps/24/
install -Dm 644 icons/ubuntu-mono-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/ubuntu-mono-light/apps/48/

install -Dm 644 icons/Yaru/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru/scalable/apps/
install -Dm 644 icons/Yaru/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru/apps/16/
install -Dm 644 icons/Yaru/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru/apps/22/
install -Dm 644 icons/Yaru/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru/apps/24/
install -Dm 644 icons/Yaru/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru/apps/48/

install -Dm 644 icons/Yaru-MATE-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-MATE-dark/scalable/apps/
install -Dm 644 icons/Yaru-MATE-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-MATE-dark/apps/16/
install -Dm 644 icons/Yaru-MATE-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-MATE-dark/apps/22/
install -Dm 644 icons/Yaru-MATE-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-MATE-dark/apps/24/
install -Dm 644 icons/Yaru-MATE-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-MATE-dark/apps/48/

install -Dm 644 icons/Yaru-MATE-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-MATE-light/scalable/apps/
install -Dm 644 icons/Yaru-MATE-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-MATE-light/apps/16/
install -Dm 644 icons/Yaru-MATE-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-MATE-light/apps/22/
install -Dm 644 icons/Yaru-MATE-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-MATE-light/apps/24/
install -Dm 644 icons/Yaru-MATE-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-MATE-light/apps/48/

install -Dm 644 icons/Yaru-unity-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-unity-dark/scalable/apps/
install -Dm 644 icons/Yaru-unity-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-unity-dark/apps/16/
install -Dm 644 icons/Yaru-unity-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-unity-dark/apps/22/
install -Dm 644 icons/Yaru-unity-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-unity-dark/apps/24/
install -Dm 644 icons/Yaru-unity-dark/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-unity-dark/apps/48/

install -Dm 644 icons/Yaru-unity-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-unity-light/scalable/apps/
install -Dm 644 icons/Yaru-unity-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-unity-light/apps/16/
install -Dm 644 icons/Yaru-unity-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-unity-light/apps/22/
install -Dm 644 icons/Yaru-unity-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-unity-light/apps/24/
install -Dm 644 icons/Yaru-unity-light/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-unity-light/apps/48/

install -Dm 644 icons/menta/indicator-virtual-box.svg -t %buildroot/%_iconsdir/menta/apps/16/
install -Dm 644 icons/menta/indicator-virtual-box.svg -t %buildroot/%_iconsdir/menta/apps/22/
install -Dm 644 icons/menta/indicator-virtual-box.svg -t %buildroot/%_iconsdir/menta/apps/24/
install -Dm 644 icons/menta/indicator-virtual-box.svg -t %buildroot/%_iconsdir/menta/apps/48/
install -Dm 644 icons/menta/indicator-virtual-box.svg -t %buildroot/%_iconsdir/menta/scalable/apps/

install -Dm 644 icons/Yaru-olive/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-olive/apps/16/
install -Dm 644 icons/Yaru-olive/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-olive/apps/22/
install -Dm 644 icons/Yaru-olive/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-olive/apps/24/
install -Dm 644 icons/Yaru-olive/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-olive/apps/48/
install -Dm 644 icons/Yaru-olive/indicator-virtual-box.svg -t %buildroot/%_iconsdir/Yaru-olive/scalable/apps/

install -Dm 644 icons/mate/indicator-virtual-box.svg -t %buildroot/%_iconsdir/mate/apps/16/
install -Dm 644 icons/mate/indicator-virtual-box.svg -t %buildroot/%_iconsdir/mate/apps/22/
install -Dm 644 icons/mate/indicator-virtual-box.svg -t %buildroot/%_iconsdir/mate/apps/24/
install -Dm 644 icons/mate/indicator-virtual-box.svg -t %buildroot/%_iconsdir/mate/apps/48/
install -Dm 644 icons/mate/indicator-virtual-box.svg -t %buildroot/%_iconsdir/mate/scalable/apps/

%find_lang %name --all-name

%files -f %{name}.lang
%_desktopdir/*.desktop
%dir %_datadir/indicator-virtual-box
%_datadir/indicator-virtual-box/indicatorbase.py
%_datadir/indicator-virtual-box/indicator-virtual-box.py
%_datadir/indicator-virtual-box/virtualmachine.py

%_iconsdir/Adwaita/*/*/indicator-virtual-box.svg
%_iconsdir/Ambiant-MATE/*/*/indicator-virtual-box.svg
%_iconsdir/Lubuntu/*/*/indicator-virtual-box.svg
%_iconsdir/Papirus-Light/*/*/indicator-virtual-box.svg
%_iconsdir/Papirus/*/*/indicator-virtual-box.svg
%_iconsdir/Pocillo/*/*/indicator-virtual-box.svg
%_iconsdir/Yaru-MATE-dark/*/*/indicator-virtual-box.svg
%_iconsdir/Yaru-MATE-light/*/*/indicator-virtual-box.svg
%_iconsdir/Yaru-unity-dark/*/*/indicator-virtual-box.svg
%_iconsdir/Yaru-unity-light/*/*/indicator-virtual-box.svg
%_iconsdir/Yaru/*/*/indicator-virtual-box.svg
%_iconsdir/breeze-dark/*/*/indicator-virtual-box.svg
%_iconsdir/breeze/*/*/indicator-virtual-box.svg
%_iconsdir/ePapirus/*/*/indicator-virtual-box.svg
%_iconsdir/elementary-xfce-darker/*/*/indicator-virtual-box.svg
%_iconsdir/hicolor/*/*/indicator-virtual-box.svg
%_iconsdir/ubuntu-mono-dark/*/*/indicator-virtual-box.svg
%_iconsdir/ubuntu-mono-light/*/*/indicator-virtual-box.svg

%_iconsdir/menta/*/*/indicator-virtual-box.svg
%_iconsdir/Yaru-olive/*/*/indicator-virtual-box.svg
%_iconsdir/mate/*/*/indicator-virtual-box.svg

%changelog
* Fri Oct 17 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.74-alt1
- Initial build for Sisyphus
