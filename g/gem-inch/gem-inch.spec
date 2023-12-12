%define        _unpackaged_files_terminate_build 1
%define        gemname inch

Name:          gem-inch
Version:       0.8.0
Release:       alt1
Summary:       Documentation measurement tool for Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://trivelop.de/inch/
Vcs:           https://github.com/rrrene/inch.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.5
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 5.2
BuildRequires: gem(rubocop) >= 0.25.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(sparkr) >= 0.2.0
BuildRequires: gem(term-ansicolor) >= 0
BuildRequires: gem(yard) >= 0.9.12
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      gem(pry) >= 0
Requires:      gem(sparkr) >= 0.2.0
Requires:      gem(term-ansicolor) >= 0
Requires:      gem(yard) >= 0.9.12
Conflicts:     gem(yard) >= 1
Provides:      gem(inch) = 0.8.0

%ruby_bindir_to %ruby_bindir

%description
Documentation measurement tool for Ruby, based on YARD.


%package       -n inch
Version:       0.8.0
Release:       alt1
Summary:       Documentation measurement tool for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета inch
Group:         Other
BuildArch:     noarch

Requires:      gem(inch) = 0.8.0

%description   -n inch
Documentation measurement tool for Ruby executable(s).

Documentation measurement tool for Ruby, based on YARD.

%description   -n inch -l ru_RU.UTF-8
Исполнямка для самоцвета inch.


%package       -n gem-inch-doc
Version:       0.8.0
Release:       alt1
Summary:       Documentation measurement tool for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inch) = 0.8.0

%description   -n gem-inch-doc
Documentation measurement tool for Ruby documentation files.

Documentation measurement tool for Ruby, based on YARD.

%description   -n gem-inch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inch.


%package       -n gem-inch-devel
Version:       0.8.0
Release:       alt1
Summary:       Documentation measurement tool for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inch) = 0.8.0
Requires:      gem(bundler) >= 1.5
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 5.2
Requires:      gem(rubocop) >= 0.25.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rubocop) >= 2

%description   -n gem-inch-devel
Documentation measurement tool for Ruby development package.

Documentation measurement tool for Ruby, based on YARD.

%description   -n gem-inch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inch.


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

%files         -n inch
%doc README.md
%ruby_bindir/inch

%files         -n gem-inch-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-inch-devel
%doc README.md


%changelog
* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- + packaged gem with Ruby Policy 2.0
