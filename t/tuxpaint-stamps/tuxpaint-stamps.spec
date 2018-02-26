Name: tuxpaint-stamps
Version: 2009.06.28
Release: alt1

Summary: This is a collection of 'rubber stamp' images for Tux Paint
Summary(ru_RU.KOI8-R): Колекция изображений 'штампов' для программы Tux Paint
License: GPL
Group: Graphics

Url: http://www.newbreedsoftware.com/tuxpaint/
Source: %name-%version.tar.gz

BuildRequires: gettext-tools
Requires: tuxpaint >= 0.9.15

BuildArch: noarch

%description
This is a collection of 'rubber stamp' images for Tux Paint.
Tux Paint - A simple drawing program for children.

%description -l ru_RU.KOI8-R
Коллекция изображений 'штампов' для программы "Tux Paint"
"Tux Paint" является детской программой для рисования.

%prep
%setup -q

%build
# Compile locales by hand.
pushd po
    for f in *.po; do
        t=${f#%name-}
        msgfmt -v -o "${t%.po}.mo" "$f"
    done
popd

%install
%__make DATA_PREFIX=%buildroot/%_datadir/tuxpaint/ install-all

# Install locales by hand.
pushd po
    for f in *.mo; do
        install -pD -m644 "$f" "$RPM_BUILD_ROOT%_datadir/locale/${f%.mo}/LC_MESSAGES/%name.mo"
    done
popd
%find_lang --with-gnome %name

%files -f %name.lang
# docs files
%doc docs/*

# data files
%_datadir/tuxpaint/stamps/*

%changelog
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
