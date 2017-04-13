%define		php5_extension	enchant

Name:	 	php5-%php5_extension
Version:	%php5_version
Release:	%php5_release
Summary:	Enchant functions
Group:		System/Servers
License:	PHP Licence

Source1:	php5-%php5_extension.ini
Source2:	php5-%php5_extension-params.sh

Prereq:		php5-libs >= %php5_version-%php5_release

BuildRequires(pre): rpm-build-php5

BuildRequires: libenchant-devel libedit-devel
BuildRequires: php5-devel = %php5_version

%description
This extension uses the functions of the Enchant library

%prep
%setup -T -c
cp -pr %php5_extsrcdir/%php5_extension/* .
%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
export LDFLAGS="-lphp-%_php5_version" ### Stupid PHP not understand LDLIBS
%add_optflags -fPIC -L%_libdir
%configure --with-%php5_extension
%php5_make

%install
%php5_make_install
install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc CREDITS

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%version-%release

