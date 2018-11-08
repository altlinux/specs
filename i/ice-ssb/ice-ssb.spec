%define oname ice

Name: ice-ssb
Version: 5.3.4
Release: alt6

Summary: Application to easily add and remove Chromium site specific browsers.
License: GPL
Group: Networking/WWW
Url: https://github.com/peppermintos/ice
BuildArch: noarch

Source: %name-%version.tar
Patch0: fix-paths.patch
Patch1: fix-browsers-names.patch
Patch2: fix-del-ice-links.patch
Patch3: fix-desktop-file.patch

Requires: python3-module-pygobject3
Requires: python3-module-BeautifulSoup4
Requires: python3-module-requests
Requires: chromium

%description
Application to easily add and remove Chromium site specific browsers in Debian 
and Ubuntu based Linux distributions. It was originally created for Peppermint 
OS Ice and is now used as the default SSB application in Peppermint OS since 
the two branches of the OS merged for Peppermint Two. Since version 5, Ice has 
supported Google Chrome. Since version 5.1, Ice has supported Mozilla Firefox.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p0

%install
install -d -m 0755 %buildroot%_bindir
install -m 0755 %name/%oname %buildroot%_bindir/%name
install -m 0755 %name/%oname-firefox %buildroot%_bindir/%oname-firefox

install -d -m 0755 %buildroot/usr/lib/peppermint
install -d -m 0755 %buildroot/usr/lib/peppermint/%oname
install -m 0755 %name/%oname.glade %buildroot/usr/lib/peppermint/%oname/%oname.glade
install -m 0755 %name/search.json.mozlz4 %buildroot/usr/lib/peppermint/%oname/search.json.mozlz4

install -d -m 0755 %buildroot%_desktopdir
install -m 0755 %name/%oname.desktop %buildroot%_desktopdir/%name.desktop

install -d -m 0755 %buildroot%_pixmapsdir
install -m 0755 %name/%oname.png %buildroot%_pixmapsdir/%name.png

install -d -m 0755 %buildroot%_datadir/%name
cp -fR %name/locale %buildroot%_datadir/%name

%files
%_bindir/%name
%_bindir/%oname-firefox
%dir /usr/lib/peppermint
%dir /usr/lib/peppermint/%oname
/usr/lib/peppermint/%oname/%oname.glade
/usr/lib/peppermint/%oname/search.json.mozlz4
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_datadir/%name/locale


%changelog
* Thu Nov 08 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.4-alt6
- Complete localization into Russian (by Olesya Gerasimenko).

* Thu Oct 18 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.4-alt5
- Fixed del ice links

* Mon Oct 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.4-alt4
- fix firefox name

* Sun Sep 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.4-alt3
- Fixed requires

* Wed Sep 12 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.4-alt2
- Fixed chromium name

* Tue Sep 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.4-alt1
- Init build to Sisyphus

