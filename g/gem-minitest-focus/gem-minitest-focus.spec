%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-focus

Name:          gem-minitest-focus
Version:       1.3.1.4
Release:       alt0.1
Summary:       Allows you to focus on a few tests with ease without having to use command-line arguments
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-focus
Vcs:           https://github.com/seattlerb/minitest-focus.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 4
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 4.2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(hoe) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) >= 4
Conflicts:     gem(minitest) >= 6
Provides:      gem(minitest-focus) = 1.3.1.4

%ruby_use_gem_version minitest-focus:1.3.1.4

%description
Allows you to focus on a few tests with ease without having to use command-line
arguments. Good for tools like guard that don't have enough brains to understand
test output. Cf. ZenTest's autotest (an example of a test runner with strong
testing logic).

Inspired by https://github.com/seattlerb/minitest/issues/213


%if_enabled    doc
%package       -n gem-minitest-focus-doc
Version:       1.3.1.4
Release:       alt0.1
Summary:       Allows you to focus on a few tests with ease without having to use command-line arguments documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-focus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-focus) = 1.3.1.4

%description   -n gem-minitest-focus-doc
Allows you to focus on a few tests with ease without having to use command-line
arguments documentation files.

Allows you to focus on a few tests with ease without having to use command-line
arguments. Good for tools like guard that don't have enough brains to understand
test output. Cf. ZenTest's autotest (an example of a test runner with strong
testing logic).

Inspired by https://github.com/seattlerb/minitest/issues/213

%description   -n gem-minitest-focus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-focus.
%endif


%if_enabled    devel
%package       -n gem-minitest-focus-devel
Version:       1.3.1.4
Release:       alt0.1
Summary:       Allows you to focus on a few tests with ease without having to use command-line arguments development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-focus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-focus) = 1.3.1.4
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 4.2
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

%description   -n gem-minitest-focus-devel
Allows you to focus on a few tests with ease without having to use command-line
arguments development package.

Allows you to focus on a few tests with ease without having to use command-line
arguments. Good for tools like guard that don't have enough brains to understand
test output. Cf. ZenTest's autotest (an example of a test runner with strong
testing logic).

Inspired by https://github.com/seattlerb/minitest/issues/213

%description   -n gem-minitest-focus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-focus.
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

%if_enabled    doc
%files         -n gem-minitest-focus-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-focus-devel
%doc README.rdoc
%endif


%changelog
* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.1.4-alt0.1
- ^ 1.3.1 -> 1.3.1.4

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- + packaged gem with Ruby Policy 2.0
