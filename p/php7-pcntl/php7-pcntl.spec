%define		php7_extension	pcntl

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	Process Control Module for PHP (pcntl)
Group:		System/Servers
License:	PHP Licence

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires:	php7-devel = %php7_version

%description
The %name package includes a dynamic shared object (DSO) that adds 
all features related to process spawning and control (fork(), waitpid(), 
signal(), WIF's, etc), to PHP.

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
%doc CREDITS README

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%version-%release
