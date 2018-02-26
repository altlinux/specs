%define		php5_extension	htmltmplpro

%define vmajor 0.95
%define vminor 1

Name:	 	php5-%php5_extension
Version:	%vmajor.%vminor
Release:	alt2

Summary:	php5 module to produce HTML from HTML Template files.
Group:		System/Servers
License:	PHP License
Packager:	Igor Vlasenko <viy@altlinux.org>
Url:		http://sf.net/projects/html-tmpl-pro

Source0:	%name-%version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires:	php5-devel = %php5_version-%php5_release
BuildRequires:	libhtmltmplpro-devel >= %vmajor
# for make test
BuildRequires:  php5-suhosin

%description
The HTML::Template::Pro library is a portable template engine for templates
that use syntax of known perl modules HTML::Template, HTML::Template::Expr
and HTML::Template::Pro.

This package contains php5 interface module for the library.

%{summary}

%prep
%setup -q

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
./configure \
	--enable-%php5_extension
%php5_make 

%install
# hack ...
# ln -s %_libdir/php/%_php5_version/extensions/suhosin.so modules/

%php5_make_install
install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%doc QUICKSTART
%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Tue Feb 14 2012 Anton Farygin <rider@altlinux.ru> 0.95.1-alt2
- rebuild for php5-5.3.10.20120202-alt1

* Tue Dec 13 2011 Igor Vlasenko <viy@altlinux.ru> 0.95.1-alt1
- 0.93-0.95 api, support for fresh php

* Sun Nov 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.93.1-alt1
- 0.93 api support

* Thu Oct 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.92.5-alt1
- added documentation

* Fri Oct 16 2009 Igor Vlasenko <viy@altlinux.ru> 0.92.4-alt1
- release

* Tue Oct 13 2009 Igor Vlasenko <viy@altlinux.ru> 0.92.3-alt1
- rc2

* Sat Oct 03 2009 Igor Vlasenko <viy@altlinux.ru> 0.92.2-alt1
- rc1

* Tue Sep 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.92.1-alt1
- first Sisyphus version;
