%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname manpages

Name:          gem-manpages
Version:       0.7.0
Release:       alt1
Summary:       Adds support for man pages to rubygems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bitboxer/manpages
Vcs:           https://github.com/bitboxer/manpages.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rexml) >= 3.3.9
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.0
BuildRequires: gem(rubocop-rspec) >= 0
BuildConflicts: gem(parallel) >= 2
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.0
Provides:      gem(manpages) = 0.7.0

%description
With this gem the rubygems command will detect man pages within gems and exposes
them to the man command.


%if_enabled    doc
%package       -n gem-manpages-doc
Version:       0.7.0
Release:       alt1
Summary:       Adds support for man pages to rubygems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета manpages
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(manpages) = 0.7.0

%description   -n gem-manpages-doc
Adds support for man pages to rubygems documentation files.

With this gem the rubygems command will detect man pages within gems and exposes
them to the man command.

%description   -n gem-manpages-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета manpages.
%endif


%if_enabled    devel
%package       -n gem-manpages-devel
Version:       0.7.0
Release:       alt1
Summary:       Adds support for man pages to rubygems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета manpages
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(manpages) = 0.7.0
Requires:      gem(bundler) >= 2.0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rexml) >= 3.3.9
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.0
Requires:      gem(rubocop-rspec) >= 0
Conflicts:     gem(parallel) >= 2
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-manpages-devel
Adds support for man pages to rubygems development package.

With this gem the rubygems command will detect man pages within gems and exposes
them to the man command.

%description   -n gem-manpages-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета manpages.
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
%doc .github_changelog_generator CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemplugin

%if_enabled    doc
%files         -n gem-manpages-doc
%doc .github_changelog_generator CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-manpages-devel
%doc .github_changelog_generator CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 0.7.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
