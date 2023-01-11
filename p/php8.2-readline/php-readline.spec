%define		php_extension	readline

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release
Summary:	Readline functions
Group:		System/Servers
License:	PHP-3.01

Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version

BuildRequires: libreadline-devel libedit-devel
BuildRequires: php-devel = %php_version

%description
The readline functions implement an interface to the GNU Readline library.

%prep
%setup -T -c
cp -pr %php_extsrcdir/%php_extension/* .
sed -i '/php.h/i#include \"config\.h\"' readline_cli.c
%build
phpize

BUILD_HAVE=`echo %php_extension | tr '[:lower:]-' '[:upper:]_'`
export LDFLAGS="-lphp-%_php_version" ### Stupid PHP not understand LDLIBS
%add_optflags -fPIC -L%_libdir
%configure --with-%php_extension
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
- Rebuild with php-devel = %php_version-%php_release

