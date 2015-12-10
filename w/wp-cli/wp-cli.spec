Name: wp-cli
Version: 0.20.4
Release: alt2

Summary: WP-CLI is a set of command-line tools for managing WordPress installations.

License: MIT
Group: System/Configuration/Packaging
Url: https://github.com/wp-cli/wp-cli

Source: %name-%version.tar

Packager: Danil Mikhailov <danil@altlinux.org>

BuildArch: noarch

BuildRequires: php5-openssl composer

%define wpcli %_datadir/wp-cli

%description
WP-CLI is a set of command-line tools for managing WordPress installations.

%prep
%setup

%build

#!!! Create new vendor cache for new wp-cli version by get_vendor_cache.sh !!!

# TODO pack in phar archive with https://github.com/clue/phar-composer

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

ln -s %name %buildroot/%_bindir/wp

%check
test "$(%buildroot%wpcli/bin/wp cli version)" = "WP-CLI %version"

%files
%attr(755,root,root) %_bindir/%name
%attr(755,root,root) %_bindir/wp
%wpcli/*

%changelog
* Thu Dec 10 2015 Vitaly Lipatov <lav@altlinux.ru> 0.20.4-alt2
- added wp command - link to wp-cli
- update vendor dir
- add check for generated version

* Wed Dec 09 2015 Vitaly Lipatov <lav@altlinux.ru> 0.20.4-alt1
- update wp-cli to 0.20.4

* Fri May 29 2015 Danil Mikhailov <danil@altlinux.org> 0.19.1-alt1
- initial build for ALT Linux Sisyphus

