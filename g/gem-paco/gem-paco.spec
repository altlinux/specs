%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname paco

Name:          gem-paco
Version:       0.2.3
Release:       alt1
Summary:       Parser combinator library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/skryukov/paco
Vcs:           https://github.com/skryukov/paco.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(ruby-next) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(paco) = 0.2.3


%description
Paco is a parser combinator library.


%if_enabled    doc
%package       -n gem-paco-doc
Version:       0.2.3
Release:       alt1
Summary:       Parser combinator library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета paco
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(paco) = 0.2.3

%description   -n gem-paco-doc
Parser combinator library documentation files.

Paco is a parser combinator library.
%description   -n gem-paco-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета paco.
%endif


%if_enabled    devel
%package       -n gem-paco-devel
Version:       0.2.3
Release:       alt1
Summary:       Parser combinator library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета paco
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(paco) = 0.2.3
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0
Requires:      gem(standard) >= 0
Requires:      gem(ruby-next) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-paco-devel
Parser combinator library development package.

Paco is a parser combinator library.
%description   -n gem-paco-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета paco.
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

%if_enabled    doc
%files         -n gem-paco-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-paco-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt1
- + packaged gem with Ruby Policy 2.0
