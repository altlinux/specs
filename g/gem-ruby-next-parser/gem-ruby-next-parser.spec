%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby-next-parser

Name:          gem-ruby-next-parser
Version:       3.4.4.0
Release:       alt1
Summary:       A Ruby parser written in pure Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/whitequark/parser
Vcs:           https://github.com/whitequark/parser.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(parser) >= 3.0.3.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.0.0
Requires:      gem(parser) >= 3.0.3.1
Provides:      gem(ruby-next-parser) = 3.4.4.0

%ruby_on_build_rake_tasks generate_release

%description
A Ruby parser written in pure Ruby.


%if_enabled    doc
%package       -n gem-ruby-next-parser-doc
Version:       3.4.4.0
Release:       alt1
Summary:       A Ruby parser written in pure Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-next-parser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-next-parser) = 3.4.4.0

%description   -n gem-ruby-next-parser-doc
A Ruby parser written in pure Ruby documentation files.

%description   -n gem-ruby-next-parser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-next-parser.
%endif


%if_enabled    devel
%package       -n gem-ruby-next-parser-devel
Version:       3.4.4.0
Release:       alt1
Summary:       A Ruby parser written in pure Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-next-parser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-next-parser) = 3.4.4.0

%description   -n gem-ruby-next-parser-devel
A Ruby parser written in pure Ruby development package.

%description   -n gem-ruby-next-parser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-next-parser.
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
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-ruby-next-parser-doc
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-next-parser-devel
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Tue Sep 01 2026 Pavel Skrylev <majioa@altlinux.org> 3.4.4.0-alt1
- ^ 3.4.0.2 -> 3.4.4.0

* Tue Dec 09 2025 Pavel Skrylev <majioa@altlinux.org> 3.4.0.2-alt1
- ^ 3.2.2.4 -> 3.4.0.2

* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 3.2.2.4-alt1
- + packaged gem with Ruby Policy 2.0
