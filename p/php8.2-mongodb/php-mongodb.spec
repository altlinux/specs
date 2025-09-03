%define php_extension mongodb

Name: php%_php_suffix-%php_extension
Version: 2.1.1
Release: alt%php_version.%php_release

Summary: MongoDB driver for PHP

License: Apache-2.0
Group: System/Servers
Url: https://pecl.php.net/package/mongodb
VCS: https://github.com/mongodb/mongo-php-driver

Source0: php-%php_extension-%version.tar
Source1: php-%php_extension.ini
Source2: php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version
BuildRequires: libbson-devel libmongoc-devel libmongocrypt-devel

%description
This extension is developed atop the
[libmongoc](https://github.com/mongodb/mongo-c-driver) and
[libbson](https://github.com/mongodb/libbson) libraries. It provides a minimal
API for core driver functionality: commands, queries, writes, connection
management, and BSON serialization.

Userland PHP libraries that depend on this extension may provide higher level
APIs, such as query builders, individual command helper methods, and GridFS.
Application developers should consider using this extension in conjunction with
the [MongoDB PHP library](https://github.com/mongodb/mongo-php-library), which
implements the same higher level APIs found in MongoDB drivers for other
languages.

%prep
%setup -n php-%php_extension-%version

%build
BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS="-lphp-%_php_version" ### Stupid PHP not understand LDLIBS
phpize
%configure \
  --with-php-config=%_bindir/php-config \
  --with-mongodb-system-libs \
  --with-mongodb-client-side-encryption \
  --enable-%php_extension \
#
%php_make

%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
# network tests
rm -f tests/logging/logging-addSubscriber-004.phpt
rm -f tests/manager/manager-{ctor-server,getencryptedfieldsmap-001}.phpt
rm -f tests/bson/bson-int64-operation-002.phpt
NO_INTERACTION=1 make test

%files
%doc LICENSE README.md
%php_extconf/%php_extension
%php_extdir/mongodb.so

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- rebuilt with php-devel = %php_version-%php_release

* Tue Sep 02 2025 Leontiy Volodin <lvol@altlinux.org> 2.1.1-alt2
- Finally packaged as a universal php package.
- Renamed: mongo-php-driver -> php-mongodb.

* Mon Sep 01 2025 Leontiy Volodin <lvol@altlinux.org> 2.1.1-alt1.1
- Packaged as a more universal php package.

* Tue Aug 12 2025 Leontiy Volodin <lvol@altlinux.org> 2.1.1-alt1
- Initial build for ALT Sisyphus.
