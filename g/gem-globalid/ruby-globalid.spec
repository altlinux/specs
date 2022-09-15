%define        gemname globalid

Name:          gem-globalid
Version:       1.0.0
Release:       alt1
Summary:       Identify app models with a URI
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/globalid
Vcs:           https://github.com/rails/globalid.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 5.0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activesupport) >= 5.0
Obsoletes:     ruby-globalid < %EVR
Provides:      ruby-globalid = %EVR
Provides:      gem(globalid) = 1.0.0


%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and eager
loading.


%package       -n gem-globalid-doc
Version:       1.0.0
Release:       alt1
Summary:       Identify app models with a URI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета globalid
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(globalid) = 1.0.0

%description   -n gem-globalid-doc
Identify app models with a URI documentation files.

Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and eager
loading.

%description   -n gem-globalid-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета globalid.


%package       -n gem-globalid-devel
Version:       1.0.0
Release:       alt1
Summary:       Identify app models with a URI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета globalid
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(globalid) = 1.0.0
Requires:      gem(rake) >= 0

%description   -n gem-globalid-devel
Identify app models with a URI development package.

Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and eager
loading.

%description   -n gem-globalid-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета globalid.


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

%files         -n gem-globalid-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-globalid-devel
%doc README.md


%changelog
* Thu Sep 01 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.4.2 -> 1.0.0

* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.2-alt1
- > Ruby Policy 2.0
- ^ 0.4.1 -> 0.4.2

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
