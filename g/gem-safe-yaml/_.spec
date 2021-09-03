%define        gemname safe_yaml

Name:          gem-safe-yaml
Version:       1.0.5
Release:       alt2.1
Summary:       Parse YAML safely
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/dtao/safe_yaml
Vcs:           https://github.com/dtao/safe_yaml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names safe_yaml,safe-yaml
Obsoletes:     ruby-safe_yaml
Provides:      ruby-safe_yaml
Provides:      gem(safe_yaml) = 1.0.5


%description
SameYAML provides an alternative implementation of YAML, load suitable for
accepting user input in Ruby applications


%package       -n safe-yaml
Version:       1.0.5
Release:       alt2.1
Summary:       Parse YAML safely executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета safe_yaml
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(safe_yaml) = 1.0.5
Obsoletes:     safe_yaml
Provides:      safe_yaml

%description   -n safe-yaml
Parse YAML safely executable(s).

SameYAML provides an alternative implementation of YAML, load suitable for
accepting user input in Ruby applications

%description   -n safe-yaml -l ru_RU.UTF-8
Исполнямка для самоцвета safe_yaml.


%package       -n gem-safe-yaml-doc
Version:       1.0.5
Release:       alt2.1
Summary:       Parse YAML safely documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета safe_yaml
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(safe_yaml) = 1.0.5
Obsoletes:     ruby-safe_yaml-doc
Provides:      ruby-safe_yaml-doc

%description   -n gem-safe-yaml-doc
Parse YAML safely documentation files.

SameYAML provides an alternative implementation of YAML, load suitable for
accepting user input in Ruby applications

%description   -n gem-safe-yaml-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета safe_yaml.


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

%files         -n safe-yaml
%doc README.md
%_bindir/safe_yaml

%files         -n gem-safe-yaml-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt2.1
- ! spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt2
- + obsoleting ruby-self_yaml package

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
