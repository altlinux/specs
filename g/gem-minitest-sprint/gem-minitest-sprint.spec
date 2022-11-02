%define        gemname minitest-sprint

Name:          gem-minitest-sprint
Version:       1.2.2
Release:       alt1
Summary:       Runs (Get it? It's fast!) your tests and makes it easier to rerun individual failures
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-sprint
Vcs:           https://github.com/seattlerb/minitest-sprint.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(path_expander) >= 1.1 gem(path_expander) < 2
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.23 gem(hoe) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(path_expander) >= 1.1 gem(path_expander) < 2
Provides:      gem(minitest-sprint) = 1.2.2


%description
Runs (Get it? It's fast!) your tests and makes it easier to rerun individual
failures.


%package       -n minitest
Version:       1.2.2
Release:       alt1
Summary:       Runs (Get it? It's fast!) your tests and makes it easier to rerun individual failures executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета minitest-sprint
Group:         Other
BuildArch:     noarch

Requires:      gem(minitest-sprint) = 1.2.2

%description   -n minitest
Runs (Get it? It's fast!) your tests and makes it easier to rerun individual
failures executable(s).

%description   -n minitest -l ru_RU.UTF-8
Исполнямка для самоцвета minitest-sprint.


%package       -n gem-minitest-sprint-doc
Version:       1.2.2
Release:       alt1
Summary:       Runs (Get it? It's fast!) your tests and makes it easier to rerun individual failures documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-sprint
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-sprint) = 1.2.2

%description   -n gem-minitest-sprint-doc
Runs (Get it? It's fast!) your tests and makes it easier to rerun individual
failures documentation files.

%description   -n gem-minitest-sprint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-sprint.


%package       -n gem-minitest-sprint-devel
Version:       1.2.2
Release:       alt1
Summary:       Runs (Get it? It's fast!) your tests and makes it easier to rerun individual failures development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-sprint
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-sprint) = 1.2.2
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.23 gem(hoe) < 4

%description   -n gem-minitest-sprint-devel
Runs (Get it? It's fast!) your tests and makes it easier to rerun individual
failures development package.

%description   -n gem-minitest-sprint-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-sprint.


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

%files         -n minitest
%doc README.rdoc
%_bindir/minitest

%files         -n gem-minitest-sprint-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-minitest-sprint-devel
%doc README.rdoc


%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1
- + packaged gem with Ruby Policy 2.0
