%define        gemname kafo_wizards

Name:          gem-kafo-wizards
Version:       0.0.2
Release:       alt1
Summary:       This gem helps to create wizard like interfaces in terminal applications, has support for nesting and value validation
License:       GPLv3+
Group:         Development/Ruby
Url:           https://github.com/theforeman/kafo_wizards
Vcs:           https://github.com/theforeman/kafo_wizards.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.5 gem(bundler) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 4.0 gem(minitest) < 6
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(ci_reporter) >= 0
BuildRequires: gem(highline) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_alias_names kafo_wizards,kafo-wizards
Requires:      gem(highline) < 3
Provides:      gem(kafo_wizards) = 0.0.2


%description
With this gem it is possible to define form or wizard and display it to the user
using one of the defined backends. The form definition is independent on the
chosen backend so it can be changed freely. Currently only command line
(highline) backend is implemented, YAD or web based backend is planed.


%package       -n gem-kafo-wizards-doc
Version:       0.0.2
Release:       alt1
Summary:       This gem helps to create wizard like interfaces in terminal applications, has support for nesting and value validation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kafo_wizards
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kafo_wizards) = 0.0.2

%description   -n gem-kafo-wizards-doc
This gem helps to create wizard like interfaces in terminal applications, has
support for nesting and value validation documentation files.

With this gem it is possible to define form or wizard and display it to the user
using one of the defined backends. The form definition is independent on the
chosen backend so it can be changed freely. Currently only command line
(highline) backend is implemented, YAD or web based backend is planed.

%description   -n gem-kafo-wizards-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета kafo_wizards.


%package       -n gem-kafo-wizards-devel
Version:       0.0.2
Release:       alt1
Summary:       This gem helps to create wizard like interfaces in terminal applications, has support for nesting and value validation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета kafo_wizards
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kafo_wizards) = 0.0.2
Requires:      gem(bundler) >= 1.5 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(minitest) >= 4.0 gem(minitest) < 6
Requires:      gem(simplecov) >= 0 gem(simplecov) < 1
Requires:      gem(mocha) >= 0 gem(mocha) < 2
Requires:      gem(ci_reporter) >= 0

%description   -n gem-kafo-wizards-devel
This gem helps to create wizard like interfaces in terminal applications, has
support for nesting and value validation development package.

With this gem it is possible to define form or wizard and display it to the user
using one of the defined backends. The form definition is independent on the
chosen backend so it can be changed freely. Currently only command line
(highline) backend is implemented, YAD or web based backend is planed.

%description   -n gem-kafo-wizards-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета kafo_wizards.


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

%files         -n gem-kafo-wizards-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-kafo-wizards-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.2-alt1
- ^ 0.0.1 -> 0.0.2

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
