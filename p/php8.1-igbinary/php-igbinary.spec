%define _unpackaged_files_terminate_build 1
%define		php_extension	igbinary

Name:           php%_php_suffix-%php_extension
Version:        3.2.15
Release:        alt2.%php_version
Summary:        Replacement for the standard PHP serializer
Group:		System/Servers
License:        BSD-3-Clause
Url:            https://pecl.php.net/package/igbinary
Source:         php-%php_extension-%version.tar

Source1: igbinary.ini
Source2: php-igbinary-params.sh

BuildRequires(pre): rpm-build-php8.1-version
BuildRequires: php-devel = %php_version
BuildRequires: gcc php-pear
BuildRequires: php%_php_suffix-json php%_php_suffix-apcu
 
%description
Igbinary is a drop in replacement for the standard PHP serializer.
Instead of time and space consuming textual representation,
igbinary stores PHP data structures in a compact binary form.
Savings are significant when using memcached or similar memory
based storages for serialized data.


%package devel
Summary:       Igbinary developer files (header)
Group:         Development/Other
Requires:      php-devel = %php_version

%description devel
These are the files needed to compile programs using Igbinary

%prep
%setup -n php-%php_extension-%version

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	--enable-%php_extension
%php_make
    
%install
%php_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%check
make test

%post
%php_extension_postin

%preun
%php_extension_preun

%files
%php_extconf/%php_extension
%php_extdir/*

%files devel
%_includedir/php

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%php_release

* Tue Dec 19 2023 Alexandr Antonov <aas@altlinux.org> 3.2.15-alt2.%php_version
- renamed the ini file (ALT #48855)

* Tue Dec 05 2023 Alexandr Antonov <aas@altlinux.org> 3.2.15-alt1.%php_version
- Init for ALT.

