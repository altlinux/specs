# vim: set ft=spec: -*- rpm-spec -*-

%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gpgme

Name:          gem-gpgme
Version:       2.0.24
Release:       alt1
Summary:       Ruby interface to GnuPG Made Easy
License:       LGPL-2.1+
Group:         Development/Ruby
Url:           https://github.com/ueno/ruby-gpgme
Vcs:           https://github.com/ueno/ruby-gpgme.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(mocha) >= 0.9.12
BuildRequires: gem(minitest) >= 2.1.0
BuildRequires: gem(yard) >= 0.9.11
BuildRequires: gem(coveralls_reborn) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(mini_portile2) >= 2.7
BuildConflicts: gem(mocha) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(mini_portile2) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      gem(mini_portile2) >= 2.7
Conflicts:     gem(mini_portile2) >= 3
Obsoletes:     ruby-gpgme < %EVR
Provides:      ruby-gpgme = %EVR
Provides:      gem(gpgme) = 2.0.24


%description
Ruby interface to GnuPG Made Easy (GPGME).


%if_enabled    doc
%package       -n gem-gpgme-doc
Version:       2.0.24
Release:       alt1
Summary:       Ruby interface to GnuPG Made Easy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gpgme
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gpgme) = 2.0.24
Obsoletes:     ruby-gpgme-doc
Provides:      ruby-gpgme-doc

%description   -n gem-gpgme-doc
Ruby interface to GnuPG Made Easy documentation files.

Ruby interface to GnuPG Made Easy (GPGME).

%description   -n gem-gpgme-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gpgme.
%endif


%if_enabled    devel
%package       -n gem-gpgme-devel
Version:       2.0.24
Release:       alt1
Summary:       Ruby interface to GnuPG Made Easy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gpgme
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gpgme) = 2.0.24
Requires:      gem(mocha) >= 0.9.12
Requires:      gem(minitest) >= 2.1.0
Requires:      gem(yard) >= 0.9.11
Requires:      gem(coveralls_reborn) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(rake) >= 0
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(yard) >= 1

%description   -n gem-gpgme-devel
Ruby interface to GnuPG Made Easy development package.

Ruby interface to GnuPG Made Easy (GPGME).

%description   -n gem-gpgme-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gpgme.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-gpgme-doc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gpgme-devel
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.24-alt1
- ^ 2.0.20 -> 2.0.24

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.20-alt1
- ^ 2.0.18 -> 2.0.20
- ! spec tags and syntax

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.18-alt1
- > Ruby Policy 2.0
- ^ 2.0.16 -> 2.0.18

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.16-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.16-alt1.1
- Rebuild with Ruby 2.5.0

* Thu Jan 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.16-alt1
- New version.

* Wed Dec 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.15-alt1
- New version.

* Mon Oct 30 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.14-alt1
- New version

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.13-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.13-alt1.1
- Rebuild with Ruby 2.4.1

* Wed Jul 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.13-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.12-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 2.0.12-alt1
- new version 2.0.12

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.0.6-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.0.6-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.6-alt1
- [1.0.6]
- License changed to LGPLv2.1+

* Sat Dec 27 2008 Sir Raorn <raorn@altlinux.ru> 1.0.1-alt1
- [1.0.1]

* Tue Aug 31 2004 Sir Raorn <raorn@altlinux.ru> 0.2-alt1
- Built for Sisyphus
