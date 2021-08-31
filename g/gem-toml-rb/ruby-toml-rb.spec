%define        gemname toml-rb

Name:          gem-toml-rb
Version:       2.0.1
Release:       alt1
Summary:       A parser for TOML using Citrus library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/emancu/toml-rb
Vcs:           https://github.com/emancu/toml-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(citrus) >= 3.0 gem(citrus) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(citrus) >= 3.0 gem(citrus) < 4
Obsoletes:     ruby-toml-rb < %EVR
Provides:      ruby-toml-rb = %EVR
Provides:      gem(toml-rb) = 2.0.1


%description
A TomlRB parser using Citrus library. TomlRB specs supported: 0.4.0.


%package       -n gem-toml-rb-doc
Version:       2.0.1
Release:       alt1
Summary:       A parser for TOML using Citrus library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета toml-rb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(toml-rb) = 2.0.1

%description   -n gem-toml-rb-doc
A parser for TOML using Citrus library documentation files.

A TomlRB parser using Citrus library. TomlRB specs supported: 0.4.0.

%description   -n gem-toml-rb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета toml-rb.


%package       -n gem-toml-rb-devel
Version:       2.0.1
Release:       alt1
Summary:       A parser for TOML using Citrus library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета toml-rb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(toml-rb) = 2.0.1

%description   -n gem-toml-rb-devel
A parser for TOML using Citrus library development package.

A TomlRB parser using Citrus library. TomlRB specs supported: 0.4.0.

%description   -n gem-toml-rb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета toml-rb.


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

%files         -n gem-toml-rb-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-toml-rb-devel
%doc README.md


%changelog
* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- ^ 1.1.2 -> 2.0.1

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus.
