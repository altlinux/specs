Name: element-desktop
Version: 1.9.7
Release: alt1

Summary: A glossy Matrix collaboration client

License: Apache 2.0
Url: https://element.io/
Group: Networking/Instant messaging

BuildArch: noarch

# Source-url: https://github.com/vector-im/element-desktop/archive/v%version.tar.gz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from etersoft-build-utils
# ask me about description using: lav@etersoft.ru
Source1: %name-development-%version.tar

Source3: %name.desktop

AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
#AutoProv: no

ExclusiveArch: x86_64 aarch64

BuildRequires: npm node-asar
# https://github.com/yarnpkg/yarn/issues/7251
BuildRequires: /proc yarn

BuildRequires: element-web = %version

Requires: electron13 >= 13.1.9

Provides: riot-desktop = %version-%release
Obsoletes: riot-desktop

BuildRequires: node-typescript

%description
Element Desktop is a Matrix client for desktop platforms with Element Web at its core.

%prep
%setup -a1
cp -a /var/www/html/element-web webapp

%build
# note: configure it
cat element.io/release/config.json | grep -v "update_base_url" > webapp/config.json
# TODO: support hak and build matrix-seshat
#yarn run hak
yarn run build:ts
yarn run build:res
#npm run build
#yarn build
#yarn dist
#npm ERR! cb() never called!
#npm ERR! This is an error with npm itself. Please report this error at:
rm -vf node_modules/.bin/{npm,npx}
npm prune --production

asar pack . resources/app.asar

cat <<EOF >%name
#!/bin/sh
electron13 %_datadir/%name/resources/app.asar "\$@"
EOF

%install
install -m755 -D %name %buildroot%_bindir/%name
ln -s %name %buildroot/%_bindir/riot-desktop

mkdir -p %buildroot%_datadir/%name/
cp -a resources %buildroot%_datadir/%name/

for i in 16 22 24 32 48 64 128 256 512 ; do
    F=build/icons/${i}x${i}.png
    [ -s "$F" ] || continue
    T=%buildroot%_iconsdir/hicolor/${i}x${i}/apps/
    mkdir -p $T/
    cp $F $T/%name.png
done

install -D -m644 %SOURCE3 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/riot-desktop
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.7-alt1
- new version 1.9.7 (with rpmrb script)

* Mon Oct 11 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version 1.9.1 (with rpmrb script)

* Mon Sep 27 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Fri Sep 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- new version 1.8.5 (with rpmrb script)

* Mon Sep 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt1
- new version (1.8.4) with rpmgs script
- switch to electron13
- CVE-2021-40823, CVE-2021-40824

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.30-alt1
- new version 1.7.30 (with rpmrb script)

* Tue Mar 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.23-alt1
- new version 1.7.23 (with rpmrb script)

* Wed Mar 03 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.22-alt1
- new version 1.7.22 (with rpmrb script)

* Wed Feb 24 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.21-alt1
- new version 1.7.21 (with rpmrb script)

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.12-alt1
- new version 1.7.12 (with rpmrb script)

* Mon Oct 12 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.9-alt1
- new version 1.7.9 (with rpmrb script)

* Tue Sep 15 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- new version 1.7.7 (with rpmrb script)

* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- new version 1.7.5 (with rpmrb script)

* Sun Aug 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- new version 1.7.4 (with rpmrb script)

* Wed Aug 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2 (with rpmrb script) (ALT bug 38786)

* Sat Jul 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.8-alt1
- new version 1.6.8 (with rpmrb script)

* Tue Jun 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.7-alt1
- new version 1.6.7 (with rpmrb script)

* Tue Jun 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.6-alt1
- new version 1.6.6 (with rpmrb script)

* Sat Jun 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.4-alt1
- new version 1.6.4 (with rpmrb script)

* Thu Jun 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.3-alt1
- new version 1.6.3 (with rpmrb script)

* Fri May 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- new version (1.6.2) with rpmgs script

* Fri Apr 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.15-alt1
- new version 1.5.15 (with rpmrb script)

* Wed Oct 16 2019 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version 1.4.2 (with rpmrb script)

* Wed Sep 04 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- new version 1.3.3 (with rpmrb script)

* Thu Jun 13 2019 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Sun Mar 10 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- build new version from sources

* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- initial release for ALT Sisyphus
