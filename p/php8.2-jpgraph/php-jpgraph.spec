%define php_extension jpgraph

%define confextensiondir %_sysconfdir/php/%php_extension
%define extensiondir %php_moddir/%php_extension
%define docdir %_docdir/%name-%version-%release
%if "%_php_suffix" == "8.1"
%def_with pack_extension
%endif

Name: php%_php_suffix-%php_extension
Version: 4.4.1
Release: alt%php_version.%php_release.1

Summary: 2D graph plotting library for PHP
License: %qpl1
Group: System/Servers
Url: http://jpgraph.net
BuildArch: noarch

%if_with pack_extension
Source: php-%php_extension-%version.tar
Source10: README.ALT
Patch: php-%php_extension-%version-alt-config.patch
%endif

Provides: %extensiondir

Requires: php%_php_suffix
Requires: php%_php_suffix-gd2
Requires: php-%php_extension = %version

BuildRequires: php-devel = %php_version

BuildRequires(pre): rpm-build-php8.2-version
BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-apache2
BuildPreReq: rpm-build-licenses >= 2.0.4

%description
The JpGraph library is a 2D graph plotting library for PHP. It is meant
to significantly simplify the creation of dynamic graphs using PHP
scripting. The libray can be used on its own or as an embedded part of
a large WEB development undertaking. In addition the library allows
images to be created using the command line version of PHP
(the cli version).

%if_with pack_extension
%package -n php-%php_extension-doc
Summary: JpGraph documentation
Group: Books/Other
AutoReq: no

%description -n php-%php_extension-doc
This package contains the JpGraph library documentation in HTML format.

%package -n php-%php_extension
Summary: %summary
Group: System/Servers

%description -n php-%php_extension
The JpGraph library is a 2D graph plotting library for PHP. It is meant
to significantly simplify the creation of dynamic graphs using PHP
scripting. The libray can be used on its own or as an embedded part of
a large WEB development undertaking. In addition the library allows
images to be created using the command line version of PHP
(the cli version).
%endif

%if_with pack_extension
%prep
%setup -n php-%php_extension-%version
%patch0 -p1

%install
mkdir -p %buildroot%php_moddir/
mkdir -p %buildroot%confextensiondir/
cp -a src %buildroot%extensiondir
mv %buildroot%extensiondir/jpg-config.inc.php \
	%buildroot%confextensiondir/
mv %buildroot%extensiondir/jpgraph_ttf.inc.php \
	%buildroot%confextensiondir/
ln -snf $(relative %buildroot%confextensiondir/jpg-config.inc.php \
	%buildroot%extensiondir/jpg-config.inc.php) \
	%buildroot%extensiondir/jpg-config.inc.php
ln -snf $(relative %buildroot%confextensiondir/jpgraph_ttf.inc.php \
	%buildroot%extensiondir/jpgraph_ttf.inc.php) \
	%buildroot%extensiondir/jpgraph_ttf.inc.php

mkdir -p %buildroot%docdir
install -m 644 src/README VERSION  %buildroot%docdir/
install -m 644 %SOURCE10 %buildroot%docdir/
cp -a docs %buildroot%docdir/html/
%endif

%if_with pack_extension
%files -n php-%php_extension
%doc %docdir/
%exclude %docdir/html/
%extensiondir/
%exclude %extensiondir/Examples
%config(noreplace) %confextensiondir/

%files -n php-%php_extension-doc
%doc %docdir/html/
%endif

%files

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php-devel = %php_version-%php_release

* Thu Dec 08 2022 Anton Farygin <rider@altlinux.ru> 4.4.1-alt%php_version.%php_release
- separated the package to extension and package of dependencies for each supported version of PHP

* Wed Nov 09 2022 Anton Farygin <rider@altlinux.ru> 4.4.1-alt1
- 4.4.1
- built for php7, php8.0 and php8.1
- removed examples, examples-apache2, doc-apache2 subpackages

* Fri Jul 09 2021 Anton Farygin <rider@altlinux.ru> 4.3.4-alt2
- switch to universal, version-independed macros from rpm-build-php 8.0

* Fri May 21 2021 Anton Farygin <rider@altlinux.ru> 4.3.4-alt1
- 4.3.4
- removed all rpm post scripts (they moved to filetriggers from apache package)

* Mon Jul 27 2020 Anton Farygin <rider@altlinux.ru> 4.3.0-alt2
- removed requirement for nonfree ms-ttf fonts (closes: #29430)

* Mon Apr 20 2020 Paul Wolneykien <manowar@altlinux.org> 4.3.0-alt1
- No more base-doc package.
- Update spec for the new PHP7 version. No more Apache v1.
- Set PHP7 in README.ALT.
- Fresh up to v4.3.0.

* Tue Apr 26 2011 Aleksey Avdeev <solo@altlinux.ru> 3.0.7-alt3
- Add provides %%_sysconfdir/php/jpgraph dir to %%name package

* Tue Apr 12 2011 Aleksey Avdeev <solo@altlinux.ru> 3.0.7-alt2
- Fix configuration files to apache{,2} in examples-apache{,2}
  subpackage

* Tue Apr 12 2011 Aleksey Avdeev <solo@altlinux.ru> 3.0.7-alt1
- Initial build for ALT Linux Sisyphus
