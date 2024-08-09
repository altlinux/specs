%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname mime-types

Name:          gem-mime-types
Version:       3.5.2
Release:       alt1
Summary:       Manages a MIME Content-Type database
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mime-types/ruby-mime-types
Vcs:           https://github.com/mime-types/ruby-mime-types.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(debug) >= 0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(hoe) >= 3.0
BuildRequires: gem(hoe-doofus) >= 1.0
BuildRequires: gem(hoe-gemspec2) >= 1.1
BuildRequires: gem(hoe-git2) >= 1.7
BuildRequires: gem(hoe-rubygems) >= 1.0
BuildRequires: gem(minitest-autotest) >= 1.0
BuildRequires: gem(minitest-focus) >= 1.0
BuildRequires: gem(minitest-hooks) >= 1.4
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(standard) >= 1.0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(mime-types-data) >= 3.2015
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(hoe-doofus) >= 2
BuildConflicts: gem(hoe-gemspec2) >= 2
BuildConflicts: gem(hoe-git2) >= 2
BuildConflicts: gem(hoe-rubygems) >= 2
BuildConflicts: gem(minitest-autotest) >= 2
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(minitest-hooks) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(mime-types-data) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(mime-types-data) >= 3.2015
Conflicts:     gem(mime-types-data) >= 4
Obsoletes:     ruby-mime-types < %EVR
Provides:      ruby-mime-types = %EVR
Provides:      gem(mime-types) = 3.5.2


%description
Manages a MIME Content-Type database that will return the Content-Type for a
given filename.

MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copy right 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.


%if_enabled    doc
%package       -n gem-mime-types-doc
Version:       3.5.2
Release:       alt1
Summary:       Manages a MIME Content-Type database documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mime-types
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mime-types) = 3.5.2

%description   -n gem-mime-types-doc
Manages a MIME Content-Type database documentation files.

Manages a MIME Content-Type database that will return the Content-Type for a
given filename.

MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copy right 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.

%description   -n gem-mime-types-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mime-types.
%endif


%if_enabled    devel
%package       -n gem-mime-types-devel
Version:       3.5.2
Release:       alt1
Summary:       Manages a MIME Content-Type database development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mime-types
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mime-types) = 3.5.2
Requires:      gem(debug) >= 0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(hoe) >= 3.0
Requires:      gem(hoe-doofus) >= 1.0
Requires:      gem(hoe-gemspec2) >= 1.1
Requires:      gem(hoe-git2) >= 1.7
Requires:      gem(hoe-rubygems) >= 1.0
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-focus) >= 1.0
Requires:      gem(minitest-hooks) >= 1.4
Requires:      gem(rake) >= 10.0
Requires:      gem(standard) >= 1.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(hoe-doofus) >= 2
Conflicts:     gem(hoe-gemspec2) >= 2
Conflicts:     gem(hoe-git2) >= 2
Conflicts:     gem(hoe-rubygems) >= 2
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(minitest-hooks) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(standard) >= 2
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(simplecov) >= 1

%description   -n gem-mime-types-devel
Manages a MIME Content-Type database development package.

Manages a MIME Content-Type database that will return the Content-Type for a
given filename.

MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copy right 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.

%description   -n gem-mime-types-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mime-types.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-mime-types-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mime-types-devel
%doc README.rdoc
%endif


%changelog
* Wed Jul 31 2024 Pavel Skrylev <majioa@altlinux.org> 3.5.2-alt1
- ^ 3.4.1 -> 3.5.2

* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 3.4.1-alt1
- ^ 3.3.1 -> 3.4.1

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 3.3.1-alt1
- ^ 3.3 -> 3.3.1

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 3.3-alt1
- update (^) 3.2.2 -> 3.3
- update to (^) Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Mar 30 2017 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- New version

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.2-alt1
- New version
- Update homepage to https://github.com/mime-types/ruby-mime-types

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.18-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Apr 18 2012 Igor Zubkov <icesik@altlinux.org> 1.18-alt1
- 1.16 -> 1.18
- Fix repocop warning

* Sat Dec 12 2009 Igor Zubkov <icesik@altlinux.org> 1.16-alt1
- build for Sisyphus
