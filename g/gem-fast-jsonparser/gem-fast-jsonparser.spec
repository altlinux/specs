%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fast_jsonparser

Name:          gem-fast-jsonparser
Version:       0.6.0.2
Release:       alt0.1
Summary:       Fast Json Parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/anilmaurya/fast_jsonparser
Vcs:           https://github.com/anilmaurya/fast_jsonparser.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
BuildRequires: gcc-c++
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(oj) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(yajl-ruby) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.0
%ruby_alias_names fast_jsonparser,fast-jsonparser
Provides:      gem(fast_jsonparser) = 0.6.0.2

%ruby_use_gem_version fast_jsonparser:0.6.0.2

%description
Fast Json Parser


%if_enabled    doc
%package       -n gem-fast-jsonparser-doc
Version:       0.6.0.2
Release:       alt0.1
Summary:       Fast Json Parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fast_jsonparser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fast_jsonparser) = 0.6.0.2

%description   -n gem-fast-jsonparser-doc
Fast Json Parser documentation files.

%description   -n gem-fast-jsonparser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fast_jsonparser.
%endif


%if_enabled    devel
%package       -n gem-fast-jsonparser-devel
Version:       0.6.0.2
Release:       alt0.1
Summary:       Fast Json Parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fast_jsonparser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fast_jsonparser) = 0.6.0.2
Requires:      gem(bundler) >= 2.0
Requires:      gem(minitest) >= 5.0
Requires:      gem(oj) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(yajl-ruby) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14

%description   -n gem-fast-jsonparser-devel
Fast Json Parser development package.

%description   -n gem-fast-jsonparser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fast_jsonparser.
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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-fast-jsonparser-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fast-jsonparser-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_includedir/*
%endif


%changelog
* Tue Sep 01 2026 Pavel Skrylev <majioa@altlinux.org> 0.6.0.2-alt0.1
- ^ 0.6.0 -> 0.6.0p2

* Thu Aug 06 2026 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
