%define        gemname rspec-core

Name:          gem-rspec-core
Version:       3.10.1
Release:       alt1
Summary:       RSpec runner and formatters
License:       MIT
Group:         Development/Ruby
Url:           http://relishapp.com/rspec/rspec-core
Vcs:           https://github.com/rspec/rspec-core.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec-support) >= 3.10.0 gem(rspec-support) < 3.11

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec-support) >= 3.10.0 gem(rspec-support) < 3.11
Obsoletes:     ruby-rspec-core < %EVR
Provides:      ruby-rspec-core = %EVR
Provides:      gem(rspec-core) = 3.10.1

%description
rspec-core provides the structure for writing executable examples of how your
code should behave, and an rspec command with tools to constrain which examples
get run and tailor the output.


%package       -n rspec
Version:       3.10.1
Release:       alt1
Summary:       rspec-core-3.10.1 executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rspec-core
Group:         Other
BuildArch:     noarch

Requires:      gem(rspec-core) = 3.10.1

%description   -n rspec
rspec-core-3.10.1 executable(s).

BDD for Ruby. RSpec runner and example groups.

%description   -n rspec -l ru_RU.UTF-8
Исполнямка для самоцвета rspec-core.


%package       -n gem-rspec-core-doc
Version:       3.10.1
Release:       alt1
Summary:       rspec-core-3.10.1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-core) = 3.10.1

%description   -n gem-rspec-core-doc
rspec-core-3.10.1 documentation files.

BDD for Ruby. RSpec runner and example groups.

%description   -n gem-rspec-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-core.


%package       -n gem-rspec-core-devel
Version:       3.10.1
Release:       alt1
Summary:       rspec-core-3.10.1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-core) = 3.10.1

%description   -n gem-rspec-core-devel
rspec-core-3.10.1 development package.

BDD for Ruby. RSpec runner and example groups.

%description   -n gem-rspec-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-core.


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

%files         -n rspec
%doc README.md
%_bindir/rspec

%files         -n gem-rspec-core-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-core-devel
%doc README.md


%changelog
* Wed May 12 2021 Pavel Skrylev <majioa@altlinux.org> 3.10.1-alt1
- ^ 3.8.0 -> 3.10.1

* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.0-alt2
- > Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt2.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt2
- Rebuild with mocha 1.5.0.

* Thu Jan 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Jun 01 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version
- Package rspec executable

* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- Initial build for ALT Linux
