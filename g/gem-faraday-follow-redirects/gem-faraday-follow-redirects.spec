%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname faraday-follow_redirects

Name:          gem-faraday-follow-redirects
Version:       0.4.0
Release:       alt1
Summary:       Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tisba/faraday-follow-redirects
Vcs:           https://github.com/tisba/faraday-follow-redirects.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(faraday) >= 1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-packaging) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(webmock) >= 0
BuildConflicts: gem(faraday) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names faraday-follow_redirects,faraday-follow-redirects
Requires:      ruby >= 3.3.3
Requires:      gem(faraday) >= 1
Requires:      gem(rubocop-rake) >= 0
Conflicts:     gem(faraday) >= 3
Provides:      faraday-follow_redirects = %EVR
Provides:      gem(faraday-follow_redirects) = 0.4.0

%description
Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects.


%if_enabled    doc
%package       -n gem-faraday-follow-redirects-doc
Version:       0.4.0
Release:       alt1
Summary:       Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-follow_redirects
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(faraday-follow_redirects) = 0.4.0

%description   -n gem-faraday-follow-redirects-doc
Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects
documentation files.

%description   -n gem-faraday-follow-redirects-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-follow_redirects.
%endif


%if_enabled    devel
%package       -n gem-faraday-follow-redirects-devel
Version:       0.4.0
Release:       alt1
Summary:       Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-follow_redirects
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(faraday-follow_redirects) = 0.4.0
Requires:      gem(appraisal) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(faraday) >= 1
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-packaging) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(webmock) >= 0
Conflicts:     gem(faraday) >= 3

%description   -n gem-faraday-follow-redirects-devel
Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects
development package.

%description   -n gem-faraday-follow-redirects-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-follow_redirects.
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
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-faraday-follow-redirects-doc
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-faraday-follow-redirects-devel
%doc CHANGELOG.md LICENSE.md README.md
%endif


%changelog
* Sat Nov 15 2025 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- ^ 0.3.0 -> 0.4.0

* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
