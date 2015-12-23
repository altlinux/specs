%define		php5_extension	apcu
%define 	real_name	APCu
%define		real_version	4.0.7

Name:	 	php5-%{php5_extension}
Version:	%php5_version
Release:	%php5_release

Summary:	PHP5 APCu - APC User Cache

License:	PHP License
Group:		System/Servers
URL:		http://pecl.php.net/package/APCu
#URL:		https://github.com/krakjoe/apcu

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh



BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version

%description
PHP extension APCu is an APC stripped of opcode caching in
preparation for the deployment of Zend Optimizer+ as the
primary solution to opcode caching in future versions of PHP.

APCu only supports userland caching (and dumping) of variables,
providing an upgrade path for the APC users. The tried and 
tested APC codebase provides far superior support for local
storage of PHP variables.

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
	--enable-apc \
	--enable-apc-mmap \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%doc README.md TECHNOTES.txt TODO NOTICE LICENSE

%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%version-%release

* Tue Aug 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 5.5.25.20150514-alt2
- Initial build for ALT Linux Sisyphus

