%define        gemname simple_oauth

Name:          gem-simple-oauth
Version:       0.3.0
Release:       alt1
Summary:       Simply builds and verifies OAuth headers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/laserlemon/simple_oauth
Vcs:           https://github.com/laserlemon/simple_oauth.git
Packager:      Andrey Cherepanov <cas@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-test-unit
BuildRequires: ruby-tool-rdoc
BuildRequires: gem(bundler) >= 1.0 gem(bundler) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_ignore_names fixtures
Obsoletes:     ruby-simple_oauth < %EVR
Provides:      ruby-simple_oauth = %EVR
Provides:      gem(simple_oauth) = 0.3.0


%description
Simply builds and verifies OAuth headers.


%package       -n gem-simple-oauth-doc
Version:       0.3.0
Release:       alt1
Summary:       Simply builds and verifies OAuth headers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simple_oauth
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(simple_oauth) = 0.3.0

%description   -n gem-simple-oauth-doc
Simply builds and verifies OAuth headers documentation files.

Simply builds and verifies OAuth headers.

%description   -n gem-simple-oauth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simple_oauth.


%package       -n gem-simple-oauth-devel
Version:       0.3.0
Release:       alt1
Summary:       Simply builds and verifies OAuth headers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета simple_oauth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(simple_oauth) = 0.3.0
Requires:      gem(bundler) >= 1.0 gem(bundler) < 3

%description   -n gem-simple-oauth-devel
Simply builds and verifies OAuth headers development package.

Simply builds and verifies OAuth headers.

%description   -n gem-simple-oauth-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета simple_oauth.


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

%files         -n gem-simple-oauth-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-simple-oauth-devel
%doc README.md


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- ^ 0.2.0 -> 0.3.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt1
- Initial build for ALT Linux
