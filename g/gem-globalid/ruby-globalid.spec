%define        gemname globalid

Name:          gem-globalid
Version:       0.4.2
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
BuildRequires: gem(activesupport) >= 4.2.0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activesupport) >= 4.2.0
Obsoletes:     ruby-globalid < %EVR
Provides:      ruby-globalid = %EVR
Provides:      gem(globalid) = 0.4.2


%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and
eager loading.


%package       -n gem-globalid-doc
Version:       0.4.2
Release:       alt1
Summary:       Identify app models with a URI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета globalid
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(globalid) = 0.4.2

%description   -n gem-globalid-doc
Identify app models with a URI documentation files.

Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and
eager loading.

%description   -n gem-globalid-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета globalid.


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


%changelog
* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.2-alt1
- > Ruby Policy 2.0
- ^ 0.4.1 -> 0.4.2

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
