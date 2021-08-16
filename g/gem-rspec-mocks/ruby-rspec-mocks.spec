%define        gemname rspec-mocks

Name:          gem-rspec-mocks
Version:       3.10.2
Release:       alt1
Summary:       RSpec's 'test double' framework, with support for stubbing and mocking
License:       MIT
Group:         Development/Ruby
Url:           http://relishapp.com/rspec/rspec-mocks
Vcs:           https://github.com/rspec/rspec-mocks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec-support) >= 3.10.0 gem(rspec-support) < 3.11
BuildRequires: gem(diff-lcs) >= 1.2.0 gem(diff-lcs) < 2.0
BuildRequires: gem(rake) > 10.0.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec-support) >= 3.10.0 gem(rspec-support) < 3.11
Requires:      gem(diff-lcs) >= 1.2.0 gem(diff-lcs) < 2.0
Obsoletes:     ruby-rspec-mocks < %EVR
Provides:      ruby-rspec-mocks = %EVR
Provides:      gem(rspec-mocks) = 3.10.2

%description
rspec-mocks is a test-double framework for rspec with support for method stubs,
fakes, and message expectations on generated test-doubles and real objects
alike.


%package       -n gem-rspec-mocks-doc
Version:       3.10.2
Release:       alt1
Summary:       rspec-mocks-3.10.2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-mocks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-mocks) = 3.10.2

%description   -n gem-rspec-mocks-doc
rspec-mocks-3.10.2 documentation files.

RSpec's 'test double' framework, with support for stubbing and mocking

%description   -n gem-rspec-mocks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-mocks.


%package       -n gem-rspec-mocks-devel
Version:       3.10.2
Release:       alt1
Summary:       rspec-mocks-3.10.2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-mocks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-mocks) = 3.10.2
Requires:      gem(rake) > 10.0.0

%description   -n gem-rspec-mocks-devel
rspec-mocks-3.10.2 development package.

RSpec's 'test double' framework, with support for stubbing and mocking

%description   -n gem-rspec-mocks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-mocks.


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

%files         -n gem-rspec-mocks-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-mocks-devel
%doc README.md


%changelog
* Wed May 12 2021 Pavel Skrylev <majioa@altlinux.org> 3.10.2-alt1
- ^ 3.8.0 -> 3.10.2

* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.0-alt2
- Use Ruby Policy 2.0.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Tue Aug 22 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version

* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- Initial build for ALT Linux
