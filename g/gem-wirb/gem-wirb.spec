%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname wirb

Name:          gem-wirb
Version:       3.0.0
Release:       alt1
Summary:       Don't use an IRB without WIRB
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/wirb
Vcs:           https://github.com/janlelis/wirb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(date) >= 0
BuildRequires: gem(diff-lcs) >= 1.6
BuildRequires: gem(fileutils) >= 0
BuildRequires: gem(irb) >= 0
BuildRequires: gem(ostruct) >= 0
BuildRequires: gem(paint) >= 0.9
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(ruby_engine) >= 2.0
BuildRequires: gem(stringio) >= 0
BuildConflicts: gem(diff-lcs) >= 3
BuildConflicts: gem(paint) >= 4.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(ruby_engine) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency diff-lcs >= 2.0.0,diff-lcs < 3
Requires:      ruby >= 3.0
Requires:      gem(paint) >= 0.9
Conflicts:     ruby >= 5.0
Conflicts:     gem(paint) >= 4.0
Obsoletes:     ruby-wirb < %EVR
Provides:      ruby-wirb = %EVR
Provides:      gem(wirb) = 3.0.0

%description
The WIRB gem syntax highlights Ruby objects. Works best as your default REPL
inspector (see usage section below), but does not require IRB.

Supported Rubies: 3.0, 2.7, 2.6, 2.5

Older Rubies, should work: 2.4, 2.3, 2.2, 2.1, 2.0, rubinius

Ancient Rubies (1.9, 1.8): Please use WIRB 1.0 Features:
* Syntax highlighting for inspected Ruby objects
* No monkey patches anywhere
* Support for generic objects, especially enumerators, and nested generic
objects
* Supports common standard library objects, like Set
* Color schemas customizable via YAML


%if_enabled    doc
%package       -n gem-wirb-doc
Version:       3.0.0
Release:       alt1
Summary:       Don't use an IRB without WIRB documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета wirb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(wirb) = 3.0.0

%description   -n gem-wirb-doc
Don't use an IRB without WIRB documentation files.

The WIRB gem syntax highlights Ruby objects. Works best as your default REPL
inspector (see usage section below), but does not require IRB.

Supported Rubies: 3.0, 2.7, 2.6, 2.5

Older Rubies, should work: 2.4, 2.3, 2.2, 2.1, 2.0, rubinius

Ancient Rubies (1.9, 1.8): Please use WIRB 1.0 Features:
* Syntax highlighting for inspected Ruby objects
* No monkey patches anywhere
* Support for generic objects, especially enumerators, and nested generic
objects
* Supports common standard library objects, like Set
* Color schemas customizable via YAML

%description   -n gem-wirb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета wirb.
%endif


%if_enabled    devel
%package       -n gem-wirb-devel
Version:       3.0.0
Release:       alt1
Summary:       Don't use an IRB without WIRB development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета wirb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(wirb) = 3.0.0
Requires:      gem(date) >= 0
Requires:      gem(diff-lcs) >= 1.6
Requires:      gem(fileutils) >= 0
Requires:      gem(irb) >= 0
Requires:      gem(ostruct) >= 0
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(ruby_engine) >= 2.0
Requires:      gem(stringio) >= 0
Conflicts:     gem(diff-lcs) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(ruby_engine) >= 3

%description   -n gem-wirb-devel
Don't use an IRB without WIRB development package.

The WIRB gem syntax highlights Ruby objects. Works best as your default REPL
inspector (see usage section below), but does not require IRB.

Supported Rubies: 3.0, 2.7, 2.6, 2.5

Older Rubies, should work: 2.4, 2.3, 2.2, 2.1, 2.0, rubinius

Ancient Rubies (1.9, 1.8): Please use WIRB 1.0 Features:
* Syntax highlighting for inspected Ruby objects
* No monkey patches anywhere
* Support for generic objects, especially enumerators, and nested generic
objects
* Supports common standard library objects, like Set
* Color schemas customizable via YAML

%description   -n gem-wirb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета wirb.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md COPYING.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-wirb-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md COPYING.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-wirb-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md COPYING.txt README.md
%endif


%changelog
* Thu May 21 2026 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.2.2 -> 3.0.0

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.2-alt1
- ^ 2.1.2 -> 2.2.2

* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus
