%define        pkgname faraday-middleware
%define        gemname faraday_middleware

Name: 	       gem-%pkgname
Version:       0.14.0
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

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary

%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.14.0-alt1
- ^ 0.13.1 -> 0.14.0
- ! spec tags

* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.13.1-alt1
- > Ruby Policy 2.0
- ^ 0.12.2 -> 0.13.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.12.2-alt1
- Initial build for Sisyphus
