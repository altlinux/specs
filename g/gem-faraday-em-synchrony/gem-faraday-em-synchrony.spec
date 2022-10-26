%define        gemname faraday-em_synchrony

Name:          gem-faraday-em-synchrony
Version:       1.0.0.1
Release:       alt1
Summary:       Faraday adapter for EM::Synchrony
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-em_synchrony
Vcs:           https://github.com/lostisland/faraday-em_synchrony.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(em-http-request) >= 1.1
BuildRequires: gem(em-synchrony) >= 1.0.3
BuildRequires: gem(faraday) >= 1.0 gem(faraday) < 3
BuildRequires: gem(faraday-em_http) >= 1.0 gem(faraday-em_http) < 2
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(multipart-parser) >= 0.1.1 gem(multipart-parser) < 0.2
BuildRequires: gem(webmock) >= 3.4 gem(webmock) < 4
BuildRequires: gem(rubocop) >= 0.91.1 gem(rubocop) < 2
BuildRequires: gem(rubocop-packaging) >= 0.5 gem(rubocop-packaging) < 1
BuildRequires: gem(rubocop-performance) >= 1.0 gem(rubocop-performance) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency simplecov >= 2.0,faraday < 3
%ruby_alias_names faraday-em_synchrony,faraday-em-synchrony
Provides:      gem(faraday-em_synchrony) = 1.0.0.1

%ruby_use_gem_version faraday-em_synchrony:1.0.0.1

%description
Faraday adapter for EM::Synchrony


%package       -n gem-faraday-em-synchrony-doc
Version:       1.0.0.1
Release:       alt1
Summary:       Faraday adapter for EM::Synchrony documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-em_synchrony
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-em_synchrony) = 1.0.0.1

%description   -n gem-faraday-em-synchrony-doc
Faraday adapter for EM::Synchrony documentation files.

%description   -n gem-faraday-em-synchrony-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-em_synchrony.


%package       -n gem-faraday-em-synchrony-devel
Version:       1.0.0.1
Release:       alt1
Summary:       Faraday adapter for EM::Synchrony development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-em_synchrony
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-em_synchrony) = 1.0.0.1
Requires:      gem(em-http-request) >= 1.1
Requires:      gem(em-synchrony) >= 1.0.3
Requires:      gem(faraday) >= 1.0 gem(faraday) < 3
Requires:      gem(faraday-em_http) >= 1.0 gem(faraday-em_http) < 2
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(simplecov) >= 0.17 gem(simplecov) < 1
Requires:      gem(multipart-parser) >= 0.1.1 gem(multipart-parser) < 0.2
Requires:      gem(webmock) >= 3.4 gem(webmock) < 4
Requires:      gem(rubocop) >= 0.91.1 gem(rubocop) < 2
Requires:      gem(rubocop-packaging) >= 0.5 gem(rubocop-packaging) < 1
Requires:      gem(rubocop-performance) >= 1.0 gem(rubocop-performance) < 2

%description   -n gem-faraday-em-synchrony-devel
Faraday adapter for EM::Synchrony development package.

%description   -n gem-faraday-em-synchrony-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-em_synchrony.


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

%files         -n gem-faraday-em-synchrony-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-faraday-em-synchrony-devel
%doc README.md


%changelog
* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.0.1-alt1
- ^ 1.0.0 -> 1.0.0[1]

* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
