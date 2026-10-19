%define pear_name Cache_Lite

Name: pear-Cache_Lite
Version: 2.0.0
Release: alt1

Summary: Fast and Safe little cache system

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/Cache_Lite

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/pear/Cache_Lite/archive/refs/tags/v%version.tar.gz
Source: Cache_Lite-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This package is a little cache system optimized for file containers. It is
fast and safe (because it uses file locking and/or anti-corruption tests).

%prep
%setup -c

%install
mkdir -p %buildroot%pear_dir
cp -a Cache %buildroot%pear_dir/

%check
for f in $(find Cache -name '*.php') ; do
    php -l $f
done
php -d include_path=.:%pear_dir -r 'require "Cache/Lite.php"; $d = sys_get_temp_dir()."/cl".getmypid()."/"; mkdir($d); $c = new Cache_Lite(array("cacheDir" => $d, "lifeTime" => 60)); $c->save("hello", "id1"); if ($c->get("id1") !== "hello") exit(1);'

%files
%doc LICENSE README.md TODO composer.json docs
%pear_dir/Cache/

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0
- switch to GitHub source (upstream dropped package.xml), install files directly

* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.3-alt1
- new version 1.8.3 (with rpmrb script)

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- new version 1.8.2 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Wed Jul 27 2016 Vitaly Lipatov <lav@altlinux.ru> 1.7.16-alt1
- new version 1.7.16 (with rpmrb script)

* Mon May 16 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.9-alt1
- new version 1.7.9 (with rpmrb script)

* Wed Dec 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.8-alt1
- new version 1.7.8 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- new version 1.7.4 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- initial build for ALT Linux Sisyphus

