%define		php5_extension	interbase

Name:	 	php5-%php5_extension
Version:	%php5_version
Release:	%php5_release

Summary:	Interbase database module for PHP5
Group:		System/Servers
License:	PHP Licence

Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh


BuildRequires(pre): rpm-build-php5
BuildRequires:	php5-devel = %php5_version

BuildRequires: firebird-devel chrpath

%description
The %name package includes a dynamic shared object (DSO) that adds Interbase (Firebird)
database support to PHP.  

%prep
%setup -T -c
cp -pr %php5_extsrcdir/%php5_extension/* .

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

chrpath -d %buildroot/%php5_extdir/%php5_extension.so

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc CREDITS

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Sat Feb 11 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- Rebuild with php5-5.3.5.20110105-alt2

* Thu Feb 10 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
- first build for Sisyphus
