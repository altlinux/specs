# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8
%define pkgname i18n

Name: ruby%{ruby_major}-%pkgname
Version: 0.3.7
Release: alt4

Summary: I18n and localization solution for Ruby
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/i18n/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Mon Nov 10 2008 (-bi)
BuildRequires: ruby%{ruby_major} rpm-build-ruby ruby%{ruby_major}-activerecord ruby%{ruby_major}-activerecord-sqlite3-adapter ruby%{ruby_major}-activesupport ruby%{ruby_major}-mocha ruby%{ruby_major}-tool-rdoc ruby-tool-setup tzdata

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
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_vendor test/all.rb

%install
%ruby_install
%rdoc lib/

%files
%doc README.textile
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/I18n*

%changelog
* Wed May 04 2011 Timur Aitov <timonbl4@altlinux.org> 0.3.7-alt4
- Rebuild with tests

* Tue Apr 12 2011 Timur Aitov <timonbl4@altlinux.org> 0.3.7-alt3
- Rebuild for ruby1.8

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

