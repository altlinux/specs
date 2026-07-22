%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname guard-rubocop

Name:          gem-guard-rubocop
Version:       1.5.0
Release:       alt2
Summary:       Guard plugin for RuboCop
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop/guard-rubocop
Vcs:           https://github.com/rubocop/guard-rubocop.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(guard) >= 2.0
BuildRequires: gem(guard-rspec) >= 4.2.3
BuildRequires: gem(launchy) >= 2.4
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0.7
BuildRequires: gem(simplecov-lcov) >= 0
BuildConflicts: gem(guard) >= 3
BuildConflicts: gem(guard-rspec) >= 5.0
BuildConflicts: gem(launchy) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.5
Requires:      gem(guard) >= 2.0
Conflicts:     gem(guard) >= 3
Conflicts:     gem(rubocop) >= 2
Provides:      gem(guard-rubocop) = 1.5.0

%description
Guard::RuboCop automatically checks Ruby code style with RuboCop when files are
modified.


%if_enabled    doc
%package       -n gem-guard-rubocop-doc
Version:       1.5.0
Release:       alt2
Summary:       Guard plugin for RuboCop documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета guard-rubocop
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard-rubocop) = 1.5.0

%description   -n gem-guard-rubocop-doc
Guard plugin for RuboCop documentation files.

Guard::RuboCop automatically checks Ruby code style with RuboCop when files are
modified.

%description   -n gem-guard-rubocop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета guard-rubocop.
%endif


%if_enabled    devel
%package       -n gem-guard-rubocop-devel
Version:       1.5.0
Release:       alt2
Summary:       Guard plugin for RuboCop development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета guard-rubocop
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard-rubocop) = 1.5.0
Requires:      gem(bundler) >= 0
Requires:      gem(guard-rspec) >= 4.2.3
Requires:      gem(launchy) >= 2.4
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0.7
Requires:      gem(simplecov-lcov) >= 0
Conflicts:     gem(guard-rspec) >= 5.0
Conflicts:     gem(launchy) >= 3
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1

%description   -n gem-guard-rubocop-devel
Guard plugin for RuboCop development package.

Guard::RuboCop automatically checks Ruby code style with RuboCop when files are
modified.

%description   -n gem-guard-rubocop-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета guard-rubocop.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-guard-rubocop-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-guard-rubocop-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.0-alt2
- enable check

* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
