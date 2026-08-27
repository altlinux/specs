%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-fail-fast

Name:          gem-minitest-fail-fast
Version:       0.2.0
Release:       alt1
Summary:       Fail and exit as soon as a test fails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/teoljungberg/minitest-fail-fast
Vcs:           https://github.com/teoljungberg/minitest-fail-fast.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rake) >= 13.1.0
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Requires:      gem(minitest) >= 5.0
Conflicts:     gem(minitest) >= 7
Provides:      gem(minitest-fail-fast) = 0.2.0

%description
Reimplements RSpec's "fail fast" feature for minitest


%if_enabled    doc
%package       -n gem-minitest-fail-fast-doc
Version:       0.2.0
Release:       alt1
Summary:       Fail and exit as soon as a test fails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-fail-fast
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-fail-fast) = 0.2.0

%description   -n gem-minitest-fail-fast-doc
Fail and exit as soon as a test fails documentation files.

Reimplements RSpec's "fail fast" feature for minitest

%description   -n gem-minitest-fail-fast-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-fail-fast.
%endif


%if_enabled    devel
%package       -n gem-minitest-fail-fast-devel
Version:       0.2.0
Release:       alt1
Summary:       Fail and exit as soon as a test fails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-fail-fast
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-fail-fast) = 0.2.0
Requires:      gem(rake) >= 13.1.0
Conflicts:     gem(rake) >= 14

%description   -n gem-minitest-fail-fast-devel
Fail and exit as soon as a test fails development package.

Reimplements RSpec's "fail fast" feature for minitest

%description   -n gem-minitest-fail-fast-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-fail-fast.
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
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-fail-fast-doc
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-fail-fast-devel
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%endif


%changelog
* Fri Aug 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- ^ 0.1.0 -> 0.2.0
- * define explicit dependencies

* Fri Sep 10 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
 - + packaged gem with Ruby Policy 2.0
