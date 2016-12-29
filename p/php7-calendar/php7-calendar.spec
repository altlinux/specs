%define		php7_extension	calendar

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release

Summary:	Date conversion between different calendar formats
Group:		System/Servers
License:	PHP Licence

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

BuildRequires(pre): rpm-build-php7
BuildRequires:	php7-devel = %php7_version

%description
The %name extension presents a series of functions to simplify
converting between different calendar formats. The intermediary or
standard it is based on is the Julian Day Count. The Julian Day Count
is a count of days starting from January 1st, 4713 B.C. To convert
between calendar systems, you must first convert to Julian Day Count,
then to the calendar system of your choice. Julian Day Count is very
different from the Julian Calendar! 

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

