%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fasterer

Name:          gem-fasterer
Version:       0.11.0
Release:       alt1
Summary:       Run Ruby more than fast. Fasterer
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/DamirSvrtan/fasterer
Vcs:           https://github.com/damirsvrtan/fasterer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby rake setup-rb
%if_enabled check
BuildRequires: gem(bundler) >= 1.6
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(pry) >= 0.10
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rspec) >= 3.2
BuildRequires: gem(ruby_parser) >= 3.19.1
BuildRequires: gem(simplecov) >= 0.9
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.3
Requires:      gem(ruby_parser) >= 3.19.1
Provides:      gem(fasterer) = 0.11.0

%description
Use Fasterer to check various places in your code that could be faster.


%package       -n fasterer
Version:       0.11.0
Release:       alt1
Summary:       Run Ruby more than fast. Fasterer executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета fasterer
Group:         Other
BuildArch:     noarch

Requires:      gem(fasterer) = 0.11.0

%description   -n fasterer
Run Ruby more than fast. Fasterer executable(s).

Use Fasterer to check various places in your code that could be faster.

%description   -n fasterer -l ru_RU.UTF-8
Исполнямка для самоцвета fasterer.


%if_enabled    doc
%package       -n gem-fasterer-doc
Version:       0.11.0
Release:       alt1
Summary:       Run Ruby more than fast. Fasterer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fasterer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fasterer) = 0.11.0

%description   -n gem-fasterer-doc
Run Ruby more than fast. Fasterer documentation files.

Use Fasterer to check various places in your code that could be faster.

%description   -n gem-fasterer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fasterer.
%endif


%if_enabled    devel
%package       -n gem-fasterer-devel
Version:       0.11.0
Release:       alt1
Summary:       Run Ruby more than fast. Fasterer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fasterer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fasterer) = 0.11.0
Requires:      gem(bundler) >= 1.6
Requires:      gem(pry) >= 0.10
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 3.2
Requires:      gem(simplecov) >= 0.9
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1

%description   -n gem-fasterer-devel
Run Ruby more than fast. Fasterer development package.

Use Fasterer to check various places in your code that could be faster.

%description   -n gem-fasterer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fasterer.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n fasterer
%doc CHANGELOG.md LICENSE.txt README.md
%_bindir/fasterer

%if_enabled    doc
%files         -n gem-fasterer-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fasterer-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Thu May 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1
- ^ 0.10.0 -> 0.11.0

* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with Ruby Policy 2.0
