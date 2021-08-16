%define        gemname rspec

Name:          gem-rspec
Version:       3.10.0
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
BuildRequires: gem(rspec-core) >= 3.10.0 gem(rspec-core) < 3.11
BuildRequires: gem(rspec-expectations) >= 3.10.0 gem(rspec-expectations) < 3.11
BuildRequires: gem(rspec-mocks) >= 3.10.0 gem(rspec-mocks) < 3.11

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec-core) >= 3.10.0 gem(rspec-core) < 3.11
Requires:      gem(rspec-expectations) >= 3.10.0 gem(rspec-expectations) < 3.11
Requires:      gem(rspec-mocks) >= 3.10.0 gem(rspec-mocks) < 3.11
Obsoletes:     ruby-rspec < %EVR
Provides:      ruby-rspec = %EVR
Provides:      gem(rspec) = 3.10.0

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


%package       -n gem-rspec-doc
Version:       3.10.0
Release:       alt1
Summary:       rspec-3.10.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec) = 3.10.0

%description   -n gem-rspec-doc
rspec-3.10.0 documentation files.

BDD for Ruby

%description   -n gem-rspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec.


%package       -n gem-rspec-devel
Version:       3.10.0
Release:       alt1
Summary:       rspec-3.10.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec) = 3.10.0

%description   -n gem-rspec-devel
rspec-3.10.0 development package.

BDD for Ruby

%description   -n gem-rspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec.


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

%files         -n gem-rspec-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-devel
%doc README.md


%changelog
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
