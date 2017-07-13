# TODO pack in phar archive with https://github.com/clue/phar-composer

Name: wp-cli
Version: 1.2.1
Release: alt1

Summary: WP-CLI is a set of command-line tools for managing WordPress installations.

License: MIT
Group: System/Configuration/Packaging
Url: https://github.com/wp-cli/wp-cli

# Source-url: https://github.com/wp-cli/wp-cli/archive/v%version.tar.gz
Source: %name-%version.tar

#!!! Create new vendor cache for new wp-cli version by get_vendor_cache.sh !!!
Source1: %name-vendor-%version.tar

Packager: Danil Mikhailov <danil@altlinux.org>

BuildArch: noarch

#composer 
BuildRequires: php5-openssl pear-PHPUnit

%define wpcli %_datadir/wp-cli

%description
WP-CLI is a set of command-line tools for managing WordPress installations.

%prep
%setup -a1

%build

#!!! Create new vendor cache for new wp-cli version by get_vendor_cache.sh !!!


#composer install --no-interaction
# --prefer-source

%install
rm -rf %buildroot/%wpcli/vendor/

mkdir -p %buildroot/%wpcli/
cp -a ./ %buildroot/%wpcli/
rm -rf %buildroot/%wpcli/.gear/ %buildroot/%wpcli/{.editorconfig,.gitattributes,.mailmap,.travis.yml}
rm -rf %buildroot/%wpcli/{tests,utils}/

# TODO: do not working after it
echo "Generating PHAR ..."
php -dphar.readonly=0 utils/make-phar.php wp-cli.phar --quiet --version=%version --store-version
# FIXME: do not work after build

mkdir -p %buildroot/%_bindir/
cat >%buildroot/%_bindir/%name <<EOF
#!/bin/sh
%wpcli/bin/wp "\$@"
EOF
chmod 0755 %buildroot/%_bindir/%name
ln -s %name %buildroot/%_bindir/wp

%check
test "$(%buildroot%wpcli/bin/wp cli version)" = "WP-CLI %version"

%files
%_bindir/%name
%_bindir/wp
%wpcli/

%changelog
* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version (1.2.1) with rpmgs script
- update vendor dir

* Fri Aug 19 2016 Vitaly Lipatov <lav@altlinux.ru> 0.24.1-alt1
- new version (0.24.1) with rpmgs script
- switch to build from tarball

* Thu Dec 10 2015 Vitaly Lipatov <lav@altlinux.ru> 0.20.4-alt2
- added wp command - link to wp-cli
- update vendor dir
- add check for generated version

* Wed Dec 09 2015 Vitaly Lipatov <lav@altlinux.ru> 0.20.4-alt1
- update wp-cli to 0.20.4

* Fri May 29 2015 Danil Mikhailov <danil@altlinux.org> 0.19.1-alt1
- initial build for ALT Linux Sisyphus

