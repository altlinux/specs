%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-bisect

Name:          gem-minitest-bisect
Version:       1.7.0
Release:       alt1
Summary:       Hunting down random test failures can be very very difficult, sometimes impossible, but minitest-bisect makes it easy
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-bisect
Vcs:           https://github.com/seattlerb/minitest-bisect.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest-server) >= 1.0
BuildRequires: gem(path_expander) >= 1.1
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(rake) > 0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 4.2
BuildConflicts: gem(minitest-server) >= 2
BuildConflicts: gem(path_expander) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(hoe) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(minitest-server) >= 1.0
Requires:      gem(path_expander) >= 1.1
Conflicts:     gem(minitest-server) >= 2
Conflicts:     gem(path_expander) >= 2
Provides:      gem(minitest-bisect) = 1.7.0


%description
Hunting down random test failures can be very very difficult, sometimes
impossible, but minitest-bisect makes it easy.

minitest-bisect helps you isolate and debug random test failures.

If your tests only fail randomly, you can reproduce the error consistently by
using `--seed <num>`, but what then? How do you figure out which combination of
tests out of hundreds are responsible for the failure? You know which test is
failing, but what others are causing it to fail or were helping it succeed in a
different order? That's what minitest-bisect does best.


%package       -n minitest-bisect
Version:       1.7.0
Release:       alt1
Summary:       Hunting down random test failures can be very very difficult, sometimes impossible, but minitest-bisect makes it easy executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета minitest-bisect
Group:         Other
BuildArch:     noarch

Requires:      gem(minitest-bisect) = 1.7.0

%description   -n minitest-bisect
Hunting down random test failures can be very very difficult, sometimes
impossible, but minitest-bisect makes it easy executable(s).

%description   -n minitest-bisect -l ru_RU.UTF-8
Исполнямка для самоцвета minitest-bisect.


%if_enabled    doc
%package       -n gem-minitest-bisect-doc
Version:       1.7.0
Release:       alt1
Summary:       Hunting down random test failures can be very very difficult, sometimes impossible, but minitest-bisect makes it easy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-bisect
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-bisect) = 1.7.0

%description   -n gem-minitest-bisect-doc
Hunting down random test failures can be very very difficult, sometimes
impossible, but minitest-bisect makes it easy documentation files.

%description   -n gem-minitest-bisect-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-bisect.
%endif


%if_enabled    devel
%package       -n gem-minitest-bisect-devel
Version:       1.7.0
Release:       alt1
Summary:       Hunting down random test failures can be very very difficult, sometimes impossible, but minitest-bisect makes it easy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-bisect
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-bisect) = 1.7.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(rake) > 0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 4.2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

%description   -n gem-minitest-bisect-devel
Hunting down random test failures can be very very difficult, sometimes
impossible, but minitest-bisect makes it easy development package.

%description   -n gem-minitest-bisect-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-bisect.
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

%files         -n minitest-bisect
%doc README.rdoc
%_bindir/minitest_bisect

%if_enabled    doc
%files         -n gem-minitest-bisect-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-bisect-devel
%doc README.rdoc
%endif


%changelog
* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- ^ 1.5.1 -> 1.7.0

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.1-alt1
- + packaged gem with Ruby Policy 2.0
