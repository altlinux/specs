%define		php7_extension	sockets

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	Sockets support for PHP
Group:		System/Servers
License:	PHP Licence

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires:	php7-devel = %php7_version

%description
The %name extension implements a low-level interface to the socket 
communication functions based on the popular BSD sockets, providing 
the possibility to act as a socket server as well as a client.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--enable-%php7_extension
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
