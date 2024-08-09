%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname bson

Name:          gem-bson
Version:       5.0.1
Release:       alt1
Summary:       Ruby Implementation of the BSON Specification (2.0.0+)
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://bsonspec.org
Vcs:           https://github.com/mongodb/bson-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(json) >= 0
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(fuubar) >= 0
BuildRequires: gem(rfc) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(activesupport) >= 7.1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
Obsoletes:     ruby-bson < %EVR
Provides:      ruby-bson = %EVR
Provides:      gem(bson) = 5.0.1


%description
An implementation of the BSON specification in Ruby.


%if_enabled    doc
%package       -n gem-bson-doc
Version:       5.0.1
Release:       alt1
Summary:       Ruby Implementation of the BSON Specification (2.0.0+) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bson
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bson) = 5.0.1

%description   -n gem-bson-doc
Ruby Implementation of the BSON Specification (2.0.0+) documentation files.

An implementation of the BSON specification in Ruby.

%description   -n gem-bson-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bson.
%endif


%if_enabled    devel
%package       -n gem-bson-devel
Version:       5.0.1
Release:       alt1
Summary:       Ruby Implementation of the BSON Specification (2.0.0+) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bson
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bson) = 5.0.1
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(rspec) >= 3
Requires:      gem(json) >= 0
Requires:      gem(ruby-prof) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(ruby-debug) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(fuubar) >= 0
Requires:      gem(rfc) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(activesupport) >= 7.1
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 3

%description   -n gem-bson-devel
Ruby Implementation of the BSON Specification (2.0.0+) development package.

An implementation of the BSON specification in Ruby.

%description   -n gem-bson-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bson.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-bson-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-bson-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 5.0.1-alt1
- ^ 4.14.1 -> 5.0.1

* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 4.14.1-alt1
- ^ 4.12.0 -> 4.14.1

* Sat Apr 24 2021 Pavel Skrylev <majioa@altlinux.org> 4.12.0-alt1
- new version 4.12.0

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 4.8.2-alt1
- ^ 4.4.2 -> 4.8.2
- ! spec tags

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 4.4.2-alt1
- > Ruby Policy 2.0
- ^ 4.3.0 -> 4.4.2

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.1
- Rebuild with Ruby 2.5.0

* Thu Jan 18 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Tue Sep 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- Initial build for Sisyphus
