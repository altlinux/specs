%define        gemname rspec-expectations

Name:          gem-rspec-expectations
Version:       3.10.1
Release:       alt1
Summary:       Provides a readable API to express expected outcomes of a code example
License:       MIT
Group:         Development/Ruby
Url:           http://relishapp.com/rspec/rspec-expectations
Vcs:           https://github.com/rspec/rspec-expectations.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec-support) >= 3.10.0 gem(rspec-support) < 3.11

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec-support) >= 3.10.0 gem(rspec-support) < 3.11
Requires:      gem(diff-lcs) >= 1.2.0 gem(diff-lcs) < 2.0
Obsoletes:     ruby-rspec-expectations < %EVR
Provides:      ruby-rspec-expectations = %EVR
Provides:      gem(rspec-expectations) = 3.10.1

%description
RSpec::Expectations lets you express expected outcomes on an object in an
example.


%package       -n gem-rspec-expectations-doc
Version:       3.10.1
Release:       alt1
Summary:       rspec-expectations-3.10.1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-expectations
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-expectations) = 3.10.1

%description   -n gem-rspec-expectations-doc
rspec-expectations-3.10.1 documentation files.

rspec-expectations provides a simple, readable API to express expected outcomes
of a code example.

%description   -n gem-rspec-expectations-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-expectations.


%package       -n gem-rspec-expectations-devel
Version:       3.10.1
Release:       alt1
Summary:       rspec-expectations-3.10.1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-expectations
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-expectations) = 3.10.1

%description   -n gem-rspec-expectations-devel
rspec-expectations-3.10.1 development package.

rspec-expectations provides a simple, readable API to express expected outcomes
of a code example.

%description   -n gem-rspec-expectations-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-expectations.


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

%files         -n gem-rspec-expectations-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-expectations-devel
%doc README.md


%changelog
* Wed May 12 2021 Pavel Skrylev <majioa@altlinux.org> 3.10.1-alt1
- ^ 3.8.2 -> 3.10.1

* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.2-alt2
- Use Ruby Policy 2.0.

* Wed Oct 10 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.2-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Tue Aug 22 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version

* Sat Dec 26 2015 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- Initial build for ALT Linux
