%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname test-queue

Name:          gem-test-queue
Version:       0.11.1
Release:       alt1
Summary:       parallel test runner
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tmm1/test-queue
Vcs:           https://github.com/tmm1/test-queue.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 2.13
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Provides:      gem(test-queue) = 0.11.1


%description
minitest/rspec parallel test runner for CI environments


%package       -n test-queue
Version:       0.11.1
Release:       alt1
Summary:       parallel test runner executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета test-queue
Group:         Other
BuildArch:     noarch

Requires:      gem(test-queue) = 0.11.1

%description   -n test-queue
parallel test runner executable(s).

minitest/rspec parallel test runner for CI environments
%description   -n test-queue -l ru_RU.UTF-8
Исполнямка для самоцвета test-queue.


%if_enabled    doc
%package       -n gem-test-queue-doc
Version:       0.11.1
Release:       alt1
Summary:       parallel test runner documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test-queue
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test-queue) = 0.11.1

%description   -n gem-test-queue-doc
parallel test runner documentation files.

minitest/rspec parallel test runner for CI environments
%description   -n gem-test-queue-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test-queue.
%endif


%if_enabled    devel
%package       -n gem-test-queue-devel
Version:       0.11.1
Release:       alt1
Summary:       parallel test runner development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test-queue
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(test-queue) = 0.11.1
Requires:      gem(appraisal) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 2.13
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2

%description   -n gem-test-queue-devel
parallel test runner development package.

minitest/rspec parallel test runner for CI environments
%description   -n gem-test-queue-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета test-queue.
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

%files         -n test-queue
%doc README.md
%_bindir/rspec-queue
%_bindir/minitest-queue
%_bindir/testunit-queue
%_bindir/cucumber-queue

%if_enabled    doc
%files         -n gem-test-queue-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-test-queue-devel
%doc README.md
%endif


%changelog
* Thu Mar 14 2024 Pavel Skrylev <majioa@altlinux.org> 0.11.1-alt1
- + packaged gem with Ruby Policy 2.0
