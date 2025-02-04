%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname opencensus

Name:          gem-opencensus
Version:       0.5.0.4
Release:       alt1
Summary:       A stats collection and distributed tracing framework
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/census-instrumentation/opencensus-ruby
Vcs:           https://github.com/census-instrumentation/opencensus-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.17
BuildRequires: gem(rake) >= 12.0
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(faraday) >= 0.14
BuildRequires: gem(jekyll) >= 3.6.2
BuildRequires: gem(jekyll-theme-minimal) >= 0.1
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(rails) >= 5.1.4
BuildRequires: gem(rubocop) >= 0.59.2
BuildRequires: gem(sinatra) >= 2.0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-doctest) >= 0.1.6
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(jekyll) >= 5
BuildConflicts: gem(jekyll-theme-minimal) >= 1
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(rails) >= 8
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(sinatra) >= 5
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(yard-doctest) >= 0.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rails >= 7.1,rails < 8
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_use_gem_dependency jekyll >= 4.3.2,jekyll < 5
%ruby_use_gem_dependency sinatra >= 4.0.0,sinatra < 5
Requires:      ruby >= 2.2.0
Provides:      gem(opencensus) = 0.5.0.4

%description
A stats collection and distributed tracing framework


%if_enabled    doc
%package       -n gem-opencensus-doc
Version:       0.5.0.4
Release:       alt1
Summary:       A stats collection and distributed tracing framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета opencensus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(opencensus) = 0.5.0.4

%description   -n gem-opencensus-doc
A stats collection and distributed tracing framework documentation files.

%description   -n gem-opencensus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета opencensus.
%endif


%if_enabled    devel
%package       -n gem-opencensus-devel
Version:       0.5.0.4
Release:       alt1
Summary:       A stats collection and distributed tracing framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета opencensus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(opencensus) = 0.5.0.4
Requires:      gem(bundler) >= 1.17
Requires:      gem(faraday) >= 0.13
Requires:      gem(jekyll) >= 3.6.2
Requires:      gem(jekyll-theme-minimal) >= 0.1
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(rails) >= 5.1.4
Requires:      gem(rake) >= 12.0
Requires:      gem(rubocop) >= 0.59.2
Requires:      gem(sinatra) >= 2.0
Requires:      gem(yard) >= 0.9
Requires:      gem(yard-doctest) >= 0.1.6
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(jekyll) >= 5
Conflicts:     gem(jekyll-theme-minimal) >= 1
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(rails) >= 8
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(sinatra) >= 5
Conflicts:     gem(yard) >= 1
Conflicts:     gem(yard-doctest) >= 0.2

%description   -n gem-opencensus-devel
A stats collection and distributed tracing framework development package.

%description   -n gem-opencensus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета opencensus.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-opencensus-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-opencensus-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.5.0.4-alt1
- ^ 0.5.0 -> 0.5.0p4

* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0
