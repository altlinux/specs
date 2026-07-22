%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname patience_diff

Name:          gem-patience-diff
Version:       1.2.0
Release:       alt1
Summary:       A Ruby implementation of the Patience diff algorithm
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/watt/ruby_patience_diff
Vcs:           https://github.com/watt/ruby_patience_diff.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 0
BuildRequires: gem(optimist) >= 3.0
BuildConflicts: gem(optimist) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names patience_diff,patience-diff
Requires:      gem(optimist) >= 3.0
Conflicts:     gem(optimist) >= 4
Provides:      gem(patience_diff) = 1.2.0

%description
A Ruby implementation of the Patience diff algorithm.

Patience Diff creates more readable diffs than other algorithms in some cases,
particularly when much of the content has changed between the documents being
compared. There's a great explanation and example [here][example].

Patience diff was originally written by Bram Cohen and is used in the
[Bazaar][bazaar] version control system. This version is loosely based off the
Python implementation in Bazaar.

[example]: http://alfedenzo.livejournal.com/170301.html [bazaar]:
http://bazaar.canonical.com/


%package       -n patience-diff
Version:       1.2.0
Release:       alt1
Summary:       A Ruby implementation of the Patience diff algorithm executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета patience_diff
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(patience_diff) = 1.2.0

%description   -n patience-diff
A Ruby implementation of the Patience diff algorithm executable(s).

%description   -n patience-diff -l ru_RU.UTF-8
Исполнямка для самоцвета patience_diff.


%if_enabled    doc
%package       -n gem-patience-diff-doc
Version:       1.2.0
Release:       alt1
Summary:       A Ruby implementation of the Patience diff algorithm documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета patience_diff
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(patience_diff) = 1.2.0

%description   -n gem-patience-diff-doc
A Ruby implementation of the Patience diff algorithm documentation files.

%description   -n gem-patience-diff-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета patience_diff.
%endif


%if_enabled    devel
%package       -n gem-patience-diff-devel
Version:       1.2.0
Release:       alt1
Summary:       A Ruby implementation of the Patience diff algorithm development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета patience_diff
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(patience_diff) = 1.2.0
Requires:      gem(hoe) >= 0

%description   -n gem-patience-diff-devel
A Ruby implementation of the Patience diff algorithm development package.

%description   -n gem-patience-diff-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета patience_diff.
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
%doc History.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n patience-diff
%doc History.txt README.md
%_bindir/patience_diff

%if_enabled    doc
%files         -n gem-patience-diff-doc
%doc History.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-patience-diff-devel
%doc History.txt README.md
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
