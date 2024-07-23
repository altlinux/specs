Name: tuxpaint-stamps
Version: 2024.07.17
Release: alt1

Summary: This is a collection of 'rubber stamp' images for Tux Paint
Summary(ru_RU.UTF8): Колекция изображений 'штампов' для программы Tux Paint
License: GPL-2.0
Group: Graphics

URL: https://www.tuxpaint.org
Source: %name-%version.tar.gz

BuildRequires: gettext-tools
Requires: tuxpaint

BuildArch: noarch

%description
This is a collection of 'rubber stamp' images for Tux Paint.
Tux Paint - A simple drawing program for children.

%description -l ru_RU.UTF8
Коллекция изображений 'штампов' для программы "Tux Paint"
"Tux Paint" является детской программой для рисования.

%prep
%setup

%build
# Compile locales by hand.
pushd po
    for f in *.po; do
        t=${f#%name-}
        msgfmt -v -o "${t%%.po}.mo" "$f"
    done
popd

%install
install -d %buildroot%_datadir/tuxpaint/stamps
make install-all PREFIX=%buildroot%_prefix

# Install locales by hand.
pushd po
    for f in *.mo; do
        install -pD -m644 "$f" "%buildroot%_datadir/locale/${f%%.mo}/LC_MESSAGES/%name.mo"
    done
popd

# License is bad on this file, Creative Commons Sampling Plus 1.0 is non-free.
rm -rf %buildroot%_datadir/tuxpaint/stamps/vehicles/emergency/firetruck.ogg

%find_lang %name

%files -f %name.lang
%doc docs/*.txt
%_datadir/tuxpaint/stamps/*

%changelog
* Tue Jul 23 2024 Grigory Ustinov <grenka@altlinux.org> 2024.07.17-alt1
- Build new version.

* Tue Apr 02 2024 Grigory Ustinov <grenka@altlinux.org> 2024.01.29-alt1
- Build new version.

* Wed May 17 2023 Grigory Ustinov <grenka@altlinux.org> 2023.04.02-alt1
- Build new version.

* Fri Jul 22 2022 Grigory Ustinov <grenka@altlinux.org> 2022.06.04-alt1
- Build new version.

* Mon Dec 27 2021 Grigory Ustinov <grenka@altlinux.org> 2021.11.25-alt1
- Build new version.

* Thu Jul 01 2021 Grigory Ustinov <grenka@altlinux.org> 2021.06.28-alt1
- Build new version.

* Fri Jan 15 2021 Grigory Ustinov <grenka@altlinux.org> 2020.12.27-alt1
- Build new version.

* Mon Sep 28 2020 Grigory Ustinov <grenka@altlinux.org> 2020.05.29-alt1
- Build new version (Closes: #38961).

* Tue Oct 16 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2009.06.28-alt2
- Fix build

* Tue Jun 30 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2009.06.28-alt1
- Update to 2009.06.28

* Fri Mar 14 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 2008.03.01-alt1
- Update to 2008.03.01

* Wed Nov 28 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2007.11.21-alt1
- Update to 2007.11.21

* Tue Oct 30 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2007.07.01-alt1
- Update to 2007.07.01

* Mon Oct 23 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 2006.10.21-alt0
- Update to 2006.10.21

* Thu Dec 01 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 2005.11.25-alt0
- built for ALT Linux
