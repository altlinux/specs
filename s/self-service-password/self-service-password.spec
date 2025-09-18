%global ssp_destdir %_datadir/%name
%global ssp_cachedir %_cachedir/%name
%undefine __brp_mangle_shebangs

Name: self-service-password
Version: 1.7.3
Release: alt2

Summary: LDAP password change web interface

License: GPL-2.0-or-later
Group: Development/Other
Url: https://ltb-project.org/documentation/self-service-password.html
VCS: https://github.com/ltb-project/self-service-password

Source: https://ltb-project.org/archives/ltb-project-%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-php

%description
Self Service Password is a simple PHP application that allows users to change
their password on an LDAP directory.

Self Service Password is provided by LDAP Tool Box project:
http://ltb-project.org

Recommends: php-gd, php-ldap, php-mbstring, php-smarty, php-sodium.

%prep
%setup -n ltb-project-%name-%version
%patch -p1
# Clean hidden files in bundled php libs
find . \
  \( -name .gitignore -o -name .travis.yml -o -name .pullapprove.yml \) \
  -delete

%build

%install
# Create directories
mkdir -p %buildroot/%ssp_cachedir/cache
mkdir -p %buildroot/%ssp_cachedir/templates_c
mkdir -p %buildroot/%ssp_destdir
mkdir -p %buildroot/%ssp_destdir/conf
mkdir -p %buildroot/%ssp_destdir/htdocs
mkdir -p %buildroot/%ssp_destdir/lang
mkdir -p %buildroot/%ssp_destdir/lib
mkdir -p %buildroot/%ssp_destdir/scripts
mkdir -p %buildroot/%ssp_destdir/templates
# mkdir -p %buildroot/%ssp_destdir/vendor

# Copy files
## PHP
install -p -m 644 htdocs/*.php   %buildroot/%ssp_destdir/htdocs
cp -a             htdocs/css     %buildroot/%ssp_destdir/htdocs
cp -a             htdocs/images  %buildroot/%ssp_destdir/htdocs
cp -a             htdocs/js      %buildroot/%ssp_destdir/htdocs
# cp -a             htdocs/vendor  %buildroot/%ssp_destdir/htdocs
install -p -m 644 lang/*         %buildroot/%ssp_destdir/lang
install -p -m 644 lib/*.php      %buildroot/%ssp_destdir/lib
cp -a             lib/smsovh     %buildroot/%ssp_destdir/lib
cp -a             lib/captcha    %buildroot/%ssp_destdir/lib
install -p -m 644 scripts/*      %buildroot/%ssp_destdir/scripts
install -p -m 644 templates/*    %buildroot/%ssp_destdir/templates
# cp -a             vendor/*       %buildroot/%ssp_destdir/vendor

## Apache configuration
mkdir -p %buildroot/%_sysconfdir/httpd/conf.d
install -p -m 644 packaging/rpm/SOURCES/self-service-password-apache.conf \
%buildroot/%_sysconfdir/httpd/conf.d/self-service-password.conf

# Adapt Smarty paths
sed \
  -e 's:/usr/share/php/smarty3:%php_moddir/smarty/lib:' \
  -e 's:^#$smarty_cache_dir.*:$smarty_cache_dir = "'%ssp_cachedir/cache'";:' \
  -e 's:^#$smarty_compile_dir.*:$smarty_compile_dir = "'%ssp_cachedir/templates_c'";:' \
  -i conf/config.inc.php

# Move conf file to %%_sysconfdir
mkdir -p %buildroot/%_sysconfdir/%name
install -p -m 644 conf/config.inc.php \
%buildroot/%_sysconfdir/%name/

# Load configuration files from /etc/self-service-password/
for file in $( grep -r -l -E "\([^(]+\/conf\/[^)]+\)" %buildroot/%ssp_destdir ) ; do
  sed -i -e \
    's#([^(]\+/conf/\([^")]\+\)")#("%_sysconfdir/%name/\1")#' \
    ${file}
done

# Make script executable
chmod +x %buildroot/%_datadir/%name/scripts/update_samba_password.sh

%pre
# Backup old configuration to /etc/self-service-password
for file in $( find %ssp_destdir/conf -name "*.php" -type f ! -name 'config.inc.php' -printf "%f\n" 2>/dev/null );
do
    # move conf file to /etc/self-service-password/*.save
    mkdir -p %_sysconfdir/%name
    mv %ssp_destdir/conf/${file} %_sysconfdir/%name/${file}.save
done
# Move specific file config.inc.php to /etc/self-service-password/config.inc.php.bak
if [[ -f "%ssp_destdir/conf/config.inc.php"  ]]; then
    mkdir -p %_sysconfdir/%name
    mv %ssp_destdir/conf/config.inc.php \
%_sysconfdir/%name/config.inc.php.bak
fi

%post
# Move old configuration to /etc/self-service-password
for file in $( find %_sysconfdir/%name -name "*.save" -type f );
do
    # move previously created *.save file into its equivalent without .save
    mv ${file} ${file%.save}
done
# Clean cache
rm -rf %ssp_cachedir/{cache,templates_c}/*


%files
%doc LICENCE README.md packaging/debian/changelog
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/config.inc.php
%config(noreplace) %_sysconfdir/httpd/conf.d/self-service-password.conf
%ssp_destdir
%dir %ssp_cachedir
%attr(-,apache,apache) %ssp_cachedir/cache
%attr(-,apache,apache) %ssp_cachedir/templates_c

%changelog
* Thu Sep 18 2025 Leontiy Volodin <lvol@altlinux.org> 1.7.3-alt2
- Fixed build with php-smarty 5.5.2-alt1.

* Mon Aug 18 2025 Leontiy Volodin <lvol@altlinux.org> 1.7.3-alt1
- Initial build for ALT Sisyphus.
