%define        gemname rspec-fire

Name:          gem-rspec-fire
Version:       1.3.0
Release:       alt1
Summary:       More resilient test doubles for RSpec
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/xaviershay/rspec-fire
Vcs:           https://github.com/xaviershay/rspec-fire.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 2.11 gem(rspec) < 4
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(rspec) >= 2.11 gem(rspec) < 4
Provides:      gem(rspec-fire) = 1.3.0

%description
RSpec fire has been completely subsumed by the verifying doubles feature in
RSpec 3, which uses the same API. It's not just a port, the RSpec 3 ones are
strictly better.

Leaving this here for posterity, but patches will not be accepted and there
will be no further releases.


%package       -n gem-rspec-fire-doc
Version:       1.3.0
Release:       alt1
Summary:       More resilient test doubles for RSpec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-fire
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-fire) = 1.3.0

%description   -n gem-rspec-fire-doc
More resilient test doubles for RSpec documentation files.

RSpec fire has been completely subsumed by the verifying doubles feature in
RSpec 3, which uses the same API. It's not just a port, the RSpec 3 ones are
strictly better.

Leaving this here for posterity, but patches will not be accepted and there
will be no further releases.

%description   -n gem-rspec-fire-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-fire.


%package       -n gem-rspec-fire-devel
Version:       1.3.0
Release:       alt1
Summary:       More resilient test doubles for RSpec development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-fire
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-fire) = 1.3.0
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-rspec-fire-devel
More resilient test doubles for RSpec development package.

RSpec fire has been completely subsumed by the verifying doubles feature in
RSpec 3, which uses the same API. It's not just a port, the RSpec 3 ones are
strictly better.

Leaving this here for posterity, but patches will not be accepted and there
will be no further releases.

%description   -n gem-rspec-fire-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-fire.


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

%files         -n gem-rspec-fire-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-fire-devel
%doc README.md


%changelog
* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- + packaged gem with Ruby Policy 2.0
