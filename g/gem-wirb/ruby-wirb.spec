%define        gemname wirb

Name:          gem-wirb
Version:       2.2.2
Release:       alt1
Summary:       Don't use an IRB without WIRB
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/wirb
Vcs:           https://github.com/janlelis/wirb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(paint) >= 0.9 gem(paint) < 3.0
BuildRequires: gem(rspec) >= 2.14 gem(rspec) < 4
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(ruby_engine) >= 1.0 gem(ruby_engine) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency ruby_engine >= 2.0,ruby_engine < 3
Requires:      gem(paint) >= 0.9 gem(paint) < 3.0
Obsoletes:     ruby-wirb < %EVR
Provides:      ruby-wirb = %EVR
Provides:      gem(wirb) = 2.2.2


%description
The WIRB gem syntax highlights Ruby objects. Works best as your default REPL
inspector (see usage section below), but does not require IRB.

Supported Rubies: 3.0, 2.7, 2.6, 2.5

Older Rubies, should work: 2.4, 2.3, 2.2, 2.1, 2.0, rubinius

Ancient Rubies (1.9, 1.8): Please use WIRB 1.0
Features:
* Syntax highlighting for inspected Ruby objects
* No monkey patches anywhere
* Support for generic objects, especially enumerators, and nested generic
  objects
* Supports common standard library objects, like Set
* Color schemas customizable via YAML


%package       -n gem-wirb-doc
Version:       2.2.2
Release:       alt1
Summary:       Don't use an IRB without WIRB documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета wirb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(wirb) = 2.2.2

%description   -n gem-wirb-doc
Don't use an IRB without WIRB documentation files.

The WIRB gem syntax highlights Ruby objects. Works best as your default REPL
inspector (see usage section below), but does not require IRB.

Supported Rubies: 3.0, 2.7, 2.6, 2.5

Older Rubies, should work: 2.4, 2.3, 2.2, 2.1, 2.0, rubinius

Ancient Rubies (1.9, 1.8): Please use WIRB 1.0
Features:
* Syntax highlighting for inspected Ruby objects
* No monkey patches anywhere
* Support for generic objects, especially enumerators, and nested generic
  objects
* Supports common standard library objects, like Set
* Color schemas customizable via YAML


%description   -n gem-wirb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета wirb.


%package       -n gem-wirb-devel
Version:       2.2.2
Release:       alt1
Summary:       Don't use an IRB without WIRB development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета wirb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(wirb) = 2.2.2
Requires:      gem(rspec) >= 2.14 gem(rspec) < 4
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(ruby_engine) >= 1.0 gem(ruby_engine) < 3

%description   -n gem-wirb-devel
Don't use an IRB without WIRB development package.

The WIRB gem syntax highlights Ruby objects. Works best as your default REPL
inspector (see usage section below), but does not require IRB.

Supported Rubies: 3.0, 2.7, 2.6, 2.5

Older Rubies, should work: 2.4, 2.3, 2.2, 2.1, 2.0, rubinius

Ancient Rubies (1.9, 1.8): Please use WIRB 1.0
Features:
* Syntax highlighting for inspected Ruby objects
* No monkey patches anywhere
* Support for generic objects, especially enumerators, and nested generic
  objects
* Supports common standard library objects, like Set
* Color schemas customizable via YAML


%description   -n gem-wirb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета wirb.


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

%files         -n gem-wirb-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-wirb-devel
%doc README.md


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.2-alt1
- ^ 2.1.2 -> 2.2.2

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus
