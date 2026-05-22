%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname rspec

Name:          gem-rspec
Version:       3.13.2
Release:       alt1
Summary:       RSpec meta-gem that depends on the other components
License:       MIT
Group:         Development/Ruby
Url:           http://rspec.info/
Vcs:           https://github.com/rspec/rspec.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(aruba) >= 1.1.0
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(childprocess) >= 3.0.0
BuildRequires: gem(coderay) >= 0
BuildRequires: gem(cucumber) >= 1.3
BuildRequires: gem(diff-lcs) >= 1.4.3
BuildRequires: gem(drb) >= 0
BuildRequires: gem(ffi) >= 1.17.0
BuildRequires: gem(flexmock) >= 0.9.0
BuildRequires: gem(minitest) >= 5.15
BuildRequires: gem(mocha) >= 0.13.0
BuildRequires: gem(rake) >= 10.0.0
BuildRequires: gem(rr) >= 1.0.4
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(test-unit) >= 3.0
BuildRequires: gem(thor) > 1.0.0
BuildRequires: gem(thread_order) >= 1.1.0
BuildConflicts: gem(aruba) >= 3.0.0
BuildConflicts: gem(diff-lcs) >= 3
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(flexmock) >= 0.10
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(rr) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(thread_order) >= 1.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency diff-lcs >= 2.0.0,diff-lcs < 3
Requires:      gem(rspec-core) = 3.13.6
Requires:      gem(rspec-expectations) = 3.13.5
Requires:      gem(rspec-mocks) = 3.13.8
Requires:      gem(rspec-support) = 3.13.7
Obsoletes:     ruby-rspec < %EVR
Provides:      ruby-rspec = %EVR
Provides:      gem(rspec) = 3.13.2

%ruby_ignore_names gem-rspec

%description
rspec is a meta-gem, which depends on the rspec-core, rspec-expectations and
rspec-mocks gems. Each of these can be installed separately and loaded in
isolation using require. Among other benefits, this allows you to use
rspec-expectations, for example, in Test::Unit::TestCase if you happen to prefer
that style.

Conversely, if you like RSpec's approach to declaring example groups and
examples (describe and it) but prefer Test::Unit assertions and mocha, rr or
flexmock for mocking, you'll be able to do that without having to install or
load the components of RSpec that you're not using.


%package       -n gem-rspec-core
Version:       3.13.6
Release:       alt1
Summary:       rspec-core-3.13.6
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 1.8.7
Requires:      gem(rspec-support) >= 3.13.0
Conflicts:     gem(rspec-support) >= 3.14
Provides:      gem(rspec-core) = 3.13.6

%description   -n gem-rspec-core
BDD for Ruby. RSpec runner and example groups.


%package       -n rspec
Version:       3.13.6
Release:       alt1
Summary:       rspec-core-3.13.6 executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rspec-core
Group:         Other
BuildArch:     noarch

Requires:      gem(rspec-core) = 3.13.6

%description   -n rspec
rspec-core-3.13.6 executable(s).

BDD for Ruby. RSpec runner and example groups.

%description   -n rspec -l ru_RU.UTF-8
Исполнямка для самоцвета rspec-core.


%if_enabled    doc
%package       -n gem-rspec-core-doc
Version:       3.13.6
Release:       alt1
Summary:       rspec-core-3.13.6 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-core) = 3.13.6
Obsoletes:     gem-rspec-doc < %EVR
Provides:      gem-rspec-doc = %EVR

%description   -n gem-rspec-core-doc
rspec-core-3.13.6 documentation files.

BDD for Ruby. RSpec runner and example groups.

%description   -n gem-rspec-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-core.
%endif


%if_enabled    devel
%package       -n gem-rspec-core-devel
Version:       3.13.6
Release:       alt1
Summary:       rspec-core-3.13.6 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-core) = 3.13.6
Obsoletes:     gem-rspec-devel < %EVR
Provides:      gem-rspec-devel = %EVR

