# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8

Name: ruby%{ruby_major}-pg
Version: 0.9.0
Release: alt2

Summary: Ruby interface to PostgreSQL RDBMS
Group: Development/Ruby
License: MIT/Ruby or GPL
Url: http://bitbucket.org/ged/ruby-pg/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sun Aug 31 2008 (-bi)
BuildRequires: libruby%{ruby_major}-devel postgresql-devel ruby-tool-setup

%description
This is the extension library to access a PostgreSQL database
from Ruby. This library works with PostgreSQL 6.4-8.x; it
probably works with 6.3 or earlier with slight modification,
but not tested at all.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc ext/pg.c

%files
%doc Contributors README LICENSE
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc
%doc sample
%ruby_ri_sitedir/PG*

%changelog
* Wed Apr 27 2011 Timur Aitov <timonbl4@altlinux.org> 0.9.0-alt2
- Rebuild for ruby1.8

* Fri Jun 11 2010 Alexey I. Froloff <raorn@altlinux.org> 0.9.0-alt1
- [0.9.0] (closes: #23616)

* Mon Aug 17 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.0-alt2
- Applied m17n patch by Yuki Sonoda and Nikolai Lugovoi

* Wed May 13 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.0-alt1
- [0.8.0]

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 0.7.9.2008.08.17-alt1
- Built for Sisyphus

