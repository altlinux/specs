%define        gemname faraday-em_http

Name:          gem-faraday-em-http
Version:       1.0.0
Release:       alt1
Summary:       Faraday adapter for Em::Http
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-em_http
Vcs:           https://github.com/lostisland/faraday-em_http.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(rubocop) >= 0.91.1 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Provides:      gem(faraday-em_http) = 1.0.0


%description
Faraday adapter for Em::Http.


%package       -n gem-faraday-em-http-doc
Version:       1.0.0
Release:       alt1
Summary:       Faraday adapter for Em::Http documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-em_http
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-em_http) = 1.0.0

%description   -n gem-faraday-em-http-doc
Faraday adapter for Em::Http documentation files.

Faraday adapter for Em::Http.

%description   -n gem-faraday-em-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-em_http.


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

%files         -n gem-faraday-em-http-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
