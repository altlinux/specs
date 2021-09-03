%define        gemname kafo_parsers

Name:          gem-kafo-parsers
Version:       1.2.1
Release:       alt1
Summary:       This gem can parse values, validations, documentation, types, groups and conditions of parameters from your puppet modules
License:       GPL-3.0+
Group:         Development/Ruby
Url:           https://github.com/theforeman/kafo_parsers
Vcs:           https://github.com/theforeman/kafo_parsers.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.5 gem(bundler) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(ci_reporter_minitest) >= 0
BuildRequires: gem(rdoc) >= 3.9.0 gem(rdoc) < 7
BuildRequires: gem(json) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_alias_names kafo_parsers,kafo-parsers
Requires:      gem(rdoc) >= 3.9.0 gem(rdoc) < 7
Requires:      gem(json) >= 0
Provides:      gem(kafo_parsers) = 1.2.1


%description
This gem can parse values, validations, documentation, types, groups and
conditions of parameters from your puppet modules. Only thing you have to do is
provide a path to manifest file you want to be parsed.

The library is used in Kafo, which can be used to get an idea of what's possible
to build on top of this library.

Currently puppet classes and types (definitions) are supported.


%package       -n gem-kafo-parsers-doc
Version:       1.2.1
Release:       alt1
Summary:       This gem can parse values, validations, documentation, types, groups and conditions of parameters from your puppet modules documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kafo_parsers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kafo_parsers) = 1.2.1

%description   -n gem-kafo-parsers-doc
This gem can parse values, validations, documentation, types, groups and
conditions of parameters from your puppet modules documentation files.

This gem can parse values, validations, documentation, types, groups and
conditions of parameters from your puppet modules. Only thing you have to do is
provide a path to manifest file you want to be parsed.

The library is used in Kafo, which can be used to get an idea of what's possible
to build on top of this library.

Currently puppet classes and types (definitions) are supported.

%description   -n gem-kafo-parsers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета kafo_parsers.


%package       -n gem-kafo-parsers-devel
Version:       1.2.1
Release:       alt1
Summary:       This gem can parse values, validations, documentation, types, groups and conditions of parameters from your puppet modules development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета kafo_parsers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kafo_parsers) = 1.2.1
Requires:      gem(bundler) >= 1.5 gem(bundler) < 3
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(ci_reporter_minitest) >= 0

%description   -n gem-kafo-parsers-devel
This gem can parse values, validations, documentation, types, groups and
conditions of parameters from your puppet modules development package.

This gem can parse values, validations, documentation, types, groups and
conditions of parameters from your puppet modules. Only thing you have to do is
provide a path to manifest file you want to be parsed.

The library is used in Kafo, which can be used to get an idea of what's possible
to build on top of this library.

Currently puppet classes and types (definitions) are supported.

%description   -n gem-kafo-parsers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета kafo_parsers.


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

%files         -n gem-kafo-parsers-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-kafo-parsers-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt1
- ^ 1.0.0 -> 1.2.1

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
