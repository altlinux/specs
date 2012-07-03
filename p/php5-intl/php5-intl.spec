%define		php5_extension	intl

Name:	 	php5-%php5_extension
Version:	%php5_version
Release:	%php5_release

Summary:	Internationalization extension is a wrapper for ICU library
Group:		System/Servers
License:	PHP Licence

Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires:	php5-devel = %php5_version

BuildRequires: libicu-devel gcc-c++
Provides: pecl-intl
Obsoletes: pecl-intl

%description
Internationalization extension (further is referred as Intl) is a wrapper
for ICU library, enabling PHP programmers to perform UCA-conformant
collation and date/time/number/currency formatting in their scripts.

It tends to closely follow ICU APIs, so that people having experience
working with ICU in either C/C++ or Java could easily use the PHP
API. Also, this way ICU documentation would be useful to understand
various ICU functions.

Intl consists of several modules, each of them exposes the corresponding ICU API:

Collator: provides string comparison capability with support for
appropriate locale-sensitive sort orderings.

Number Formatter: allows to display number according to the localized
format or given pattern or set of rules, and to parse strings into
numbers.

Message Formatter: allows to create messages incorporating data (such as
numbers or dates) formatted according to given pattern and locale rules,
and parse messages extracting data from them.

Normalizer: provides a function to transform text into one of the Unicode
normalization forms, and provides a routine to test if a given string
is already normalized.

Locale: provides interaction with locale identifiers in the form
of functions to get subtags from locale identifier; parse, compose,
match(lookup and filter) locale identifiers.

%prep
%setup -T -c
cp -pr %php5_extsrcdir/%php5_extension/* .

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-php-config=%_bindir/php-config \
	--with-%php5_extension
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
* Sat Feb 11 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
- now intl extension included to php
