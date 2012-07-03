%define		php5_extension	readline

Name:	 	php5-%php5_extension
Version:	%php5_version
Release:	%php5_release
Summary:	ZIP functions
Group:		System/Servers
License:	PHP Licence

Source1:	php5-%php5_extension.ini
Source2:	php5-%php5_extension-params.sh

Prereq:		php5-libs >= %php5_version-%php5_release

BuildRequires(pre): rpm-build-php5

BuildRequires: libreadline-devel libedit-devel
BuildRequires: php5-devel = %php5_version

%description
The readline functions implement an interface to the GNU Readline library.

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
* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
- Rebuild with php5-5.3.5.20110105-alt1

* Mon Nov 15 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3
- initial build for Sisyphus, thanks to Konstantin Pavlov

