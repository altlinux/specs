%define        gemname faraday_middleware

Name:          gem-faraday-middleware
Version:       1.2.0
Release:       alt1
Summary:       Various Faraday middlewares for Faraday-based API wrappers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday_middleware
Vcs:           https://github.com/lostisland/faraday_middleware.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(brotli) >= 0.1.8
BuildRequires: gem(hashie) >= 1.2
BuildRequires: gem(json) < 3
BuildRequires: gem(multi_xml) >= 0.5.3
BuildRequires: gem(rack) < 3
BuildRequires: gem(rack-cache) >= 1.1 gem(rack-cache) < 1.3
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rash_alt) >= 0.4.3
BuildRequires: gem(safe_yaml) >= 0
BuildRequires: gem(simple_oauth) >= 0.1 gem(simple_oauth) < 0.3
BuildRequires: gem(addressable) < 2.4
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(simplecov) >= 0.12.0 gem(simplecov) < 1
BuildRequires: gem(webmock) >= 2.3 gem(webmock) < 4
BuildRequires: gem(rubocop) >= 1.12.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-packaging) >= 0.4 gem(rubocop-packaging) < 1
BuildRequires: gem(rubocop-performance) >= 1.5.2 gem(rubocop-performance) < 2
BuildRequires: gem(faraday) >= 1.0 gem(faraday) < 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_alias_names faraday_middleware,faraday-middleware
Requires:      gem(rubocop) >= 1.12.0 gem(rubocop) < 2
Requires:      gem(rubocop-packaging) >= 0.4 gem(rubocop-packaging) < 1
Requires:      gem(rubocop-performance) >= 1.5.2 gem(rubocop-performance) < 2
Requires:      gem(faraday) >= 1.0 gem(faraday) < 3
Obsoletes:     ruby-faraday_middleware < %EVR
Provides:      ruby-faraday_middleware = %EVR
Provides:      gem(faraday_middleware) = 1.2.0


%description
A collection of useful Faraday middleware.


%package       -n gem-faraday-middleware-doc
Version:       1.2.0
Release:       alt1
Summary:       Various Faraday middlewares for Faraday-based API wrappers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday_middleware
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday_middleware) = 1.2.0

%description   -n gem-faraday-middleware-doc
Various Faraday middlewares for Faraday-based API wrappers documentation
files.

A collection of useful Faraday middleware.

%description   -n gem-faraday-middleware-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday_middleware.


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

%files         -n gem-faraday-middleware-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Oct 19 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- ^ 1.0.0 -> 1.2.0

* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.14.0 -> 1.0.0

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.14.0-alt1
- ^ 0.13.1 -> 0.14.0

* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.13.1-alt1
- > Ruby Policy 2.0
- ^ 0.12.2 -> 0.13.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.12.2-alt1
- Initial build for Sisyphus
