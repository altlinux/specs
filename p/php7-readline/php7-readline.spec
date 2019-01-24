%define		php7_extension	readline

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release
Summary:	Readline functions
Group:		System/Servers
License:	PHP Licence

Source1:	php7-%php7_extension.ini
Source2:	php7-%php7_extension-params.sh

Prereq:		php7-libs >= %php7_version-%php7_release

BuildRequires(pre): rpm-build-php7

BuildRequires: libreadline-devel libedit-devel
BuildRequires: php7-devel = %php7_version

%description
The readline functions implement an interface to the GNU Readline library.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .
sed -i '/php.h/i#include \"config\.h\"' readline_cli.c
%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
export LDFLAGS="-lphp-%_php7_version" ### Stupid PHP not understand LDLIBS
%add_optflags -fPIC -L%_libdir
%configure --with-%php7_extension
%php7_make

%install
%php7_make_install
install -D -m 644 %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%php7_extconf/%php7_extension
%php7_extdir/*
%doc CREDITS

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release

