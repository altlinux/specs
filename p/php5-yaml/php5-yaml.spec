%define		php5_extension	yaml
%define 	real_name	yaml
%define		real_version	1.1.0

Name:	 	php5-%{php5_extension}
Version:	%php5_version
Release:	%php5_release

Summary:	PHP5 YAML-1.1 parser and emitter

License:	%mit
Group:		System/Servers
URL:		http://pecl.php.net/package/yaml

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-licenses rpm-build-php5
BuildRequires: php5-devel = %php5_version  libyaml-devel

%description
YAML PHP5 extension provides support for YAML 1.1 (YAML Ain't Markup Language)
serialization using the LibYAML library.

%prep
%setup -c

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	--enable-yaml \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Fri Jan 04 2013 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.18.20121017-alt1
- Initial build for ALT Linux Sisyphus