%description   -n gem-rspec-core-devel
rspec-core-3.13.6 development package.

BDD for Ruby. RSpec runner and example groups.

%description   -n gem-rspec-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-core.
%endif


%package       -n gem-rspec-mocks
Version:       3.13.8
Release:       alt1
Summary:       rspec-mocks-3.13.8
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 1.8.7
Requires:      gem(diff-lcs) >= 1.2.0
Requires:      gem(rspec-support) >= 3.13.0
Conflicts:     gem(diff-lcs) >= 3
Conflicts:     gem(rspec-support) >= 3.14
Provides:      gem(rspec-mocks) = 3.13.8

%description   -n gem-rspec-mocks
RSpec's 'test double' framework, with support for stubbing and mocking


%if_enabled    doc
%package       -n gem-rspec-mocks-doc
Version:       3.13.8
Release:       alt1
Summary:       rspec-mocks-3.13.8 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-mocks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-mocks) = 3.13.8

%description   -n gem-rspec-mocks-doc
rspec-mocks-3.13.8 documentation files.

RSpec's 'test double' framework, with support for stubbing and mocking

%description   -n gem-rspec-mocks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-mocks.
%endif


%if_enabled    devel
%package       -n gem-rspec-mocks-devel
Version:       3.13.8
Release:       alt1
Summary:       rspec-mocks-3.13.8 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-mocks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-mocks) = 3.13.8

%description   -n gem-rspec-mocks-devel
rspec-mocks-3.13.8 development package.

RSpec's 'test double' framework, with support for stubbing and mocking

%description   -n gem-rspec-mocks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-mocks.
%endif


%package       -n gem-rspec-support
Version:       3.13.7
Release:       alt1
Summary:       rspec-support-3.13.7
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 1.8.7
Provides:      gem(rspec-support) = 3.13.7

%description   -n gem-rspec-support
Support utilities for RSpec gems


%if_enabled    doc
%package       -n gem-rspec-support-doc
Version:       3.13.7
Release:       alt1
Summary:       rspec-support-3.13.7 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-support
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-support) = 3.13.7

%description   -n gem-rspec-support-doc
rspec-support-3.13.7 documentation files.

Support utilities for RSpec gems

%description   -n gem-rspec-support-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-support.
%endif


%if_enabled    devel
%package       -n gem-rspec-support-devel
Version:       3.13.7
Release:       alt1
Summary:       rspec-support-3.13.7 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-support
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-support) = 3.13.7
Requires:      gem(rake) > 10.0.0
Requires:      gem(thread_order) >= 1.1.0
Conflicts:     gem(thread_order) >= 1.2

%description   -n gem-rspec-support-devel
rspec-support-3.13.7 development package.

Support utilities for RSpec gems

%description   -n gem-rspec-support-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-support.
%endif


%package       -n gem-rspec-expectations
Version:       3.13.5
Release:       alt1
Summary:       rspec-expectations-3.13.5
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 1.8.7
Requires:      gem(diff-lcs) >= 1.2.0
Requires:      gem(rspec-support) >= 3.13.0
Conflicts:     gem(diff-lcs) >= 3
Conflicts:     gem(rspec-support) >= 3.14
Provides:      gem(rspec-expectations) = 3.13.5

%description   -n gem-rspec-expectations
rspec-expectations provides a simple, readable API to express expected outcomes
of a code example.


%if_enabled    doc
%package       -n gem-rspec-expectations-doc
Version:       3.13.5
Release:       alt1
Summary:       rspec-expectations-3.13.5 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-expectations
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-expectations) = 3.13.5

%description   -n gem-rspec-expectations-doc
rspec-expectations-3.13.5 documentation files.

rspec-expectations provides a simple, readable API to express expected outcomes
of a code example.

%description   -n gem-rspec-expectations-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-expectations.
%endif


