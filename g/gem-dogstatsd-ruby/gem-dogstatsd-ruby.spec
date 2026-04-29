%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dogstatsd-ruby

Name:          gem-dogstatsd-ruby
Version:       5.7.1
Release:       alt1
Summary:       A Ruby DogStatsd client
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/DataDog/dogstatsd-ruby
Vcs:           https://github.com/datadog/dogstatsd-ruby.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby
BuildRequires(pre): setup-rb
BuildRequires(pre): rake
%if_enabled check
BuildRequires: gem(allocation_stats) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(benchmark-memory) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(climate_control) >= 0.2.0
BuildRequires: gem(fakefs) >= 2.5.0
BuildRequires: gem(faker) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-matchers) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(parallel) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rspec-its) >= 0
BuildRequires: gem(single_cov) >= 0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(yard) >= 0.9.20
BuildConflicts: gem(climate_control) >= 2
BuildConflicts: gem(fakefs) >= 4
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency climate_control >= 1.2.0,climate_control < 2
%ruby_use_gem_dependency fakefs >= 2.5.0,fakefs < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      ruby >= 2.1.0
Provides:      gem(dogstatsd-ruby) = 5.7.1

%description
A Ruby DogStatsd client


%if_enabled    doc
%package       -n gem-dogstatsd-ruby-doc
Version:       5.7.1
Release:       alt1
Summary:       A Ruby DogStatsd client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dogstatsd-ruby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dogstatsd-ruby) = 5.7.1

%description   -n gem-dogstatsd-ruby-doc
A Ruby DogStatsd client documentation files.

%description   -n gem-dogstatsd-ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dogstatsd-ruby.
%endif


%if_enabled    devel
%package       -n gem-dogstatsd-ruby-devel
Version:       5.7.1
Release:       alt1
Summary:       A Ruby DogStatsd client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dogstatsd-ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dogstatsd-ruby) = 5.7.1
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(benchmark-memory) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(fakefs) >= 2.5.0
Requires:      gem(faker) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rspec-its) >= 0
Requires:      gem(timecop) >= 0
Requires:      gem(allocation_stats) >= 0
Requires:      gem(climate_control) >= 0.2.0
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-matchers) >= 0
Requires:      gem(parallel) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(single_cov) >= 0
Requires:      gem(yard) >= 0.9.20
Conflicts:     gem(climate_control) >= 2
Conflicts:     gem(fakefs) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-dogstatsd-ruby-devel
A Ruby DogStatsd client development package.

%description   -n gem-dogstatsd-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dogstatsd-ruby.
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
%doc LICENSE.txt README.md CHANGELOG.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-dogstatsd-ruby-doc
%doc LICENSE.txt README.md CHANGELOG.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dogstatsd-ruby-devel
%doc LICENSE.txt README.md CHANGELOG.md
%endif


%changelog
* Wed Apr 29 2026 Pavel Skrylev <majioa@altlinux.org> 5.7.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
