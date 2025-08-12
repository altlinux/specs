%define php_extension mongodb

Name: mongo-php-driver
Version: 2.1.1
Release: alt1

Summary: MongoDB driver for PHP

License: Apache-2.0
Group: Development/Other
Url: https://pecl.php.net/package/mongodb
VCS: https://github.com/mongodb/mongo-php-driver.git

# Source-url: https://github.com/mongodb/mongo-php-driver/archive/%version/mongo-php-driver-%version.tar.gz
Source: php-%php_extension-%version.tar.gz
Patch: php-%php_extension-%version-alt.patch

BuildRequires(pre): rpm-build-php8.4-version
BuildRequires: libbson-devel libmongoc-devel libmongocrypt-devel
BuildRequires: php-devel = %php_version

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

%package -n php%_php_suffix-%php_extension
Summary: MongoDB driver for PHP
Group: Development/Other

%description -n php%_php_suffix-%php_extension
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

%prep
%setup -n php-%php_extension-%version
%patch -p1

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

# config file
mkdir -p %buildroot%php_extconf/%php_extension
echo "extension=%php_extension.so" > %buildroot%php_extconf/%php_extension/config
cat <<EOF > %buildroot%php_extconf/%php_extension/params
file_ini=%php_extension.ini
exceptions=
EOF

%post
%php_extension_postin

%preun
%php_extension_preun

%files -n php%_php_suffix-%php_extension
%doc LICENSE README.md
%php_extconf/%php_extension
%php_extdir/mongodb.so

%changelog
* Tue Aug 12 2025 Leontiy Volodin <lvol@altlinux.org> 2.1.1-alt1
- Initial build for ALT Sisyphus.
