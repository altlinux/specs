Name: composer
Version: 1.0.0
Release: alt4

Summary: Composer helps you declare, manage and install dependencies of PHP projects, ensuring you have the right stack everywhere.

License: MIT
Group: System/Configuration/Packaging
Url: https://github.com/composer/composer

Source: %name-%version.tar

Packager: Danil Mikhailov <danil@altlinux.org>

Requires: php5-openssl php5

#BuildPreReq: php5 php5-openssl php5-suhosin
# Automatically added by buildreq on Thu May 28 2015
# optimized out: fontconfig libgnome-keyring libgpg-error php5-libs php5-pdo php5-suhosin python-base python-module-distribute python-module-oslo.i18n python-module-oslo.utils python-modules python-modules-compiler python-modules-encodings python3-base
#BuildRequires: git-core libcrypto7 libdb4-devel libsubversion-auth-gnome-keyring mercurial php5 php5-curl php5-dom php5-imagick2 php5-mbstring php5-mysql php5-openssl php5-pdo_sqlite php5-zip python-module-cmd2 python-module-google python-module-mwlib python-module-oslo.config python-module-oslo.serialization python3 ruby ruby-stdlibs subversion time unzip
BuildRequires: git-core php5-openssl php5
BuildArch: noarch

%description
Composer helps you declare, manage and install dependencies of PHP projects, ensuring you have the right stack everywhere.

%prep
%setup

%build

#!!! Create new vendor cache for new composer version by get_vendor_cache.sh !!!

#Move vendor cache with build requires
mv .gear/vendor/ vendor/

#Compile need git log -n1 --pretty=ct HEAD #TODO remove it
git init
git config user.email "you@example.com"
git config user.name "Your Name"
git add bin/compile
git commit -am "Fix for compile"

#build composer.phar
php -d phar.readonly=off -d date.timezone='Europe/Moscow' bin/compile

%install
mkdir -p %buildroot/%_datadir/
cp composer.phar %buildroot/%_datadir/

mkdir -p %buildroot/%_bindir/
cat >%buildroot/%_bindir/%name <<EOF
#!/bin/sh
php -d suhosin.executor.include.whitelist=phar %_datadir/composer.phar "\$@"
EOF

%pre

%files
%attr(755,root,root) %_bindir/%name
%attr(755,root,root) %_datadir/%name.phar

%changelog
* Wed Nov 25 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt4
- Added php5 req

* Fri May 29 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt3
- Remove install section, added vendor cache

* Fri May 29 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt2
- Change libdir to datadir, add commets

* Thu May 28 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
