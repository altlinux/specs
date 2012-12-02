%define		php5_extension	redis
%define 	real_name	redis
%define		real_version	2.2.2

Name:	 	php5-%php5_extension
Version:	%real_version
Release:	alt1

Summary:	Client extension for Redis key-value store.

License:	PHP License
Group:		System/Servers
URL:		https://github.com/nicolasff/phpredis

Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version

%description
The phpredis extension provides an API for communicating with the Redis key-value store.

%prep
%setup -q -n %php5_extension-%version

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension \
	--with-libdir=%_lib

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%doc CREDITS *.markdown

%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Sun Dec 02 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 2.2.2-alt1
- Initial build

