%define        gemname fasterer

Name:          gem-fasterer
Version:       0.10.0
Release:       alt1
Summary:       Run Ruby more than fast. Fasterer
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/DamirSvrtan/fasterer
Vcs:           https://github.com/damirsvrtan/fasterer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.6
BuildRequires: gem(pry) >= 0.10
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rspec) >= 3.2
BuildRequires: gem(simplecov) >= 0.9
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(colorize) >= 0.7
BuildRequires: gem(ruby_parser) >= 3.19.1
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(colorize) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(colorize) >= 0.7
Requires:      gem(ruby_parser) >= 3.19.1
Conflicts:     gem(colorize) >= 1
Provides:      gem(fasterer) = 0.10.0


%description
Use Fasterer to check various places in your code that could be faster.


%package       -n fasterer
Version:       0.10.0
Release:       alt1
Summary:       Run Ruby more than fast. Fasterer executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета fasterer
Group:         Other
BuildArch:     noarch

Requires:      gem(fasterer) = 0.10.0

%description   -n fasterer
Run Ruby more than fast. Fasterer executable(s).

Use Fasterer to check various places in your code that could be faster.

%description   -n fasterer -l ru_RU.UTF-8
Исполнямка для самоцвета fasterer.


%package       -n gem-fasterer-doc
Version:       0.10.0
Release:       alt1
Summary:       Run Ruby more than fast. Fasterer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fasterer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fasterer) = 0.10.0

%description   -n gem-fasterer-doc
Run Ruby more than fast. Fasterer documentation files.

Use Fasterer to check various places in your code that could be faster.

%description   -n gem-fasterer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fasterer.


%package       -n gem-fasterer-devel
Version:       0.10.0
Release:       alt1
Summary:       Run Ruby more than fast. Fasterer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fasterer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fasterer) = 0.10.0
Requires:      gem(bundler) >= 1.6
Requires:      gem(pry) >= 0.10
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 3.2
Requires:      gem(simplecov) >= 0.9
Requires:      gem(codeclimate-test-reporter) >= 0
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1

%description   -n gem-fasterer-devel
Run Ruby more than fast. Fasterer development package.

Use Fasterer to check various places in your code that could be faster.

%description   -n gem-fasterer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fasterer.


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

%files         -n fasterer
%doc README.md
%_bindir/fasterer

%files         -n gem-fasterer-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fasterer-devel
%doc README.md


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with Ruby Policy 2.0
