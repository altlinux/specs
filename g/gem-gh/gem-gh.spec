%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gh

Name:          gem-gh
Version:       0.21.0
Release:       alt1
Summary:       layered github client
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/travis-ci/gh
Vcs:           https://github.com/travis-ci/gh.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-console) >= 0
BuildRequires: gem(activesupport) >= 6.1.3.2
BuildRequires: gem(addressable) >= 2.8
BuildRequires: gem(faraday) >= 2
BuildRequires: gem(faraday-retry) >= 0
BuildRequires: gem(faraday-typhoeus) >= 0
BuildRequires: gem(multi_json) >= 1
BuildRequires: gem(net-http-persistent) >= 4
BuildRequires: gem(net-http-pipeline) >= 0
BuildConflicts: gem(activesupport) >= 7.1
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(multi_json) >= 2
BuildConflicts: gem(net-http-persistent) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency activesupport >= 6.1.3.2,activesupport < 7
Requires:      gem(activesupport) >= 6.1.3.2
Requires:      gem(addressable) >= 2.8
Requires:      gem(faraday) >= 2
Requires:      gem(faraday-retry) >= 0
Requires:      gem(faraday-typhoeus) >= 0
Requires:      gem(multi_json) >= 1
Requires:      gem(net-http-persistent) >= 4
Requires:      gem(net-http-pipeline) >= 0
Conflicts:     gem(activesupport) >= 7.1
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(multi_json) >= 2
Conflicts:     gem(net-http-persistent) >= 5
Provides:      gem(gh) = 0.21.0


%description
multi-layer client for the github api v3


%if_enabled    doc
%package       -n gem-gh-doc
Version:       0.21.0
Release:       alt1
Summary:       layered github client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gh
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gh) = 0.21.0

%description   -n gem-gh-doc
layered github client documentation files.

multi-layer client for the github api v3

%description   -n gem-gh-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gh.
%endif


%if_enabled    devel
%package       -n gem-gh-devel
Version:       0.21.0
Release:       alt1
Summary:       layered github client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gh
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gh) = 0.21.0
Requires:      gem(rspec) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-console) >= 0

%description   -n gem-gh-devel
layered github client development package.

multi-layer client for the github api v3

%description   -n gem-gh-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gh.
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
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-gh-doc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gh-devel
%endif


%changelog
* Fri Oct 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.21.0-alt1
- + packaged gem with Ruby Policy 2.0
