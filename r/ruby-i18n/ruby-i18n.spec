# vim: set ft=spec: -*- rpm-spec -*-

%def_disable check

%define pkgname i18n

Name: ruby-%pkgname
Version: 0.3.7
Release: alt2.1

Summary: I18n and localization solution for Ruby
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/i18n/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup tzdata
%{!?_disable_check:BuildRequires: ruby-activerecord ruby-activerecord-sqlite3-adapter ruby-activesupport ruby-mocha}

%description
I18n and localization solution for Ruby.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1

%build
%update_setup_rb
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%check
%ruby_vendor test/all.rb

%files
%doc README.textile
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/I18n*

%changelog
* Wed Dec 05 2012 Led <led@altlinux.ru> 0.3.7-alt2.1
- Rebuilt with ruby-1.9.3-alt1
- disabled check

* Sat May 29 2010 Alexey I. Froloff <raorn@altlinux.org> 0.3.7-alt2
- Mask ActiveRecord dependency

* Sun Apr 25 2010 Alexey I. Froloff <raorn@altlinux.org> 0.3.7-alt1
- [0.3.7]

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 0.3.6-alt1
- [0.3.6]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1.3-alt1
- [0.1.3]

* Tue Feb 03 2009 Sir Raorn <raorn@altlinux.ru> 0.1.2-alt1
- [0.1.2]

* Wed Nov 19 2008 Sir Raorn <raorn@altlinux.ru> 0.1.0-alt3
- Updated to [g3696c92] from git://github.com/svenfuchs/i18n

* Tue Nov 18 2008 Sir Raorn <raorn@altlinux.ru> 0.1.0-alt2
- Updated to [g0bafcb3] from git://github.com/mattetti/i18n.git

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 0.1.0-alt1
- Built for Sisyphus

