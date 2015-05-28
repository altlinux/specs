Name: composer
Version: 1.0.0
Release: alt1

Summary: Composer helps you declare, manage and install dependencies of PHP projects, ensuring you have the right stack everywhere.

License: LGPL
Group: Office
Url: https://github.com/meganz/sdk

Source: %name-%version.tar
Source1: composer.phar

Packager: Danil Mikhailov <danil@altlinux.org>


#BuildPreReq: php5 php5-openssl php5-suhosin
# Automatically added by buildreq on Thu May 28 2015
# optimized out: fontconfig libgnome-keyring libgpg-error php5-libs php5-pdo php5-suhosin python-base python-module-distribute python-module-oslo.i18n python-module-oslo.utils python-modules python-modules-compiler python-modules-encodings python3-base
BuildRequires: git-core libcrypto7 libdb4-devel libsubversion-auth-gnome-keyring mercurial php5 php5-curl php5-dom php5-imagick2 php5-mbstring php5-mysql php5-openssl php5-pdo_sqlite php5-zip python-module-cmd2 python-module-google python-module-mwlib python-module-oslo.config python-module-oslo.serialization python3 ruby ruby-stdlibs subversion time unzip

%description
Composer helps you declare, manage and install dependencies of PHP projects, ensuring you have the right stack everywhere.

%prep
%setup

%build

#TODO change to req composer
mkdir -p %buildroot/tmp/
cp %SOURCE1 %buildroot/tmp/
cp -a .composer/ %buildroot/tmp/

HOME=%buildroot/tmp/
php -d phar.readonly=off -d suhosin.executor.include.whitelist=phar %buildroot/tmp/composer.phar install

#build composer.phar
git init
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git add bin/compile
git commit -am "Fix for compile"

php -d phar.readonly=off -d date.timezone='Europe/Moscow' bin/compile

%install
mkdir -p %buildroot/%_libdir/
cp composer.phar %buildroot/%_libdir/
ls %buildroot/%_libdir/

mkdir -p %buildroot/%_bindir/
cat >%buildroot/%_bindir/%name <<EOF
#!/bin/sh
php -d suhosin.executor.include.whitelist=phar %_libdir/composer.phar "\$@"
EOF

%pre

%files
%attr(755,root,root) %_bindir/%name
%attr(755,root,root) %_libdir/%name.phar

%changelog
* Thu May 28 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt1
- initial build for ALT Linux Sisyphus