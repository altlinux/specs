%define        gemname bundler_ext

Name:          gem-bundler-ext
Version:       0.4.2
Release:       alt1
Summary:       Simple library leveraging the Bundler Gemfile DSL
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bundlerext/bundler_ext
Vcs:           https://github.com/bundlerext/bundler_ext.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(rake) >= 12
BuildRequires: gem(rails) >= 0
BuildRequires: gem(bundler) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names bundler_ext,bundler-ext
Requires:      gem(bundler) >= 0
Obsoletes:     ruby-bundler-ext
Provides:      ruby-bundler-ext
Provides:      gem(bundler_ext) = 0.4.2


%description
Simple library leveraging the Bundler Gemfile DSL to load gems already on the
system and managed by the systems package manager (like yum/apt).


%package       -n gem-bundler-ext-doc
Version:       0.4.2
Release:       alt1
Summary:       Simple library leveraging the Bundler Gemfile DSL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bundler_ext
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bundler_ext) = 0.4.2

%description   -n gem-bundler-ext-doc
Simple library leveraging the Bundler Gemfile DSL documentation files.

Simple library leveraging the Bundler Gemfile DSL to load gems already on the
system and managed by the systems package manager (like yum/apt).

%description   -n gem-bundler-ext-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bundler_ext.


%package       -n gem-bundler-ext-devel
Version:       0.4.2
Release:       alt1
Summary:       Simple library leveraging the Bundler Gemfile DSL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bundler_ext
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bundler_ext) = 0.4.2
Requires:      gem(rspec) >= 3
Requires:      gem(rake) >= 12
Requires:      gem(rails) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rake) >= 14

%description   -n gem-bundler-ext-devel
Simple library leveraging the Bundler Gemfile DSL development package.

Simple library leveraging the Bundler Gemfile DSL to load gems already on the
system and managed by the systems package manager (like yum/apt).

%description   -n gem-bundler-ext-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bundler_ext.


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

%files         -n gem-bundler-ext-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-bundler-ext-devel
%doc README.md


%changelog
* Thu Mar 02 2023 Pavel Skrylev <majioa@altlinux.org> 0.4.2-alt1
- ^ 0.4.0 -> 0.4.2

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt2
- > Ruby Policy 2.0
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
