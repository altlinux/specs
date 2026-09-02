%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname declarative

Name:          gem-declarative
Version:       0.0.20.2
Release:       alt0.1
Summary:       DSL for nested schemas
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/apotonick/declarative
Vcs:           https://github.com/apotonick/declarative.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-line) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(trailblazer-core-utils) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.3.0
Obsoletes:     ruby-declarative < %EVR
Provides:      ruby-declarative = %EVR
Provides:      gem(declarative) = 0.0.20.2

%ruby_use_gem_version declarative:0.0.20.2

%description
DSL for nested generic schemas with inheritance and refining.


%if_enabled    doc
%package       -n gem-declarative-doc
Version:       0.0.20.2
Release:       alt0.1
Summary:       DSL for nested schemas documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета declarative
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(declarative) = 0.0.20.2

%description   -n gem-declarative-doc
DSL for nested schemas documentation files.

DSL for nested generic schemas with inheritance and refining.

%description   -n gem-declarative-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета declarative.
%endif


%if_enabled    devel
%package       -n gem-declarative-devel
Version:       0.0.20.2
Release:       alt0.1
Summary:       DSL for nested schemas development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета declarative
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(declarative) = 0.0.20.2
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-line) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(trailblazer-core-utils) >= 0

%description   -n gem-declarative-devel
DSL for nested schemas development package.

DSL for nested generic schemas with inheritance and refining.

%description   -n gem-declarative-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета declarative.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-declarative-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-declarative-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Tue Sep 01 2026 Pavel Skrylev <majioa@altlinux.org> 0.0.20.2-alt0.1
- ^ 0.0.20 -> 0.0.20p2

* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.20-alt1
- > Ruby Policy 2.0
- ^ 0.0.10 -> 0.0.20

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.10-alt1.1
- Rebuild for new Ruby autorequirements.

* Sun May 27 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.10-alt1
- Initial build for Sisyphus
