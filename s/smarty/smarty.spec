%define _smartydir %php5_datadir/smarty

Name: smarty
Version: 2.6.22
Release: alt1

Summary: Template engine for PHP
License: LGPL
Group: Development/Other

# git svn init -Ttrunk -ttags -bbranches http://smarty-php.googlecode.com/svn/
Url: http://www.smarty.net
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: rpm-build-php5

%description
Smarty is a template engine for PHP. Smarty provides your basic
variable substitution and dynamic block functionality, and also takes
a step further to be a "smart" template engine, adding features such
as configuration files, template functions, variable modifiers, and
making all of this functionality as easy as possible to use for both
programmers and template designers.

%prep
%setup

%install
install -d %buildroot{%_smartydir/{internals,plugins},%php5_peardir}

install libs/{Config_File,Smarty{,_Compiler}}.class.php %buildroot%_smartydir
install libs/debug.tpl %buildroot%_smartydir
install libs/internals/*.php %buildroot%_smartydir/internals
install libs/plugins/*.php %buildroot%_smartydir/plugins

install -d %buildroot%php5_peardir/%name

%post
[ -e %php5_peardir/%name ] || ln -s %_smartydir %php5_peardir/%name

%files
%doc BUGS ChangeLog FAQ INSTALL NEWS README RELEASE_NOTES TODO
%dir %_smartydir
%dir %_smartydir/internals
%dir %_smartydir/plugins
%_smartydir/*.class.php
%_smartydir/debug.tpl
%_smartydir/internals/*.php
%_smartydir/plugins/*.php

# for the sake of bc
%ghost %php5_peardir/%name

%changelog
* Tue Jan 27 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.6.22-alt1
- Updated to 2.6.22. Security fixes:
  + CVE-2008-4810
  + CVE-2008-4811

* Wed Mar 12 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.6.19-alt1
- 2.6.19. Security fixes:
  + CVE-2008-1066 (Smarty "regex_replace" Modifier Template Security Bypass)

* Thu May 24 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 2.6.18-alt1
- Initial build for Sisyphus
