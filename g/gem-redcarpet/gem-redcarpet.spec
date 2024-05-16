%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname redcarpet

Name:          gem-redcarpet
Version:       3.6.0
Release:       alt1
Summary:       The safe Markdown parser, reloaded
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/vmg/redcarpet
Vcs:           https://github.com/vmg/redcarpet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13
BuildRequires: gem(rake-compiler) >= 1.1
BuildRequires: gem(test-unit) >= 3.3.5
BuildRequires: gem(benchmark-ips) >= 2.7.2
BuildRequires: gem(bluecloth) >= 2.2.0
BuildRequires: gem(kramdown) >= 1.13.2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(benchmark-ips) >= 3
BuildConflicts: gem(bluecloth) >= 2.3
BuildConflicts: gem(kramdown) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency benchmark-ips < 3
Obsoletes:     ruby-redcarpet < %EVR
Provides:      ruby-redcarpet = %EVR
Provides:      gem(redcarpet) = 3.6.0


%description
Redcarpet is a Ruby library for Markdown processing that smells like butterflies
and popcorn.


%package       -n redcarpet
Version:       3.6.0
Release:       alt1
Summary:       The safe Markdown parser, reloaded executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета redcarpet
Group:         Development/Other
BuildArch:     noarch

Requires:      gem(redcarpet) = 3.6.0

%description   -n redcarpet
The safe Markdown parser, reloaded executable(s).

Redcarpet is a Ruby library for Markdown processing that smells like butterflies
and popcorn.

%description   -n redcarpet -l ru_RU.UTF-8
Исполнямка для самоцвета redcarpet.


%if_enabled    doc
%package       -n gem-redcarpet-doc
Version:       3.6.0
Release:       alt1
Summary:       The safe Markdown parser, reloaded documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redcarpet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redcarpet) = 3.6.0

%description   -n gem-redcarpet-doc
The safe Markdown parser, reloaded documentation files.

Redcarpet is a Ruby library for Markdown processing that smells like butterflies
and popcorn.

%description   -n gem-redcarpet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redcarpet.
%endif


%if_enabled    devel
%package       -n gem-redcarpet-devel
Version:       3.6.0
Release:       alt1
Summary:       The safe Markdown parser, reloaded development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redcarpet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redcarpet) = 3.6.0
Requires:      gem(rake) >= 13
Requires:      gem(rake-compiler) >= 1.1
Requires:      gem(test-unit) >= 3.3.5
Requires:      gem(benchmark-ips) >= 2.7.2
Requires:      gem(bluecloth) >= 2.2.0
Requires:      gem(kramdown) >= 1.13.2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(benchmark-ips) >= 3
Conflicts:     gem(bluecloth) >= 2.3
Conflicts:     gem(kramdown) >= 3

%description   -n gem-redcarpet-devel
The safe Markdown parser, reloaded development package.

Redcarpet is a Ruby library for Markdown processing that smells like butterflies
and popcorn.

%description   -n gem-redcarpet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redcarpet.
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
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n redcarpet
%doc README.markdown
%_bindir/redcarpet

%if_enabled    doc
%files         -n gem-redcarpet-doc
%doc README.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-redcarpet-devel
%doc README.markdown
%ruby_includedir/*
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt1
- ^ 3.5.1[1] -> 3.6.0

* Tue May 17 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.1.1-alt1
- ^ 3.5.1 -> 3.5.1[.1]

* Sat Apr 24 2021 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1
- ^ 3.5.0 -> 3.5.1

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- ^ 3.4.0 -> 3.5.0
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.4.0-alt2
- > Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- Initial build for Sisyphus
