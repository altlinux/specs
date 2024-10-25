%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname github_api

Name:          gem-github-api
Version:       0.19.0
Release:       alt1
Summary:       Ruby client for the official GitHub API
License:       MIT
Group:         Development/Ruby
Url:           http://piotrmurach.github.io/github/
Vcs:           https://github.com/piotrmurach/github.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.5.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(cucumber) >= 2.1
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(rspec-its) >= 1
BuildRequires: gem(vcr) >= 3.0.3
BuildRequires: gem(webmock) >= 3.8
BuildRequires: gem(mime-types) >= 3.0
BuildRequires: gem(yard) >= 0.9.9
BuildRequires: gem(pry) >= 0
BuildRequires: gem(coveralls) >= 0.8.7
BuildRequires: gem(simplecov) >= 0.14.1
BuildRequires: gem(yardstick) >= 0.9.9
BuildRequires: gem(addressable) >= 2.4
BuildRequires: gem(hashie) >= 3.5.2
BuildRequires: gem(faraday) >= 0.8
BuildRequires: gem(oauth2) >= 1.0
BuildRequires: gem(descendants_tracker) >= 0.0.4
BuildConflicts: gem(cucumber) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-its) >= 2
BuildConflicts: gem(vcr) >= 3.1
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(mime-types) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(coveralls) >= 0.9
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(yardstick) >= 0.10
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(hashie) >= 5
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(oauth2) >= 3
BuildConflicts: gem(descendants_tracker) >= 0.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 3.0.0,rack < 4
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency hashie >= 4.0.0,hashie < 5
%ruby_use_gem_dependency oauth2 >= 2.0.0,oauth2 < 3
Requires:      gem(addressable) >= 2.4
Requires:      gem(hashie) >= 3.5.2
Requires:      gem(faraday) >= 0.8
Requires:      gem(oauth2) >= 1.0
Requires:      gem(descendants_tracker) >= 0.0.4
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(hashie) >= 5
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(oauth2) >= 3
Conflicts:     gem(descendants_tracker) >= 0.1
Provides:      gem(github_api) = 0.19.0


%description
Ruby client that supports all of the GitHub API methods. It"s build in a modular
way, that is, you can either instantiate the whole api wrapper Github.new or use
parts of it e.i. Github::Client::Repos.new if working solely with repositories
is your main concern. Intuitive query methods allow you easily call API
endpoints.


%if_enabled    doc
%package       -n gem-github-api-doc
Version:       0.19.0
Release:       alt1
Summary:       Ruby client for the official GitHub API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета github_api
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(github_api) = 0.19.0

%description   -n gem-github-api-doc
Ruby client for the official GitHub API documentation files.

Ruby client that supports all of the GitHub API methods. It"s build in a modular
way, that is, you can either instantiate the whole api wrapper Github.new or use
parts of it e.i. Github::Client::Repos.new if working solely with repositories
is your main concern. Intuitive query methods allow you easily call API
endpoints.

%description   -n gem-github-api-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета github_api.
%endif


%if_enabled    devel
%package       -n gem-github-api-devel
Version:       0.19.0
Release:       alt1
Summary:       Ruby client for the official GitHub API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета github_api
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(github_api) = 0.19.0
Requires:      gem(bundler) >= 1.5.0
Requires:      gem(rake) >= 0
Requires:      gem(cucumber) >= 2.1
Requires:      gem(rspec) >= 3
Requires:      gem(rspec-its) >= 1
Requires:      gem(vcr) >= 3.0.3
Requires:      gem(webmock) >= 3.8
Requires:      gem(mime-types) >= 3.0
Requires:      gem(yard) >= 0.9.9
Requires:      gem(pry) >= 0
Requires:      gem(coveralls) >= 0.8.7
Requires:      gem(simplecov) >= 0.14.1
Requires:      gem(yardstick) >= 0.9.9
Conflicts:     gem(cucumber) >= 3
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-its) >= 2
Conflicts:     gem(vcr) >= 3.1
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(rack) >= 4
Conflicts:     gem(mime-types) >= 4
Conflicts:     gem(yard) >= 1
Conflicts:     gem(coveralls) >= 0.9
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(yardstick) >= 0.10

%description   -n gem-github-api-devel
Ruby client for the official GitHub API development package.

Ruby client that supports all of the GitHub API methods. It"s build in a modular
way, that is, you can either instantiate the whole api wrapper Github.new or use
parts of it e.i. Github::Client::Repos.new if working solely with repositories
is your main concern. Intuitive query methods allow you easily call API
endpoints.

%description   -n gem-github-api-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета github_api.
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
%files         -n gem-github-api-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-github-api-devel
%doc README.md
%endif


%changelog
* Fri Oct 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.19.0-alt1
- + packaged gem with Ruby Policy 2.0
