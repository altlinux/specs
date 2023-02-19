%define        gemname spork

Name:          gem-spork
Version:       1.0.0
Release:       alt0.4
Summary:       A forking Drb spec server
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/sporkrb/spork
Vcs:           https://github.com/sporkrb/spork.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(spork) = 1.0.0

%ruby_use_gem_version spork:1.0.0

%description
A forking Drb spec server.

A DRb server for testing frameworks (RSpec / Cucumber currently) that forks
before each run to ensure a clean testing state.


%package       -n spork
Version:       1.0.0
Release:       alt0.4
Summary:       A forking Drb spec server executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета spork
Group:         Other
BuildArch:     noarch

Requires:      gem(spork) = 1.0.0

%description   -n spork
A forking Drb spec server executable(s).

A DRb server for testing frameworks (RSpec / Cucumber currently) that forks
before each run to ensure a clean testing state.

%description   -n spork -l ru_RU.UTF-8
Исполнямка для самоцвета spork.


%package       -n gem-spork-doc
Version:       1.0.0
Release:       alt0.4
Summary:       A forking Drb spec server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета spork
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(spork) = 1.0.0

%description   -n gem-spork-doc
A forking Drb spec server documentation files.

A DRb server for testing frameworks (RSpec / Cucumber currently) that forks
before each run to ensure a clean testing state.

%description   -n gem-spork-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета spork.


%package       -n gem-spork-devel
Version:       1.0.0
Release:       alt0.4
Summary:       A forking Drb spec server development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета spork
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(spork) = 1.0.0

%description   -n gem-spork-devel
A forking Drb spec server development package.

A DRb server for testing frameworks (RSpec / Cucumber currently) that forks
before each run to ensure a clean testing state.

%description   -n gem-spork-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета spork.


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

%files         -n spork
%doc README.rdoc
%_bindir/spork

%files         -n gem-spork-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-spork-devel
%doc README.rdoc


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt0.4
- + packaged gem with Ruby Policy 2.0 with version 1.0.0rc4
