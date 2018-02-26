# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname mysql-ruby

Name: %pkgname
Version: 2.8.2
Release: alt2

Summary: MySQL Ruby Connector
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/mysql-ruby/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Tue May 12 2009 (-bi)
BuildRequires: libruby-devel libMySQL-devel

%description
This is MySQL Ruby Connector (libmysqlclient wrapper).

%prep
%setup -n %pkgname-%version
%patch -p1

%build
%ruby_configure
%make_build
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
%makeinstall_std

%files
%doc README.html
%ruby_sitearchdir/*

%changelog
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