%if_enabled    devel
%package       -n gem-rspec-expectations-devel
Version:       3.13.5
Release:       alt1
Summary:       rspec-expectations-3.13.5 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-expectations
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-expectations) = 3.13.5

%description   -n gem-rspec-expectations-devel
rspec-expectations-3.13.5 development package.

rspec-expectations provides a simple, readable API to express expected outcomes
of a code example.

%description   -n gem-rspec-expectations-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-expectations.
%endif


%if_enabled    doc
%package       -n gem-rspec-doc
Version:       3.13.2
Release:       alt1
Summary:       RSpec meta-gem that depends on the other components documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec) = 3.13.2

%description   -n gem-rspec-doc
RSpec meta-gem that depends on the other components documentation files.

rspec is a meta-gem, which depends on the rspec-core, rspec-expectations and
rspec-mocks gems. Each of these can be installed separately and loaded in
isolation using require. Among other benefits, this allows you to use
rspec-expectations, for example, in Test::Unit::TestCase if you happen to prefer
that style.

Conversely, if you like RSpec's approach to declaring example groups and
examples (describe and it) but prefer Test::Unit assertions and mocha, rr or
flexmock for mocking, you'll be able to do that without having to install or
load the components of RSpec that you're not using.

%description   -n gem-rspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec.
%endif


%if_enabled    devel
%package       -n gem-rspec-devel
Version:       3.13.2
Release:       alt1
Summary:       RSpec meta-gem that depends on the other components development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec) = 3.13.2

%description   -n gem-rspec-devel
RSpec meta-gem that depends on the other components development package.

rspec is a meta-gem, which depends on the rspec-core, rspec-expectations and
rspec-mocks gems. Each of these can be installed separately and loaded in
isolation using require. Among other benefits, this allows you to use
rspec-expectations, for example, in Test::Unit::TestCase if you happen to prefer
that style.

Conversely, if you like RSpec's approach to declaring example groups and
examples (describe and it) but prefer Test::Unit assertions and mocha, rr or
flexmock for mocking, you'll be able to do that without having to install or
load the components of RSpec that you're not using.

%description   -n gem-rspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec.
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
%doc rspec/LICENSE.md rspec/README.md rspec/code_of_conduct.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rspec-core
%doc rspec-core/Changelog.md rspec-core/LICENSE.md rspec-core/README.md rspec-core/CODE_OF_CONDUCT.md rspec-core/CONTRIBUTING.md rspec-core/DEV-README.md
%ruby_gemspecdir/rspec-core-3.13.6.gemspec
%ruby_gemslibdir/rspec-core-3.13.6

%files         -n rspec
%doc rspec-core/Changelog.md rspec-core/LICENSE.md rspec-core/README.md rspec-core/CODE_OF_CONDUCT.md rspec-core/CONTRIBUTING.md rspec-core/DEV-README.md
%_bindir/rspec

%if_enabled    doc
%files         -n gem-rspec-core-doc
%doc rspec-core/Changelog.md rspec-core/LICENSE.md rspec-core/README.md rspec-core/CODE_OF_CONDUCT.md rspec-core/CONTRIBUTING.md rspec-core/DEV-README.md
%ruby_gemsdocdir/rspec-core-3.13.6
%endif

%if_enabled    devel
%files         -n gem-rspec-core-devel
%doc rspec-core/Changelog.md rspec-core/LICENSE.md rspec-core/README.md rspec-core/CODE_OF_CONDUCT.md rspec-core/CONTRIBUTING.md rspec-core/DEV-README.md
%endif

%files         -n gem-rspec-mocks
%doc rspec-mocks/Changelog.md rspec-mocks/LICENSE.md rspec-mocks/README.md rspec-mocks/CODE_OF_CONDUCT.md rspec-mocks/CONTRIBUTING.md rspec-mocks/DEV-README.md
%ruby_gemspecdir/rspec-mocks-3.13.8.gemspec
%ruby_gemslibdir/rspec-mocks-3.13.8

