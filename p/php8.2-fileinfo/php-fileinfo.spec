%define php_extension	fileinfo

Name: php%_php_suffix-%php_extension
Version: %php_version
Release: %php_release
Group: System/Servers
License: PHP-3.01

Epoch: 1

BuildRequires(pre): rpm-build-php8.2-version
BuildPreReq: php-devel = %php_version

# Automatically added by buildreq on Wed Mar 03 2010
BuildRequires: libmagic-devel

Summary: Fileinfo PHP extension try to guess the content type and encoding of a file

Source1: php-%php_extension.ini
Source2: php-%php_extension-params.sh

%description
The functions in this module try to guess the content type and encoding
of a file by looking for certain magic byte sequences at specific
positions within the file. While this is not a bullet proof approach
the heuristics used do a very good job.

Additionally it can also be used to retrieve the mime type
for a particular file and for text files proper language encoding.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .

%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php_version
%configure \
	--with-%php_extension=%_usr
%php_make

%check
NO_INTERACTION=1 make test

%install
%php_make_install
install -D -m 644 %SOURCE1 %buildroot/%php_extconf/%php_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php_extconf/%php_extension/params

%post
%php_extension_postin

%preun
%php_extension_preun

%files
%php_extconf/%php_extension
%php_extdir/*
%doc CREDITS

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} 1:%version-%release
- Rebuild with php-devel = %version-%release
