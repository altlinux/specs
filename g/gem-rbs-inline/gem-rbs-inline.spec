%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname rbs-inline

Name:          gem-rbs-inline
Version:       0.12.0
Release:       alt1
Summary:       Inline RBS type declaration
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/soutaro/rbs-inline
Vcs:           https://github.com/soutaro/rbs-inline.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(prism) >= 0.29
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rbs) >= 3.8.0
BuildRequires: gem(steep) >= 1.9.0
BuildRequires: gem(strscan) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(steep) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency steep >= 1.10.0,steep < 2
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      ruby >= 3.1.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(prism) >= 0.29
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rbs) >= 3.8.0
Requires:      gem(steep) >= 1.9.0
Requires:      gem(strscan) >= 0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(steep) >= 2
Provides:      gem(rbs-inline) = 0.12.0

%description
Inline RBS type declaration.


%package       -n rbs-inline
Version:       0.12.0
Release:       alt1
Summary:       Inline RBS type declaration executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rbs-inline
Group:         Other
BuildArch:     noarch

Requires:      gem(rbs-inline) = 0.12.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(rake) >= 13.1.0
Requires:      gem(steep) >= 1.9.0
Requires:      gem(strscan) >= 0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(steep) >= 2

%description   -n rbs-inline
Inline RBS type declaration executable(s).

%description   -n rbs-inline -l ru_RU.UTF-8
Исполнямка для самоцвета rbs-inline.


%if_enabled    doc
%package       -n gem-rbs-inline-doc
Version:       0.12.0
Release:       alt1
Summary:       Inline RBS type declaration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rbs-inline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rbs-inline) = 0.12.0

%description   -n gem-rbs-inline-doc
Inline RBS type declaration documentation files.

%description   -n gem-rbs-inline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rbs-inline.
%endif


%if_enabled    devel
%package       -n gem-rbs-inline-devel
Version:       0.12.0
Release:       alt1
Summary:       Inline RBS type declaration development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rbs-inline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rbs-inline) = 0.12.0

%description   -n gem-rbs-inline-devel
Inline RBS type declaration development package.

%description   -n gem-rbs-inline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rbs-inline.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rbs-inline
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%_bindir/rbs-inline

%if_enabled    doc
%files         -n gem-rbs-inline-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rbs-inline-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%endif


%changelog
* Wed Oct 22 2025 Pavel Skrylev <majioa@altlinux.org> 0.12.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
