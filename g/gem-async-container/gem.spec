%define        gemname async-container

Name:          gem-async-container
Version:       0.16.12
Release:       alt1
Summary:       Abstract container-based parallelism using threads and processes where appropriate
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-container
Vcs:           https://github.com/socketry/async-container.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(async) >= 0
BuildRequires: gem(async-io) >= 0
BuildRequires: gem(async-rspec) >= 1.1 gem(async-rspec) < 2
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async) >= 0
Requires:      gem(async-io) >= 0
Provides:      gem(async-container) = 0.16.12


%description
Abstract container-based parallelism using threads and processes where
appropriate.


%package       -n gem-async-container-doc
Version:       0.16.12
Release:       alt1
Summary:       Abstract container-based parallelism using threads and processes where appropriate documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-container
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-container) = 0.16.12

%description   -n gem-async-container-doc
Abstract container-based parallelism using threads and processes where
appropriate documentation files.

%description   -n gem-async-container-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-container.


%package       -n gem-async-container-devel
Version:       0.16.12
Release:       alt1
Summary:       Abstract container-based parallelism using threads and processes where appropriate development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-container
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-container) = 0.16.12
Requires:      gem(async-rspec) >= 1.1 gem(async-rspec) < 2
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4

%description   -n gem-async-container-devel
Abstract container-based parallelism using threads and processes where
appropriate development package.

%description   -n gem-async-container-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-container.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-async-container-doc
%ruby_gemdocdir

%files         -n gem-async-container-devel


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.16.12-alt1
- + packaged gem with Ruby Policy 2.0
