%define        gemname cane

Name:          gem-cane
Version:       3.0.0
Release:       alt1
Summary:       Fails your build if code quality thresholds are not met. Provides complexity and style checkers built-in, and allows integration with with custom quality metrics
License:       Apache 2.0
Group:         Development/Ruby
Url:           http://github.com/square/cane
Vcs:           https://github.com/square/cane.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(parallel) >= 0
BuildRequires: gem(rspec) >= 2.0 gem(rspec) < 4
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(simplecov) >= 0 gem(simplecov) < 1
BuildRequires: gem(rspec-fire) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_ignore_names example
Requires:      gem(parallel) >= 0
Provides:      gem(cane) = 3.0.0


%description
Fails your build if code quality thresholds are not met


%package       -n cane
Version:       3.0.0
Release:       alt1
Summary:       Fails your build if code quality thresholds are not met. Provides complexity and style checkers built-in, and allows integration with with custom quality metrics executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета cane
Group:         Other
BuildArch:     noarch

Requires:      gem(cane) = 3.0.0

%description   -n cane
Fails your build if code quality thresholds are not met. Provides complexity and
style checkers built-in, and allows integration with with custom quality metrics
executable(s).

Fails your build if code quality thresholds are not met

%description   -n cane -l ru_RU.UTF-8
Исполнямка для самоцвета cane.


%package       -n gem-cane-doc
Version:       3.0.0
Release:       alt1
Summary:       Fails your build if code quality thresholds are not met. Provides complexity and style checkers built-in, and allows integration with with custom quality metrics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cane
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cane) = 3.0.0

%description   -n gem-cane-doc
Fails your build if code quality thresholds are not met. Provides complexity and
style checkers built-in, and allows integration with with custom quality metrics
documentation files.

Fails your build if code quality thresholds are not met

%description   -n gem-cane-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cane.


%package       -n gem-cane-devel
Version:       3.0.0
Release:       alt1
Summary:       Fails your build if code quality thresholds are not met. Provides complexity and style checkers built-in, and allows integration with with custom quality metrics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cane
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cane) = 3.0.0
Requires:      gem(rspec) >= 2.0 gem(rspec) < 4
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(simplecov) >= 0 gem(simplecov) < 1
Requires:      gem(rspec-fire) >= 0

%description   -n gem-cane-devel
Fails your build if code quality thresholds are not met. Provides complexity and
style checkers built-in, and allows integration with with custom quality metrics
development package.

Fails your build if code quality thresholds are not met

%description   -n gem-cane-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cane.


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

%files         -n cane
%doc README.md
%_bindir/cane

%files         -n gem-cane-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-cane-devel
%doc README.md


%changelog
* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- + packaged gem with Ruby Policy 2.0
