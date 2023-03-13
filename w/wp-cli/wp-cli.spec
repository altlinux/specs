Name: wp-cli
Version: 2.7.1
Release: alt1

Summary: WP-CLI is a set of command-line tools for managing WordPress installations.

License: MIT
Group: System/Configuration/Packaging
Url: https://github.com/wp-cli/wp-cli

# Source-url: https://github.com/wp-cli/wp-cli-bundle/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-vendor-%version.tar

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

#composer 
BuildRequires: php7 php7-openssl php7-readline

%define wpcli %_datadir/wp-cli

%description
WP-CLI is a set of command-line tools for managing WordPress installations.

%prep
%setup -a1

%build
echo "Generating PHAR ..."
php -dphar.readonly=0 utils/make-phar.php wp-cli.phar --quiet --version=%version --store-version

%install

mkdir -p %buildroot/%_bindir/
install wp-cli.phar %buildroot%_bindir/%name
ln -s %name %buildroot/%_bindir/wp

%check
test "$(%buildroot%_bindir/wp cli version)" = "WP-CLI %version"

%files
%_bindir/%name
%_bindir/wp

%changelog
* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 2.7.1-alt1
- new version 2.7.1 (with rpmrb script)

* Mon Oct 28 2019 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)

* Fri Jun 07 2019 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Fri Mar 08 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version (2.1.0) with rpmgs script

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

