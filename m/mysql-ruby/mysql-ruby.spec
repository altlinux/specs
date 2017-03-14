# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname mysql-ruby

Name: %pkgname
Version: 2.9.0
Release: alt2

Summary: MySQL Ruby Connector
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/mysql-ruby/

Source: %pkgname-%version.tar

BuildRequires: libruby-devel libMySQL-devel ruby-tool-setup

%description
This is MySQL Ruby Connector (libmysqlclient wrapper).

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build
# Needs running mysqld
#ruby test.rb 127.0.0.1 root '' test 3306
## + ruby test.rb 127.0.0.1 root '' test 3306
## Loaded suite test
## Started
## ...................................................................................................................
## Finished in 0.543375 seconds.
## 
## 115 tests, 397 assertions, 0 failures, 0 errors, 0 skips

%install
%ruby_install

%files
%doc README.txt extra/README* extra/*.css
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Tue Sep 13 2016 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- New version
- Use ALT-specific Ruby module build rules

* Wed Mar 19 2014 Led <led@altlinux.ru> 2.8.2-alt2.2
- Rebuilt with ruby-2.0.0-alt1

* Fri Nov 30 2012 Led <led@altlinux.ru> 2.8.2-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Dec 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.8.2-alt2
- Rebuild with libmysqlclient.so.16

* Fri Jun 11 2010 Alexey I. Froloff <raorn@altlinux.org> 2.8.2-alt1
- [2.8.2]

* Mon Aug 17 2009 Alexey I. Froloff <raorn@altlinux.org> 2.8.1-alt2
- Applied m17n patch by hectoregm and PerfectlyNormal

* Tue May 12 2009 Alexey I. Froloff <raorn@altlinux.org> 2.8.1-alt1
- [2.8.1]

* Thu Apr 03 2008 Mikhail Yakshin <greycat@altlinux.ru> 2.7.5-alt1
- 2.7.5

* Tue Feb 20 2007 Mikhail Yakshin <greycat@altlinux.ru> 2.7-alt2
- Rebuild to fix x86_64 issue

* Tue Feb 21 2006 Mikhail Yakshin <greycat@altlinux.org> 2.7-alt1
- 2.7

* Mon Mar  1 2004 Mikhail Yakshin <greycat@altlinux.org> 2.4.5-alt1
- 2.4.5

* Tue Aug 05 2003 Alexander Bokovoy <ab@altlinux.ru> 2.4.4a-alt1
- 2.4.4a
- Rebuild with Ruby 1.8

* Fri Nov 22 2002 Rider <rider@altlinux.ru> 2.4.3a-alt3
- new version

* Tue Nov 19 2002 Alexander Bokovoy <ab@altlinux.ru> 2.4.3-alt3
- Rebuild with new FHS-compliant Ruby package
- Specfile cleanups (add BuildRequires, etc)
- Extconf.rb patch is replaced with new one

* Tue Sep 17 2002 Rider <rider@altlinux.ru> 2.4.3-alt2
- added patch from Alexander Bokovoy (BUILD with ruby-1.6.x and ruby-1.7.x)

* Tue Sep 17 2002 Rider <rider@altlinux.ru> 2.4.3-alt1
- first build for ALT Linux

