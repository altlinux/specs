Name: wp-cli
Version: 0.20.4
Release: alt1

Summary: WP-CLI is a set of command-line tools for managing WordPress installations.

License: MIT
Group: System/Configuration/Packaging
Url: https://github.com/wp-cli/wp-cli

Source: %name-%version.tar

Packager: Danil Mikhailov <danil@altlinux.org>


# Automatically added by buildreq on Thu May 28 2015
# optimized out: fontconfig libgnome-keyring libgpg-error php5-libs php5-pdo php5-suhosin python-base python-module-distribute python-module-oslo.i18n python-module-oslo.utils python-modules python-modules-compiler python-modules-encodings python3-base
#BuildRequires: git-core libcrypto7 libdb4-devel libsubversion-auth-gnome-keyring mercurial php5 php5-curl php5-dom php5-imagick2 php5-mbstring php5-mysql php5-openssl php5-pdo_sqlite php5-zip python-module-cmd2 python-module-google python-module-mwlib python-module-oslo.config python-module-oslo.serialization python3 ruby ruby-stdlibs subversion time unzip
BuildRequires: php5-openssl
BuildArch: noarch

%define wpcli %_datadir/wp-cli

%description
WP-CLI is a set of command-line tools for managing WordPress installations.

%prep
%setup

%build

#!!! Create new vendor cache for new wp-cli version by get_vendor_cache.sh !!!

#TODO pack in phar archive

%install
#Move vendor cache with build requires
mv .gear/vendor/ vendor/

mkdir -p %buildroot/%wpcli/
cp -a ./ %buildroot/%wpcli/
rm -rf %buildroot/%wpcli/.gear/ %buildroot/usr/share/wp-cli/.gitattributes %buildroot/usr/share/wp-cli/.mailmap %buildroot/usr/share/wp-cli/.travis.yml

mkdir -p %buildroot/%_bindir/
cat >%buildroot/%_bindir/%name <<EOF
#!/bin/sh
%wpcli/bin/wp "\$@"
EOF

#ln -s /%_bindir/%name /%_bindir/wp

%pre

%files
%attr(755,root,root) %_bindir/%name
#%attr(755,root,root) %_bindir/wp
%wpcli/*

%changelog
* Wed Dec 09 2015 Vitaly Lipatov <lav@altlinux.ru> 0.20.4-alt1
- update wp-cli to 0.20.4

* Fri May 29 2015 Danil Mikhailov <danil@altlinux.org> 0.19.1-alt1
- initial build for ALT Linux Sisyphus

