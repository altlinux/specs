%define        gemname faraday-follow_redirects

Name:          gem-faraday-follow-redirects
Version:       0.3.0
Release:       alt1
Summary:       Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tisba/faraday-follow-redirects
Vcs:           https://github.com/tisba/faraday-follow-redirects.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(appraisal) >= 2.4 gem(appraisal) < 3
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(webmock) >= 3.13.0 gem(webmock) < 4
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-packaging) >= 0.5.0 gem(rubocop-packaging) < 0.6
BuildRequires: gem(rubocop-performance) >= 1.11.3 gem(rubocop-performance) < 2
BuildRequires: gem(rubocop-rspec) >= 2.4.0 gem(rubocop-rspec) < 3
BuildRequires: gem(faraday) >= 1 gem(faraday) < 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Requires:      gem(faraday) >= 1 gem(faraday) < 3
Provides:      gem(faraday-follow_redirects) = 0.3.0


%description
Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects.


%package       -n gem-faraday-follow-redirects-doc
Version:       0.3.0
Release:       alt1
Summary:       Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-follow_redirects
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-follow_redirects) = 0.3.0

%description   -n gem-faraday-follow-redirects-doc
Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects
documentation files.

%description   -n gem-faraday-follow-redirects-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-follow_redirects.


%package       -n gem-faraday-follow-redirects-devel
Version:       0.3.0
Release:       alt1
Summary:       Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-follow_redirects
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-follow_redirects) = 0.3.0
Requires:      gem(appraisal) >= 2.4.0 gem(appraisal) < 3
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(simplecov) >= 0.17 gem(simplecov) < 1
Requires:      gem(webmock) >= 3.13.0 gem(webmock) < 4
Requires:      gem(rubocop) >= 1.15.0 gem(rubocop) < 2
Requires:      gem(rubocop-packaging) >= 0.5.0 gem(rubocop-packaging) < 0.6
Requires:      gem(rubocop-performance) >= 1.11.3 gem(rubocop-performance) < 2
Requires:      gem(rubocop-rspec) >= 2.4.0 gem(rubocop-rspec) < 3

%description   -n gem-faraday-follow-redirects-devel
Faraday 2.x compatible extraction of FaradayMiddleware::FollowRedirects
development package.

%description   -n gem-faraday-follow-redirects-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-follow_redirects.


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

%files         -n gem-faraday-follow-redirects-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-faraday-follow-redirects-devel
%doc README.md


%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
