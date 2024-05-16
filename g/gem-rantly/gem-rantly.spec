%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rantly

Name:          gem-rantly
Version:       2.0.0
Release:       alt1
Summary:       Ruby Imperative Random Data Generator and Quickcheck
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rantly-rb/rantly
Vcs:           https://github.com/rantly-rb/rantly.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(minitest) >= 5.10.0
BuildRequires: gem(rake) >= 12.0.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(rubocop) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Provides:      gem(rantly) = 2.0.0


%description
Ruby Imperative Random Data Generator and Quickcheck


%if_enabled    doc
%package       -n gem-rantly-doc
Version:       2.0.0
Release:       alt1
Summary:       Ruby Imperative Random Data Generator and Quickcheck documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rantly
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rantly) = 2.0.0

%description   -n gem-rantly-doc
Ruby Imperative Random Data Generator and Quickcheck documentation files.

%description   -n gem-rantly-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rantly.
%endif


%if_enabled    devel
%package       -n gem-rantly-devel
Version:       2.0.0
Release:       alt1
Summary:       Ruby Imperative Random Data Generator and Quickcheck development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rantly
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rantly) = 2.0.0
Requires:      gem(coveralls) >= 0
Requires:      gem(minitest) >= 5.10.0
Requires:      gem(rake) >= 12.0.0
Requires:      gem(simplecov) >= 0
Requires:      gem(rubocop) >= 0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14

%description   -n gem-rantly-devel
Ruby Imperative Random Data Generator and Quickcheck development package.

%description   -n gem-rantly-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rantly.
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
%files         -n gem-rantly-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rantly-devel
%doc README.md
%endif


%changelog
* Thu Apr 25 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
