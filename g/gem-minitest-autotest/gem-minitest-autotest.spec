%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-autotest

Name:          gem-minitest-autotest
Version:       1.1.1
Release:       alt1.1
Summary:       autotest is a continous testing facility meant to be used during development
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-autotest
Vcs:           https://github.com/seattlerb/minitest-autotest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest-server) >= 1.0
BuildRequires: gem(path_expander) >= 1.0
BuildRequires: gem(minitest) >= 5.17.0
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
Requires:      gem(path_expander) >= 1.0
Conflicts:     gem(minitest-server) >= 2
Conflicts:     gem(path_expander) >= 2
Provides:      gem(minitest-autotest) = 1.1.1


%description
autotest is a continous testing facility meant to be used during development. As
soon as you save a file, autotest will run the corresponding dependent
tests.

minitest-autotest is the latest incarnation of the venerable and wise autotest.
This time, it talks to minitest via minitest-server. As a result, there is no
output parsing. There are no regexps to tweak. There's no cruft or overhead.


%package       -n autotest
Version:       1.1.1
Release:       alt1.1
Summary:       autotest is a continous testing facility meant to be used during development executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета minitest-autotest
Group:         Other
BuildArch:     noarch

Requires:      gem(minitest-autotest) = 1.1.1

%description   -n autotest
autotest is a continous testing facility meant to be used during development
executable(s).

autotest is a continous testing facility meant to be used during development. As
soon as you save a file, autotest will run the corresponding dependent
tests.

minitest-autotest is the latest incarnation of the venerable and wise autotest.
This time, it talks to minitest via minitest-server. As a result, there is no
output parsing. There are no regexps to tweak. There's no cruft or overhead.

%description   -n autotest -l ru_RU.UTF-8
Исполнямка для самоцвета minitest-autotest.


%if_enabled    doc
%package       -n gem-minitest-autotest-doc
Version:       1.1.1
Release:       alt1.1
Summary:       autotest is a continous testing facility meant to be used during development documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-autotest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-autotest) = 1.1.1

%description   -n gem-minitest-autotest-doc
autotest is a continous testing facility meant to be used during development
documentation files.

autotest is a continous testing facility meant to be used during development. As
soon as you save a file, autotest will run the corresponding dependent
tests.

minitest-autotest is the latest incarnation of the venerable and wise autotest.
This time, it talks to minitest via minitest-server. As a result, there is no
output parsing. There are no regexps to tweak. There's no cruft or overhead.

%description   -n gem-minitest-autotest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-autotest.
%endif


%if_enabled    devel
%package       -n gem-minitest-autotest-devel
Version:       1.1.1
Release:       alt1.1
Summary:       autotest is a continous testing facility meant to be used during development development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-autotest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-autotest) = 1.1.1
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 4.2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

%description   -n gem-minitest-autotest-devel
autotest is a continous testing facility meant to be used during development
development package.

autotest is a continous testing facility meant to be used during development. As
soon as you save a file, autotest will run the corresponding dependent
tests.

minitest-autotest is the latest incarnation of the venerable and wise autotest.
This time, it talks to minitest via minitest-server. As a result, there is no
output parsing. There are no regexps to tweak. There's no cruft or overhead.

%description   -n gem-minitest-autotest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-autotest.
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

%files         -n autotest
%doc README.rdoc
%_bindir/autotest

%if_enabled    doc
%files         -n gem-minitest-autotest-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-autotest-devel
%doc README.rdoc
%endif


%changelog
* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1.1
- ! spec

* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
