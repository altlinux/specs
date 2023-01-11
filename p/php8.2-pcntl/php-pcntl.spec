%define		php_extension	pcntl

Name:	 	php%_php_suffix-%php_extension
Version:	%php_version
Release:	%php_release

Summary:	Process Control Module for PHP (pcntl)
Group:		System/Servers
License:	PHP-3.01
Source1:	php-%php_extension.ini
Source2:	php-%php_extension-params.sh

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires:	php-devel = %php_version

BuildRequires: /proc php%_php_suffix

%description
The %name package includes a dynamic shared object (DSO) that adds 
all features related to process spawning and control (fork(), waitpid(), 
signal(), WIF's, etc), to PHP.

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

%check
# PHP-8.0: Insufficient privileges for CLONE_NEWUSER
rm -f tests/pcntl_unshare_03.phpt ||:
make test

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
