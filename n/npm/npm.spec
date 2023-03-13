Name: npm
Version: 8.19.3
Release: alt1

Summary: A package manager for node

Group: Development/Tools
License: MIT
Url: http://nodejs.org/

# Source-url: https://github.com/npm/cli/archive/v%version.tar.gz
Source: %name-%version.tar

Patch1: npm-disable-update-notifier.patch
Patch2: npm-disable-internal-node-gyp.patch
Patch3: npm-fix-user-agent-output.patch

BuildRequires(pre): rpm-macros-nodejs

#BuildRequires: node >= 6.9
#Requires:	node >= 6.9

# Note! Change version with new npm
#Requires: npm(node-gyp) = 5.0.7

BuildArch:	noarch

# we do not need any module provides here
AutoProv: yes,nonodejs
AutoReq: yes,nonodejs

%description
npm is a package manager for node. You can use it to install and publish your
node programs. It manages dependencies and does other cool stuff.

npm is configured to use npm, Inc.'s public package registry
at https://registry.npmjs.org by default.

It is not recommended to build binary libraries within npm module,
but you can install node-gyp package to support that.

In most cases it is enough to install appropriate node- package (like node-sass).

%prep
%setup
%patch1 -p2
%patch2 -p2
%patch3 -p2

# remove all node-gyp deps
rm -rv bin/node-gyp-bin node_modules/node-gyp/

%build
#make man

%install
mkdir -p %buildroot%nodejs_sitelib/%name/ %buildroot%_bindir/
ln -s %nodejs_sitelib/%name/bin/npm-cli.js %buildroot%_bindir/npm
ln -s %nodejs_sitelib/%name/bin/npx-cli.js %buildroot%_bindir/npx

# need inet
#node cli.js install -g --prefix %buildroot%_prefix
# just copy, like in node package was
cp -a . %buildroot%nodejs_sitelib/%name/

