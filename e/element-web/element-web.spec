Name: element-web
Version: 1.12.13
Release: alt1

Summary: A glossy Matrix collaboration client

License: AGPL-3.0-only
Group: Networking/Instant messaging
Url: https://element.io/

BuildArch: noarch

# Source-url: https://github.com/element-hq/element-web/archive/v%version.tar.gz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from
# etersoft-build-utils. ask me about description using: lav@etersoft.ru
Source1: %name-development-%version.tar

AutoReq:yes,nonodejs,nonodejs_native,nomono
AutoReq:nopython,nomingw32,nomingw64,noshebang

# node_modules vendored on x86_64 (native rollup bindings are arch-specific)
ExclusiveArch: x86_64

Requires: /var/www/html

BuildRequires: /proc
BuildRequires: /usr/bin/node

%description
Element (formerly known as Vector and Riot) is a Matrix web client built using
the Matrix React SDK.

%prep
%setup -a1
# Remove packageManager to prevent nx from trying to use specific pnpm version
subst '/"packageManager"/d' package.json
# Ensure all dependencies are hoisted to root node_modules
echo "shamefully-hoist=true" >> .npmrc
cp apps/web/config.sample.json apps/web/config.json

%build
export PATH=$(pwd)/node_modules/.bin:$PATH
export NODE_PATH=$(pwd)/node_modules
# Run prebuild steps manually (nx calls pnpm which is not available)
cd apps/web
sh res/css/rethemendex.sh
node module_system/scripts/install.ts
cd -
# Build shared-components
cd packages/shared-components
vite build
cd -
# Build element-web
cd apps/web
webpack-cli --disable-interpret --progress --mode production

%install
mkdir -p %buildroot/var/www/html/
cp -a apps/web/webapp %buildroot/var/www/html/%name/

# Move config to /etc and create symlink
mkdir -p %buildroot%_sysconfdir/%name/
mv %buildroot/var/www/html/%name/config.json %buildroot%_sysconfdir/%name/config.json
ln -s %_sysconfdir/%name/config.json %buildroot/var/www/html/%name/config.json

%files
%doc README.md
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/config.json
/var/www/html/%name/

%changelog
* Thu Apr 03 2026 Vitaly Lipatov <lav@altlinux.ru> 1.12.13-alt1
- new version (1.12.13) via gear-uupdate
- switch from yarn to pnpm (upstream moved to pnpm monorepo)
- update License to AGPL-3.0-only
- update Source-url to element-hq organization
- add Requires: /var/www/html
- move config.json to /etc/element-web/ with symlink

* Wed Mar 29 2023 Sergey V Markov <markow@altlinux.org> 1.11.25-alt1
- new version 1.11.25 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.7-alt1
- new version 1.9.7 (with rpmrb script)

* Mon Oct 11 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version 1.9.1 (with rpmrb script)

* Mon Sep 27 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Fri Sep 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- new version 1.8.5 (with rpmrb script)

* Mon Sep 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt1
- new version 1.8.4 (with rpmrb script)
- CVE-2021-40823, CVE-2021-40824

* Wed Sep 01 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- new version 1.8.2 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.32-alt1
- new version 1.7.32 (with rpmrb script)

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.30-alt1
- new version 1.7.30 (with rpmrb script)

* Tue Mar 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.23-alt1
- new version 1.7.23 (with rpmrb script)

* Wed Mar 03 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.22-alt1
- new version 1.7.22 (with rpmrb script)

* Tue Feb 23 2021 Vitaly Lipatov <lav@altlinux.ru> 1.7.21-alt1
- new version 1.7.21 (with rpmrb script)

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.12-alt1
- new version 1.7.12 (with rpmrb script)

* Mon Oct 12 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.9-alt1
- new version 1.7.9 (with rpmrb script)

* Mon Sep 14 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- new version 1.7.7 (with rpmrb script)

* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- new version 1.7.5 (with rpmrb script)

* Sun Aug 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- new version 1.7.4 (with rpmrb script)

* Wed Aug 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2 (with rpmrb script)

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
- initial release for ALT Sisyphus
