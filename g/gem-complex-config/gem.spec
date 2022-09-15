%define        gemname complex_config

Name:          gem-complex-config
Version:       0.19.3
Release:       alt1
Summary:       configuration library
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/flori/complex_config
Vcs:           https://github.com/flori/complex_config.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(gem_hadar) >= 1.12.0 gem(gem_hadar) < 2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(monetize) >= 0
# BuildRequires: gem(utils) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(tins) >= 0
BuildRequires: gem(mize) >= 0.3.4 gem(mize) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.12.0,gem_hadar < 2
Requires:      gem(json) >= 0
Requires:      gem(tins) >= 0
Requires:      gem(mize) >= 0.3.4 gem(mize) < 1
Provides:      gem(complex_config) = 0.19.3


%description
This library allows you to access configuration files via a simple interface


%package       -n complex-config
Version:       0.19.3
Release:       alt1
Summary:       configuration library executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета complex_config
Group:         Other
BuildArch:     noarch

Requires:      gem(complex_config) = 0.19.3

%description   -n complex-config
configuration library executable(s).

This library allows you to access configuration files via a simple interface

%description   -n complex-config -l ru_RU.UTF-8
Исполнямка для самоцвета complex_config.


%package       -n gem-complex-config-doc
Version:       0.19.3
Release:       alt1
Summary:       configuration library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета complex_config
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(complex_config) = 0.19.3

%description   -n gem-complex-config-doc
configuration library documentation files.

This library allows you to access configuration files via a simple interface

%description   -n gem-complex-config-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета complex_config.


%package       -n gem-complex-config-devel
Version:       0.19.3
Release:       alt1
Summary:       configuration library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета complex_config
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(complex_config) = 0.19.3
Requires:      gem(gem_hadar) >= 1.12.0 gem(gem_hadar) < 2
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(monetize) >= 0
Requires:      gem(utils) >= 0

%description   -n gem-complex-config-devel
configuration library development package.

This library allows you to access configuration files via a simple interface

%description   -n gem-complex-config-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета complex_config.


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

%files         -n complex-config
%doc README.md
%_bindir/complex_config

%files         -n gem-complex-config-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-complex-config-devel
%doc README.md


%changelog
* Wed Jul 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.19.3-alt1
- + packaged gem with Ruby Policy 2.0
