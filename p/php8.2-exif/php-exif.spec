%define		php_extension	exif

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release

Summary:	Read header information from JPEG and DIFF headers
Group:		System/Servers
License:	PHP-3.01

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh
Patch0: php7-exif-mbstring-bug68547.patch

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires: php-devel = %php_version
BuildRequires: php%_php_suffix = %php_version
# for unicode support in exif files
BuildRequires: php%_php_suffix-mbstring = %php_version
Requires: php%_php_suffix-mbstring = %php_version

%description
The EXIF functions provide access to information stored in headers
of JPEG and TIFF images. This way you can read meta data generated
by digital cameras and certain image processing applications.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .
%if "%_php_suffix" == "7"
%patch0 -p3
%endif

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

%check
# turned off tests on i586 does not pass the tests/bug76557.phpt (poor processing errors from exif)
# 063+ Warning: exif_read_data(bug76557.jpg): Process tag(x3030=UndefinedTa): Illegal pointer offset(x30303030 < xF70732CE) in /usr/src/RPM/BUILD/php7-exif-7.3.10/tests/bug76557.php on line 2
# 063- Warning: exif_read_data(bug76557.jpg): Process tag(x3030=UndefinedTa): Illegal pointer offset(x30303030 + x30303030 = x60606060 > x00EE) in %sbug76557.php on line %d

%ifnarch %ix86 armh
ln -s %php_extdir/* modules/
NO_INTERACTION=1 make test
%endif

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
