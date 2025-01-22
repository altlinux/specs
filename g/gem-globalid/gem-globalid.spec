%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname globalid

Name:          gem-globalid
Version:       1.2.1
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
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(activemodel) >= 0
BuildRequires: gem(activesupport) >= 6.1
BuildRequires: gem(railties) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.0
Requires:      gem(activesupport) >= 6.1
Obsoletes:     ruby-globalid < %EVR
Provides:      ruby-globalid = %EVR
Provides:      globalid = %EVR
Provides:      gem(globalid) = 1.2.1

%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and eager
loading.


%if_enabled    doc
%package       -n gem-globalid-doc
Version:       1.2.1
Release:       alt1
Summary:       Identify app models with a URI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета globalid
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(globalid) = 1.2.1

%description   -n gem-globalid-doc
Identify app models with a URI documentation files.

Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and eager
loading.

%description   -n gem-globalid-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета globalid.
%endif


%if_enabled    devel
%package       -n gem-globalid-devel
Version:       1.2.1
Release:       alt1
Summary:       Identify app models with a URI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета globalid
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(globalid) = 1.2.1
Requires:      gem(activemodel) >= 0
Requires:      gem(railties) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-globalid-devel
Identify app models with a URI development package.

Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and eager
loading.

%description   -n gem-globalid-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета globalid.
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
%doc MIT-LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-globalid-doc
%doc MIT-LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-globalid-devel
%doc MIT-LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%endif


%changelog
* Tue Jan 21 2025 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt1
- ^ 1.0.0[1] -> 1.2.1

* Sun Oct 09 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.0.1-alt1
- ^ 1.0.0 -> 1.0.0[1]

* Thu Sep 01 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.4.2 -> 1.0.0

* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.2-alt1
- > Ruby Policy 2.0
- ^ 0.4.1 -> 0.4.2

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
