%define        gemname rspec-memory

Name:          gem-rspec-memory
Version:       1.0.1
Release:       alt1
Summary:       RSpec helpers for checking memory allocations
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/rspec-memory
Vcs:           https://github.com/socketry/rspec-memory.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Provides:      gem(rspec-memory) = 1.0.1


%description
RSpec helpers for checking memory allocations.


%package       -n gem-rspec-memory-doc
Version:       1.0.1
Release:       alt1
Summary:       RSpec helpers for checking memory allocations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-memory
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-memory) = 1.0.1

%description   -n gem-rspec-memory-doc
RSpec helpers for checking memory allocations documentation files.

%description   -n gem-rspec-memory-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-memory.


%package       -n gem-rspec-memory-devel
Version:       1.0.1
Release:       alt1
Summary:       RSpec helpers for checking memory allocations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-memory
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-memory) = 1.0.1
Requires:      gem(covered) >= 0
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 10.0 gem(rake) < 14

%description   -n gem-rspec-memory-devel
RSpec helpers for checking memory allocations development package.

%description   -n gem-rspec-memory-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-memory.


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

%files         -n gem-rspec-memory-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-memory-devel
%doc README.md


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
