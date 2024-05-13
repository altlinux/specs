%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname blockenspiel

Name:          gem-blockenspiel
Version:       0.5.0
Release:       alt1
Summary:       Blockenspiel is a helper library designed to make it easy to implement DSL blocks
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           http://dazuma.github.io/blockenspiel
Vcs:           https://github.com/dazuma/blockenspiel.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.8
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rdoc) >= 4.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(blockenspiel) = 0.5.0


%description
Blockenspiel is a helper library designed to make it easy to implement DSL
blocks. It is designed to be comprehensive and robust, supporting most common
usage patterns, and working correctly in the presence of nested blocks and
multithreading.


%if_enabled    doc
%package       -n gem-blockenspiel-doc
Version:       0.5.0
Release:       alt1
Summary:       Blockenspiel is a helper library designed to make it easy to implement DSL blocks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета blockenspiel
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(blockenspiel) = 0.5.0

%description   -n gem-blockenspiel-doc
Blockenspiel is a helper library designed to make it easy to implement DSL
blocks documentation files.

Blockenspiel is a helper library designed to make it easy to implement DSL
blocks. It is designed to be comprehensive and robust, supporting most common
usage patterns, and working correctly in the presence of nested blocks and
multithreading.

%description   -n gem-blockenspiel-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета blockenspiel.
%endif


%if_enabled    devel
%package       -n gem-blockenspiel-devel
Version:       0.5.0
Release:       alt1
Summary:       Blockenspiel is a helper library designed to make it easy to implement DSL blocks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета blockenspiel
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(blockenspiel) = 0.5.0
Requires:      gem(minitest) >= 5.8
Requires:      gem(rake) >= 10.0
Requires:      gem(rdoc) >= 4.2

%description   -n gem-blockenspiel-devel
Blockenspiel is a helper library designed to make it easy to implement DSL
blocks development package.

Blockenspiel is a helper library designed to make it easy to implement DSL
blocks. It is designed to be comprehensive and robust, supporting most common
usage patterns, and working correctly in the presence of nested blocks and
multithreading.

%description   -n gem-blockenspiel-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета blockenspiel.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-blockenspiel-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-blockenspiel-devel
%doc README.rdoc
%endif


%changelog
* Wed May 08 2024 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0
