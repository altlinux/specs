Name: trustme
Version: 0.7
Release: alt6

Summary: Encrypted notepad
License: %gpl2only
BuildArch: noarch

Group: Editors

Source: %{name}_%version.tar.gz
Patch1: trustme-commit-on-lock.patch
Patch2: trustme-multiple-db.patch


#optimized out: fontconfig glibc-pthread libX11-locales libgpg-error libgtk+2-common python-base python-module-pycairo python-module-pygobject python-modules
BuildRequires: libgcrypt python-module-pygtk python-modules-encodings python-module-gcrypt

BuildPreReq: rpm-build-licenses
BuildRequires: desktop-file-utils

%description
Encrypted notepad, also used on Maemo

%prep
%setup -q -n %{name}_%version
%patch1 -p2
%patch2 -p2

sed -i '1 c#!/usr/bin/env python' ./trustme.py ./mktest.py ./Crypto/Cipher/tests.py ./TrustMe/DataStore.py
sed -i '/compileall/ d' makefile

# fix python shebangs
find . -type f -print0 |
    xargs -r0 grep -lZ '^#![[:space:]]*%_bindir/.*python$' -- |
    xargs -r0 sed -E -i '1 s@^(#![[:space:]]*)%_bindir/(env[[:space:]]+)?python$@\1%__python@' --

%build
make build

%install
make DESTDIR=%buildroot install
install %name.desktop %buildroot%_desktopdir/
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Utility \
	--add-category=TextEditor \
	%buildroot%_desktopdir/trustme.desktop

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.png

%changelog
* Wed Dec 18 2019 Grigory Ustinov <grenka@altlinux.org> 0.7-alt6
- Fixed python shebang.

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.7-alt5.qa2
- NMU: reverted repocop patch

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.7-alt5.qa1
- NMU: applied repocop patch

* Fri Sep 21 2018 Grigory Ustinov <grenka@altlinux.org> 0.7-alt5
- Changed categories of desktop file (Closes: #25688).

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt4.qa1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.7-alt4.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for trustme

* Sun Jan 9 2011 Mykola Grechukh <gns@altlinux.ru> 0.7-alt4
- support for multiple db (choosed at first argv)
- in editor commit before lock

* Sun May 30 2010 Mykola Grechukh <gns@altlinux.ru> 0.7-alt3
- word-wrap in editor

* Thu May 27 2010 Mykola Grechukh <gns@altlinux.ru> 0.7-alt2
- buildreq fixed

* Thu May 27 2010 Mykola Grechukh <gns@altlinux.ru> 0.7-alt1
- first build to Sisyphus 
