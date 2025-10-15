%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname faraday_middleware

Name:          gem-faraday-middleware
Version:       1.2.1
Release:       alt1
Summary:       Various Faraday middlewares for Faraday-based API wrappers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday_middleware
Vcs:           https://github.com/lostisland/faraday_middleware.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(faraday) >= 1.0
BuildRequires: gem(hashie) >= 1.2
BuildRequires: gem(multi_xml) >= 0.5.3
BuildRequires: gem(rack) >= 2
BuildRequires: gem(rack-cache) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rash_alt) >= 0.4.3
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(safe_yaml) >= 0
BuildRequires: gem(simple_oauth) >= 0.1
BuildRequires: gem(simplecov) >= 0.12.0
BuildRequires: gem(webmock) >= 2.3
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(simple_oauth) >= 1
BuildConflicts: gem(webmock) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 3.0.0,rack < 4
%ruby_use_gem_dependency simple_oauth >= 0.3.1,simple_oauth < 1
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_alias_names faraday_middleware,faraday-middleware
Requires:      ruby >= 2.3
Requires:      gem(faraday) >= 1.0
Conflicts:     gem(faraday) >= 3
Obsoletes:     ruby-faraday_middleware < %EVR
Provides:      ruby-faraday_middleware = %EVR
Provides:      gem(faraday_middleware) = 1.2.1

%description
A collection of useful Faraday middleware.


%if_enabled    doc
%package       -n gem-faraday-middleware-doc
Version:       1.2.1
Release:       alt1
Summary:       Various Faraday middlewares for Faraday-based API wrappers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday_middleware
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday_middleware) = 1.2.1

%description   -n gem-faraday-middleware-doc
Various Faraday middlewares for Faraday-based API wrappers documentation
files.

A collection of useful Faraday middleware.

%description   -n gem-faraday-middleware-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday_middleware.
%endif


%if_enabled    devel
%package       -n gem-faraday-middleware-devel
Version:       1.2.1
Release:       alt1
Summary:       Various Faraday middlewares for Faraday-based API wrappers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday_middleware
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday_middleware) = 1.2.1
Requires:      gem(faraday) >= 1.0
Requires:      gem(hashie) >= 1.2
Requires:      gem(multi_xml) >= 0.5.3
Requires:      gem(rack) >= 2
Requires:      gem(rack-cache) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rash_alt) >= 0.4.3
Requires:      gem(rspec) >= 3
Requires:      gem(safe_yaml) >= 0
Requires:      gem(simple_oauth) >= 0.1
Requires:      gem(simplecov) >= 0.12.0
Requires:      gem(webmock) >= 2.3
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(json) >= 3
Conflicts:     gem(rack) >= 4
Conflicts:     gem(simple_oauth) >= 1
Conflicts:     gem(webmock) >= 4

%description   -n gem-faraday-middleware-devel
Various Faraday middlewares for Faraday-based API wrappers development
package.

A collection of useful Faraday middleware.

%description   -n gem-faraday-middleware-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday_middleware.
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
%doc LICENSE.md README.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-faraday-middleware-doc
%doc LICENSE.md README.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-faraday-middleware-devel
%doc LICENSE.md README.md CONTRIBUTING.md
%endif


%changelog
* Wed Oct 15 2025 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt1
- ^ 1.2.0 -> 1.2.1

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
