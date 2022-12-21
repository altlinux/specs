%define        gemname jwt

Name:          gem-jwt
Version:       2.5.0
Release:       alt1
Summary:       A pure ruby implementation of the RFC 7519 OAuth JSON Web Token (JWT) standard
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jwt/ruby-jwt
Vcs:           https://github.com/jwt/ruby-jwt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(reek) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Obsoletes:     ruby-jwt < %EVR
Provides:      ruby-jwt = %EVR
Provides:      gem(jwt) = 2.5.0


%description
A pure ruby implementation of the RFC 7519 OAuth JSON Web Token (JWT) standard.


%package       -n gem-jwt-doc
Version:       2.5.0
Release:       alt1
Summary:       A pure ruby implementation of the RFC 7519 OAuth JSON Web Token (JWT) standard documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jwt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jwt) = 2.5.0

%description   -n gem-jwt-doc
A pure ruby implementation of the RFC 7519 OAuth JSON Web Token (JWT) standard
documentation files.

%description   -n gem-jwt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jwt.


%package       -n gem-jwt-devel
Version:       2.5.0
Release:       alt1
Summary:       A pure ruby implementation of the RFC 7519 OAuth JSON Web Token (JWT) standard development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jwt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jwt) = 2.5.0
Requires:      gem(appraisal) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(reek) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(rubocop) >= 1.15.0 gem(rubocop) < 2

%description   -n gem-jwt-devel
A pure ruby implementation of the RFC 7519 OAuth JSON Web Token (JWT) standard
development package.

%description   -n gem-jwt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jwt.


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

%files         -n gem-jwt-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-jwt-devel
%doc README.md


%changelog
* Mon Dec 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 2.2.1 -> 2.5.0

* Mon Mar 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- updated (^) 2.1.0 -> 2.2.1
- used (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus
