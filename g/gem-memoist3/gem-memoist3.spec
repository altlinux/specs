%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname memoist3

Name:          gem-memoist3
Version:       1.0.0
Release:       alt1
Summary:       memoize methods invocation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/honzasterba/memoist
Vcs:           https://github.com/honzasterba/memoist.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(minitest) >= 5.10
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.2
Provides:      gem(memoist3) = 1.0.0

%description
memoize methods invocation


%if_enabled    doc
%package       -n gem-memoist3-doc
Version:       1.0.0
Release:       alt1
Summary:       memoize methods invocation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета memoist3
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(memoist3) = 1.0.0

%description   -n gem-memoist3-doc
memoize methods invocation documentation files.

%description   -n gem-memoist3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета memoist3.
%endif


%if_enabled    devel
%package       -n gem-memoist3-devel
Version:       1.0.0
Release:       alt1
Summary:       memoize methods invocation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета memoist3
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(memoist3) = 1.0.0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 5.10
Requires:      gem(rake) >= 0
Conflicts:     gem(minitest) >= 6

%description   -n gem-memoist3-devel
memoize methods invocation development package.

%description   -n gem-memoist3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета memoist3.
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
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-memoist3-doc
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-memoist3-devel
%doc CHANGELOG.md LICENSE.md README.md
%endif


%changelog
* Mon Jul 06 2026 Alexander Burmatov <thatman@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
