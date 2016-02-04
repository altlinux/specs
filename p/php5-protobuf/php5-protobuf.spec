%define		php5_extension	protobuf
%define 	real_name	protobuf
%define		real_version	0.10

Name:	 	php5-%{php5_extension}
Version:	%php5_version
Release:	%php5_release

Summary:	PHP5 Protobuf - Fast PHP Protocol Buffers implementation

License:	PHP License
Group:		System/Servers
URL:		https://github.com/allegro/php-protobuf

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version

%description
Protobuf PHP5 extension is a PHP implementation of Google's Protocol Buffers.
Parsing and serialization is provided by ProtobufMessage class which is
entirely implemented in extension providing high performance.

%prep
%setup -c
##%setup -T -c
##tar xvf %SOURCE0

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	--enable-protobuf \
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
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%version-%release

* Tue Feb 02 2016 Nikolay A. Fetisov <naf@altlinux.ru> 5.6.16.20151125-alt1
- Initial build for ALT Linux Sisyphus

