# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8
%define pkgname mongrel

Name: ruby%{ruby_major}-%pkgname
Version: 1.1.5
Release: alt7

Summary: Simple Fast Mostly Ruby Web Server
Group: Development/Ruby
License: MIT
Url: http://rubyforge.org/projects/mongrel/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

#require_relative -> require
Patch1: ruby-mongrel-1.1.5-alt-require_relative.patch

# Automatically added by buildreq on Wed Aug 27 2008 (-bi)
BuildRequires: /proc libruby%{ruby_major}-devel ruby%{ruby_major}-daemons ruby%{ruby_major}-gem_plugin ruby%{ruby_major}-stdlibs ruby-tool-setup ragel

%description
Mongrel is a small library that provides a very fast HTTP 1.1
server for Ruby web applications.  It is not particular to any
framework, and is intended to be just enough to get a web
application running behind a more complete and robust web
server.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q -n %pkgname-%version
%patch -p1
%patch1 -p2
%update_setup_rb

%build
%ruby_config
## 58 tests, 445 assertions, 3 failures, 0 errors, 0 pendings, 0 omissions, 0 notifications
#pushd ext/http11
#ragel -G2 -o http11_parser.c http11_parser.rl
#popd
%ruby_build
%ruby_test_unit -Ilib:ext/http11 test

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGELOG README TODO
%_bindir/*
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%doc examples
%ruby_ri_sitedir/Mongrel*

%changelog
* Thu Apr 28 2011 Timur Aitov <timonbl4@altlinux.org> 1.1.5-alt7
- Rebuild for ruby1.8

* Mon Nov 29 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt6
- Fix build with Ruby 1.9.2

* Sat Jun 05 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt5
- Fix cookies processing (once more)

* Sun May 02 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt4
- Fix cookies processing

* Fri Nov 20 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt3
- Fixed :prefix setting for new Rails API

* Fri May 15 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.5-alt2
- Rebuilt with Ruby 1.9

* Wed Aug 27 2008 Sir Raorn <raorn@altlinux.ru> 1.1.5-alt1
- Built for Sisyphus

