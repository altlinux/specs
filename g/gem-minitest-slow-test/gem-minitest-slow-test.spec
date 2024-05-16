%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-slow_test

Name:          gem-minitest-slow-test
Version:       0.2.0
Release:       alt1
Summary:       Display the summary of a slow test when tests finished
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/y-yagi/minitest-slow_test
Vcs:           https://github.com/y-yagi/minitest-slow_test.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.6
BuildRequires: gem(rake) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildConflicts: gem(bundler) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      gem(minitest) >= 5.0
Provides:      gem(minitest-slow_test) = 0.2.0


%description
Display the summary of a slow test when tests finished.


%if_enabled    doc
%package       -n gem-minitest-slow-test-doc
Version:       0.2.0
Release:       alt1
Summary:       Display the summary of a slow test when tests finished documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-slow_test
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-slow_test) = 0.2.0

%description   -n gem-minitest-slow-test-doc
Display the summary of a slow test when tests finished documentation files.
%description   -n gem-minitest-slow-test-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-slow_test.
%endif


%if_enabled    devel
%package       -n gem-minitest-slow-test-devel
Version:       0.2.0
Release:       alt1
Summary:       Display the summary of a slow test when tests finished development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-slow_test
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-slow_test) = 0.2.0
Requires:      gem(bundler) >= 1.6
Requires:      gem(rake) >= 0
Requires:      gem(pry) >= 0
Conflicts:     gem(bundler) >= 3

%description   -n gem-minitest-slow-test-devel
Display the summary of a slow test when tests finished development package.
%description   -n gem-minitest-slow-test-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-slow_test.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-slow-test-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-slow-test-devel
%doc README.md
%endif


%changelog
* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
