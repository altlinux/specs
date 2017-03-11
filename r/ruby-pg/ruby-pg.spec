# vim: set ft=spec: -*- rpm-spec -*-

Name: ruby-pg
Version: 0.19.0
Release: alt2

Summary: Ruby interface to PostgreSQL RDBMS
Group: Development/Ruby
License: MIT/Ruby or GPL
Url: http://bitbucket.org/ged/ruby-pg/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sun Aug 31 2008 (-bi)
BuildRequires: libruby-devel postgresql-devel ruby-tool-setup
BuildRequires: uni2ascii

%description
This is the extension library to access a PostgreSQL database
from Ruby. This library works with PostgreSQL 6.4-8.x; it
probably works with 6.3 or earlier with slight modification,
but not tested at all.

%package doc
Summary: Documentation files for %name
Group: Documentation
Conflicts: ruby-postgres-doc
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup
%patch -p1
#sed -i -r 's/([[:blank:]]rb_enc)(_alias\()/\1db\2/g' ext/pg.c
#mv ext/pg.c ext/pg.c.utf8 && uni2ascii -B ext/pg.c.utf8 > ext/pg.c
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc ext/pg.c

%files
%doc Contributors.rdoc README.rdoc LICENSE
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc
%doc sample
%ruby_ri_sitedir/PG*

%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Tue Sep 13 2016 Denis Medvedev <nbr@altlinux.org> 0.19.0-alt1
- new version

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.9.0-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Sun Dec 08 2012 Led <led@altlinux.ru> 0.9.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed build doc
- fixed build with libruby 1.9.x

* Fri Jun 11 2010 Alexey I. Froloff <raorn@altlinux.org> 0.9.0-alt1
- [0.9.0] (closes: #23616)

* Mon Aug 17 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.0-alt2
- Applied m17n patch by Yuki Sonoda and Nikolai Lugovoi

* Wed May 13 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.0-alt1
- [0.8.0]

* Sun Aug 31 2008 Sir Raorn <raorn@altlinux.ru> 0.7.9.2008.08.17-alt1
- Built for Sisyphus