%if_enabled    doc
%files         -n gem-rspec-mocks-doc
%doc rspec-mocks/Changelog.md rspec-mocks/LICENSE.md rspec-mocks/README.md rspec-mocks/CODE_OF_CONDUCT.md rspec-mocks/CONTRIBUTING.md rspec-mocks/DEV-README.md
%ruby_gemsdocdir/rspec-mocks-3.13.8
%endif

%if_enabled    devel
%files         -n gem-rspec-mocks-devel
%doc rspec-mocks/Changelog.md rspec-mocks/LICENSE.md rspec-mocks/README.md rspec-mocks/CODE_OF_CONDUCT.md rspec-mocks/CONTRIBUTING.md rspec-mocks/DEV-README.md
%endif

%files         -n gem-rspec-support
%doc rspec-support/Changelog.md rspec-support/LICENSE.md rspec-support/README.md rspec-support/CODE_OF_CONDUCT.md rspec-support/CONTRIBUTING.md
%ruby_gemspecdir/rspec-support-3.13.7.gemspec
%ruby_gemslibdir/rspec-support-3.13.7

%if_enabled    doc
%files         -n gem-rspec-support-doc
%doc rspec-support/Changelog.md rspec-support/LICENSE.md rspec-support/README.md rspec-support/CODE_OF_CONDUCT.md rspec-support/CONTRIBUTING.md
%ruby_gemsdocdir/rspec-support-3.13.7
%endif

%if_enabled    devel
%files         -n gem-rspec-support-devel
%doc rspec-support/Changelog.md rspec-support/LICENSE.md rspec-support/README.md rspec-support/CODE_OF_CONDUCT.md rspec-support/CONTRIBUTING.md
%endif

%files         -n gem-rspec-expectations
%doc rspec-expectations/Changelog.md rspec-expectations/LICENSE.md rspec-expectations/README.md rspec-expectations/CODE_OF_CONDUCT.md rspec-expectations/CONTRIBUTING.md rspec-expectations/DEV-README.md
%ruby_gemspecdir/rspec-expectations-3.13.5.gemspec
%ruby_gemslibdir/rspec-expectations-3.13.5

%if_enabled    doc
%files         -n gem-rspec-expectations-doc
%doc rspec-expectations/Changelog.md rspec-expectations/LICENSE.md rspec-expectations/README.md rspec-expectations/CODE_OF_CONDUCT.md rspec-expectations/CONTRIBUTING.md rspec-expectations/DEV-README.md
%ruby_gemsdocdir/rspec-expectations-3.13.5
%endif

%if_enabled    devel
%files         -n gem-rspec-expectations-devel
%doc rspec-expectations/Changelog.md rspec-expectations/LICENSE.md rspec-expectations/README.md rspec-expectations/CODE_OF_CONDUCT.md rspec-expectations/CONTRIBUTING.md rspec-expectations/DEV-README.md
%endif

%if_enabled    doc
%files         -n gem-rspec-doc
%doc rspec/LICENSE.md rspec/README.md rspec/code_of_conduct.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-devel
%doc rspec/LICENSE.md rspec/README.md rspec/code_of_conduct.md
%endif


%changelog
* Fri May 22 2026 Pavel Skrylev <majioa@altlinux.org> 3.13.2-alt1
- ^ 3.13.0 -> 3.13.2
- * since upstreaam now contain all the rspec gem in the single repo just use
    them, and remove other rspec separated ones

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- ^ 3.10.0 -> 3.13.0

* Wed May 12 2021 Pavel Skrylev <majioa@altlinux.org> 3.10.0-alt1
- ^ 3.8.0 -> 3.10.0

* Tue Feb 26 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.0-alt3
- Use Ruby Policy 2.0.

* Thu Jan 10 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.0-alt2
- Place library into proper ruby gem folder.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus
