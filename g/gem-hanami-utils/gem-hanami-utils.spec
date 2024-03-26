%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hanami-utils

Name:          gem-hanami-utils
Version:       2.1.0
Release:       alt1
Summary:       Ruby core extentions and Hanami utilities
License:       MIT
Group:         Development/Ruby
Url:           http://hanamirb.org
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.6
BuildRequires: gem(rake) >= 13
BuildRequires: gem(rspec) >= 3.9
BuildRequires: gem(rubocop) >= 1.0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(yard-junk) >= 0
BuildRequires: gem(multi_json) >= 1.0
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(dry-core) >= 1.0
BuildRequires: gem(dry-transformer) >= 1.0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(multi_json) >= 2
BuildConflicts: gem(dry-core) >= 2
BuildConflicts: gem(dry-transformer) >= 2
BuildConflicts: gem(concurrent-ruby) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(dry-core) >= 1.0
Requires:      gem(dry-transformer) >= 1.0
Requires:      gem(concurrent-ruby) >= 1.0
Conflicts:     gem(dry-core) >= 2
Conflicts:     gem(dry-transformer) >= 2
Conflicts:     gem(concurrent-ruby) >= 2
Provides:      gem(hanami-utils) = 2.1.0


%description
Hanami utilities


%if_enabled    doc
%package       -n gem-hanami-utils-doc
Version:       2.1.0
Release:       alt1
Summary:       Ruby core extentions and Hanami utilities documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hanami-utils
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hanami-utils) = 2.1.0

%description   -n gem-hanami-utils-doc
Ruby core extentions and Hanami utilities documentation files.
%description   -n gem-hanami-utils-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hanami-utils.
%endif


%if_enabled    devel
%package       -n gem-hanami-utils-devel
Version:       2.1.0
Release:       alt1
Summary:       Ruby core extentions and Hanami utilities development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hanami-utils
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hanami-utils) = 2.1.0
Requires:      gem(bundler) >= 1.6
Requires:      gem(rake) >= 13
Requires:      gem(rspec) >= 3.9
Requires:      gem(rubocop) >= 1.0
Requires:      gem(byebug) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(yard-junk) >= 0
Requires:      gem(multi_json) >= 1.0
Requires:      gem(codecov) >= 0
Requires:      gem(gson) >= 0.6
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(multi_json) >= 2

%description   -n gem-hanami-utils-devel
Ruby core extentions and Hanami utilities development package.
%description   -n gem-hanami-utils-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hanami-utils.
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
%files         -n gem-hanami-utils-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hanami-utils-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- + packaged gem with Ruby Policy 2.0
