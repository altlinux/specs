%define        gemname benchmark_driver

Name:          gem-benchmark-driver
Version:       0.15.17
Release:       alt1
Summary:       Fully-featured accurate benchmark driver for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/benchmark-driver/benchmark-driver
Vcs:           https://github.com/benchmark-driver/benchmark-driver.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rspec-retry) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names benchmark_driver,benchmark-driver
%ruby_ignore_names gnore-names=benchmark-driver
Provides:      gem(benchmark_driver) = 0.15.17


%description
Fully-featured accurate benchmark driver for Ruby


%package       -n benchmark-driver
Version:       0.15.17
Release:       alt1
Summary:       Fully-featured accurate benchmark driver for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета benchmark_driver
Group:         Other
BuildArch:     noarch

Requires:      gem(benchmark_driver) = 0.15.17

%description   -n benchmark-driver
Fully-featured accurate benchmark driver for Ruby executable(s).

%description   -n benchmark-driver -l ru_RU.UTF-8
Исполнямка для самоцвета benchmark_driver.


%package       -n gem-benchmark-driver-doc
Version:       0.15.17
Release:       alt1
Summary:       Fully-featured accurate benchmark driver for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета benchmark_driver
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(benchmark_driver) = 0.15.17

%description   -n gem-benchmark-driver-doc
Fully-featured accurate benchmark driver for Ruby documentation
files.

%description   -n gem-benchmark-driver-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета benchmark_driver.


%package       -n gem-benchmark-driver-devel
Version:       0.15.17
Release:       alt1
Summary:       Fully-featured accurate benchmark driver for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета benchmark_driver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(benchmark_driver) = 0.15.17
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rspec-retry) >= 0

%description   -n gem-benchmark-driver-devel
Fully-featured accurate benchmark driver for Ruby development
package.

%description   -n gem-benchmark-driver-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета benchmark_driver.


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

%files         -n benchmark-driver
%doc README.md
%_bindir/benchmark-driver

%files         -n gem-benchmark-driver-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-benchmark-driver-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.15.17-alt1
- + packaged gem with Ruby Policy 2.0
