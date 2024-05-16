%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rspec

Name:          gem-rspec
Version:       3.13.0
Release:       alt1
Summary:       RSpec meta-gem that depends on the other components
License:       MIT
Group:         Development/Ruby
Url:           http://rspec.info/
Vcs:           https://github.com/rspec/rspec.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec-core) >= 3.10.1
BuildRequires: gem(rspec-expectations) >= 3.10.1
BuildRequires: gem(rspec-mocks) >= 3.10.2
BuildConflicts: gem(rspec-core) >= 4
BuildConflicts: gem(rspec-expectations) >= 4
BuildConflicts: gem(rspec-mocks) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec-core >= 3.10.1,rspec-core < 4
%ruby_use_gem_dependency rspec-expectations >= 3.10.1,rspec-expectations < 4
%ruby_use_gem_dependency rspec-mocks >= 3.10.2,rspec-mocks < 4
Requires:      gem(rspec-core) >= 3.10.1
Requires:      gem(rspec-expectations) >= 3.10.1
Requires:      gem(rspec-mocks) >= 3.10.2
Conflicts:     gem(rspec-core) >= 4
Conflicts:     gem(rspec-expectations) >= 4
Conflicts:     gem(rspec-mocks) >= 4
Obsoletes:     ruby-rspec < %EVR
Provides:      ruby-rspec = %EVR
Provides:      gem(rspec) = 3.13.0


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


%if_enabled    doc
%package       -n gem-rspec-doc
Version:       3.13.0
Release:       alt1
Summary:       RSpec meta-gem that depends on the other components documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec) = 3.13.0

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
Version:       3.13.0
Release:       alt1
Summary:       RSpec meta-gem that depends on the other components development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec) = 3.13.0
Requires:      gem(rake) >= 0

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rspec-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-devel
%doc README.md
%endif


%changelog
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
