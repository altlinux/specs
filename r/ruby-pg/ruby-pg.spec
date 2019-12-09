%define        pkgname pg

Name:          ruby-%pkgname
Version:       1.1.4
Release:       alt2
Summary:       Ruby interface to PostgreSQL RDBMS
Group:         Development/Ruby
License:       BSD-2-Clause
Url:           https://bitbucket.org/ged/ruby-pg/
Vcs:           https://bitbucket.org/ged/ruby-pg.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: postgresql-devel
BuildRequires: uni2ascii

%description
This is the extension library to access a PostgreSQL database
from Ruby. This library works with PostgreSQL 6.4-8.x; it
probably works with 6.3 or earlier with slight modification,
but not tested at all.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Summary(ru_RU.UTF-8): Файлы для разработки на основе самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

Requires:      postgresql-devel

%description   -n gem-%pkgname-devel
Development files for %gemname gem.

%description   -n gem-%pkgname-devel -l ru_RU.UTF8
Файлы для разработки на основе самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=pg --version-replace=1.1.4

%install
%ruby_install

%check
%ruby_test

%files
%doc README* LICENSE
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*


%changelog
* Mon Dec 09 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt2
- added (+) postgresql-devel to gem-%pkgname-devel
- added (+) some translations
- fixed (*) some syntax issues, licence (TODO)

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt1
- Bump to 1.1.4
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2.5
- Rebuild with new Ruby autorequirements.
- Disable debuginfo.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt2.1
- Rebuild with Ruby 2.4.1

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
