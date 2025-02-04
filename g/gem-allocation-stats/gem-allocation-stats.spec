%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname allocation_stats

Name:          gem-allocation-stats
Version:       0.1.5
Release:       alt1
Summary:       Tooling for tracing object allocations in Ruby 2.1
License:       Apache-v2.0
Group:         Development/Ruby
Url:           https://github.com/srawlins/allocation_stats
Vcs:           https://github.com/srawlins/allocation_stats.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(yajl-ruby) >= 1.1.0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names allocation_stats,allocation-stats
%ruby_use_gem_dependency bundler >= 1.4.3,bundler < 2
Requires:      ruby > 2.0.99
Provides:      gem(allocation_stats) = 0.1.5

%description
Tooling for tracing object allocations in Ruby 2.1


%if_enabled    doc
%package       -n gem-allocation-stats-doc
Version:       0.1.5
Release:       alt1
Summary:       Tooling for tracing object allocations in Ruby 2.1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета allocation_stats
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(allocation_stats) = 0.1.5

%description   -n gem-allocation-stats-doc
Tooling for tracing object allocations in Ruby 2.1 documentation files.

%description   -n gem-allocation-stats-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета allocation_stats.
%endif


%if_enabled    devel
%package       -n gem-allocation-stats-devel
Version:       0.1.5
Release:       alt1
Summary:       Tooling for tracing object allocations in Ruby 2.1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета allocation_stats
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(allocation_stats) = 0.1.5
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(yajl-ruby) >= 1.1.0
Requires:      gem(yard) >= 0
Conflicts:     gem(rspec) >= 4

%description   -n gem-allocation-stats-devel
Tooling for tracing object allocations in Ruby 2.1 development package.

%description   -n gem-allocation-stats-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета allocation_stats.
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
%doc CHANGELOG.markdown LICENSE README.markdown
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-allocation-stats-doc
%doc CHANGELOG.markdown LICENSE README.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-allocation-stats-devel
%doc CHANGELOG.markdown LICENSE README.markdown
%endif


%changelog
* Sun Jan 26 2025 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
