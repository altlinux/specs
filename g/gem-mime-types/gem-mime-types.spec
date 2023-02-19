%define        gemname mime-types

Name:          gem-mime-types
Version:       3.4.1
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
%if_with check
BuildRequires: gem(minitest) >= 5.14
BuildRequires: gem(hoe-doofus) >= 1.0
BuildRequires: gem(hoe-gemspec2) >= 1.1
BuildRequires: gem(hoe-git) >= 1.6
BuildRequires: gem(hoe-rubygems) >= 1.0
BuildRequires: gem(standard) >= 1.0
BuildRequires: gem(minitest-autotest) >= 1.0
BuildRequires: gem(minitest-focus) >= 1.0
BuildRequires: gem(minitest-bonus-assertions) >= 3.0
BuildRequires: gem(minitest-hooks) >= 1.4
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(simplecov) >= 0.7
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 3.23
BuildRequires: gem(mime-types-data) >= 3.2015
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(hoe-doofus) >= 2
BuildConflicts: gem(hoe-gemspec2) >= 2
BuildConflicts: gem(hoe-git) >= 2
BuildConflicts: gem(hoe-rubygems) >= 2
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(minitest-autotest) >= 2
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(minitest-bonus-assertions) >= 4
BuildConflicts: gem(minitest-hooks) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(hoe) >= 4
BuildConflicts: gem(mime-types-data) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(mime-types-data) >= 3.2015
Conflicts:     gem(mime-types-data) >= 4
Obsoletes:     ruby-mime-types < %EVR
Provides:      ruby-mime-types = %EVR
Provides:      gem(mime-types) = 3.4.1


%description
Manages a MIME Content-Type database that will return the Content-Type for a
given filename.

MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copy right 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.


%package       -n gem-mime-types-doc
Version:       3.4.1
Release:       alt1
Summary:       Manages a MIME Content-Type database documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mime-types
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mime-types) = 3.4.1

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


%package       -n gem-mime-types-devel
Version:       3.4.1
Release:       alt1
Summary:       Manages a MIME Content-Type database development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mime-types
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mime-types) = 3.4.1
Requires:      gem(minitest) >= 5.14
Requires:      gem(hoe-doofus) >= 1.0
Requires:      gem(hoe-gemspec2) >= 1.1
Requires:      gem(hoe-git) >= 1.6
Requires:      gem(hoe-rubygems) >= 1.0
Requires:      gem(standard) >= 1.0
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-focus) >= 1.0
Requires:      gem(minitest-bonus-assertions) >= 3.0
Requires:      gem(minitest-hooks) >= 1.4
Requires:      gem(rake) >= 10.0
Requires:      gem(simplecov) >= 0.7
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 3.23
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(hoe-doofus) >= 2
Conflicts:     gem(hoe-gemspec2) >= 2
Conflicts:     gem(hoe-git) >= 2
Conflicts:     gem(hoe-rubygems) >= 2
Conflicts:     gem(standard) >= 2
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(minitest-bonus-assertions) >= 4
Conflicts:     gem(minitest-hooks) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 4

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

%files         -n gem-mime-types-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-mime-types-devel
%doc README.rdoc


%changelog
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
