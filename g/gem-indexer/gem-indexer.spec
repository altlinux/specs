%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname indexer

Name:          gem-indexer
Version:       0.3.1
Release:       alt1
Summary:       Enable Your Project's Metadata
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://rubyworks.github.com/indexer
Vcs:           https://github.com/rubyworks/indexer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(ae) >= 0
BuildConflicts: gem(qed) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(indexer) = 0.3.1

%description
Indexer provides projects with a universal metadata format.


%package       -n index
Version:       0.3.1
Release:       alt1
Summary:       Enable Your Project's Metadata executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета indexer
Group:         Other
BuildArch:     noarch

Requires:      gem(indexer) = 0.3.1

%description   -n index
Enable Your Project's Metadata executable(s).

Indexer provides projects with a universal metadata format.

%description   -n index -l ru_RU.UTF-8
Исполнямка для самоцвета indexer.


%if_enabled    doc
%package       -n gem-indexer-doc
Version:       0.3.1
Release:       alt1
Summary:       Enable Your Project's Metadata documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета indexer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(indexer) = 0.3.1

%description   -n gem-indexer-doc
Enable Your Project's Metadata documentation files.

Indexer provides projects with a universal metadata format.

%description   -n gem-indexer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета indexer.
%endif


%if_enabled    devel
%package       -n gem-indexer-devel
Version:       0.3.1
Release:       alt1
Summary:       Enable Your Project's Metadata development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета indexer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(indexer) = 0.3.1
Requires:      gem(ae) >= 0
Conflicts:     gem(qed) >= 0

%description   -n gem-indexer-devel
Enable Your Project's Metadata development package.

Indexer provides projects with a universal metadata format.

%description   -n gem-indexer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета indexer.
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
%doc HISTORY.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n index
%doc HISTORY.md README.md
%_bindir/index

%if_enabled    doc
%files         -n gem-indexer-doc
%doc HISTORY.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-indexer-devel
%doc HISTORY.md README.md
%endif


%changelog
* Wed Sep 23 2026 Pavel Skrylev <majioa@altlinux.org> 0.3.1-alt1
- ^ 0.3.0 -> 0.3.1

* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