# remove all tests from workspaces (ALT bug 42037)
rm -rv %buildroot%nodejs_sitelib/%name/workspaces/*/test/

# remove unused scripts
rm -rv %buildroot%nodejs_sitelib/%name/{scripts,tap-snapshots,test,configure}

# remove all node-gyp deps
rm -rv %buildroot%nodejs_sitelib/%name/node_modules/@npmcli/run-script/lib/node-gyp-bin

# stop symlinks
find %buildroot%nodejs_sitelib/%name/ -type l | while read link ; do
    real=$(realpath $link)
    rm -v $link
    mv -v $real $link
done

%files -n npm
%_bindir/npm
%_bindir/npx
%nodejs_sitelib/%name/

%changelog
* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 8.19.3-alt1
- new version 8.19.3 (with rpmrb script)

* Fri Oct 21 2022 Vitaly Lipatov <lav@altlinux.ru> 8.19.2-alt2
- fix npm config get user-agent output (ALT bug 43430)

* Sun Oct 16 2022 Vitaly Lipatov <lav@altlinux.ru> 8.19.2-alt1
- new version 8.19.2 (with rpmrb script)

* Fri Sep 30 2022 Vitaly Lipatov <lav@altlinux.ru> 8.15.0-alt1
- new version 8.15.0 (with rpmrb script)

* Wed Aug 03 2022 Vitaly Lipatov <lav@altlinux.ru> 8.11.0-alt2
- drop node-gyp deps (ALT bug 42036)
- remove unused scripts makes extra deps

* Tue Jul 12 2022 Vitaly Lipatov <lav@altlinux.ru> 8.11.0-alt1
- new version 8.11.0 (with rpmrb script)

* Wed Apr 27 2022 Vitaly Lipatov <lav@altlinux.ru> 8.5.5-alt1
- new version 8.5.5 (with rpmrb script)

* Sat Apr 23 2022 Vitaly Lipatov <lav@altlinux.ru> 8.5.0-alt1
- new version 8.5.0 (with rpmrb script)

* Thu Mar 31 2022 Vitaly Lipatov <lav@altlinux.ru> 8.3.1-alt3
- disable update notifier

* Thu Mar 17 2022 Vitaly Lipatov <lav@altlinux.ru> 8.3.1-alt2
- drop tests from new workspaces libs (ALT bug 42037)
- don't pack symlinks (ALT bug 42000)

* Sun Feb 13 2022 Vitaly Lipatov <lav@altlinux.ru> 8.3.1-alt1
- new version 8.3.1 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 8.1.2-alt1
- new version 8.1.2 for node 16 LTS (with rpmrb script)

* Wed Sep 01 2021 Vitaly Lipatov <lav@altlinux.ru> 6.14.15-alt1
- new version 6.14.15 (with rpmrb script)
- CVE-2021-32803, CVE-2021-32804, CVE-2021-37701, CVE-2021-37712, CVE-2021-37713, CVE-2021-39134, CVE-2021-39135

* Fri Jul 30 2021 Vitaly Lipatov <lav@altlinux.ru> 6.14.14-alt1
- new version 6.14.14 (with rpmrb script)

* Thu Jul 22 2021 Vitaly Lipatov <lav@altlinux.ru> 6.14.13-alt1
- new version 6.14.13 (with rpmrb script)

* Sun Apr 11 2021 Vitaly Lipatov <lav@altlinux.ru> 6.14.12-alt1
- new version 6.14.12 (with rpmrb script)
- CVE-2020-7774, CVE-2020-7788. CVE-2020-8244

* Fri Feb 05 2021 Vitaly Lipatov <lav@altlinux.ru> 6.14.10-alt1
- new version 6.14.10 (with rpmrb script)
- GHSL-2020-145

* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.8-alt1
- new version 6.14.8 (with rpmrb script)

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.7-alt1
- new version 6.14.7 (with rpmrb script)

* Sat Jun 27 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.5-alt3
- fix npm ERR without module 'node-gyp/bin/node-gyp'

* Tue Jun 23 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.5-alt2
- drop node-gyp requires (to avoid toolchain requires)

* Fri May 22 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.5-alt1
- new version 6.14.5 (with rpmrb script)

* Sun Mar 29 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.4-alt1
- new version 6.14.4 (with rpmrb script)

* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 6.13.7-alt1
- new version 6.13.7 (with rpmrb script)

* Wed Feb 19 2020 Vitaly Lipatov <lav@altlinux.ru> 6.13.6-alt2
- pack /usr/bin/npx

* Tue Feb 18 2020 Vitaly Lipatov <lav@altlinux.ru> 6.13.6-alt1
- new version 6.13.6 (with rpmrb script)

* Wed Dec 25 2019 Vitaly Lipatov <lav@altlinux.ru> 6.13.4-alt1
- new version 6.13.4 (with rpmrb script)

* Sat Oct 26 2019 Vitaly Lipatov <lav@altlinux.ru> 6.11.3-alt1
- new version 6.11.3 (with rpmrb script)

* Fri Jun 07 2019 Vitaly Lipatov <lav@altlinux.ru> 6.9.0-alt1
- new version 6.9.0 (with rpmrb script)

* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 6.4.1-alt1
- new version 6.4.1 (with rpmrb script)

* Tue May 22 2018 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt1
- new version 5.6.0 (with rpmrb script)

* Sat Mar 18 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.10-alt2
- build with external node-gyp

* Thu Feb 02 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.10-alt1
- new version 3.10.10 (with rpmrb script)

* Wed Dec 21 2016 Vitaly Lipatov <lav@altlinux.ru> 3.10.9-alt3
- drop gnuplot and convert requires

* Sun Dec 18 2016 Vitaly Lipatov <lav@altlinux.ru> 3.10.9-alt2
- new version 3.10.9 (with rpmrb script)

* Sat Oct 08 2016 Vitaly Lipatov <lav@altlinux.ru> 3.10.3-alt1
- initial build for ALT Linux Sisyphus

