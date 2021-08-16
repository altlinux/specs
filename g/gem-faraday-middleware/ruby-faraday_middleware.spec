%define        gemname faraday_middleware

Name:          gem-faraday-middleware
Version:       1.0.0
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
BuildRequires: gem(faraday) >= 1.0 gem(faraday) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names faraday_middleware,faraday-middleware
Requires:      gem(faraday) >= 1.0 gem(faraday) < 2
Obsoletes:     ruby-faraday_middleware < %EVR
Provides:      ruby-faraday_middleware = %EVR
Provides:      gem(faraday_middleware) = 1.0.0


%description
A collection of useful Faraday middleware.


%package       -n gem-faraday-middleware-doc
Version:       1.0.0
Release:       alt1
Summary:       Various Faraday middlewares for Faraday-based API wrappers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday_middleware
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday_middleware) = 1.0.0

%description   -n gem-faraday-middleware-doc
Various Faraday middlewares for Faraday-based API wrappers documentation
files.

A collection of useful Faraday middleware.

%description   -n gem-faraday-middleware-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday_middleware.


%package       -n gem-faraday-middleware-devel
Version:       1.0.0
Release:       alt1
Summary:       Various Faraday middlewares for Faraday-based API wrappers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday_middleware
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday_middleware) = 1.0.0

%description   -n gem-faraday-middleware-devel
Various Faraday middlewares for Faraday-based API wrappers development
package.

A collection of useful Faraday middleware.

%description   -n gem-faraday-middleware-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday_middleware.


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

%files         -n gem-faraday-middleware-devel
%doc README.md


%changelog
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
