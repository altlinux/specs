%define php_extension	calendar

Name: php%_php_suffix-%php_extension
Version: %php_version
Release: %php_release
Summary: Date conversion between different calendar formats
Group: System/Servers
License: PHP-3.01

Source1: php-%php_extension.ini
Source2: php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version

%description
The %name extension presents a series of functions to simplify
converting between different calendar formats. The intermediary or
standard it is based on is the Julian Day Count. The Julian Day Count
is a count of days starting from January 1st, 4713 B.C. To convert
between calendar systems, you must first convert to Julian Day Count,
then to the calendar system of your choice. Julian Day Count is very
different from the Julian Calendar!

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .

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
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%files
%php_extconf/%php_extension
%php_extdir/*
%doc CREDITS

%post
%php_extension_postin

%preun
%php_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %version-%release
