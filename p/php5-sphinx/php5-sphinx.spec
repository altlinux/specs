%define		php5_extension	sphinx
%define 	real_name	sphinx
%define		real_version	1.2.0

Name:	 	php5-%php5_extension
Version:	%real_version
Release:	alt1

Summary:	Client extension for Sphinx - opensource SQL full-text search engine

License:	PHP License
Group:		System/Servers
URL:		http://pecl.php.net/package/sphinx

Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version
BuildRequires: libsphinxclient-devel
Requires: libsphinxclient

%description
This extension provides bindings for libsphinxclient, client library for Sphinx.
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
%doc CREDITS

%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Tue Jun 19 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 1.0.4-alt8
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 1.0.4-alt7
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 1.0.4-alt6
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 1.0.4-alt5
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 1.0.4-alt4
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Sep 16 2010 Anton Farygin <rider@altlinux.ru> 1.0.4-alt3
- Rebuild with php5-5.3.3.20100722-alt1

* Wed Aug 25 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 1.0.4-alt2
- Fix URL
- Required libsphinxclient

* Wed Aug 25 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 1.0.4-alt1
- Init build for ALT Libyx Sisyphus

