# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname tty-table

Name:          gem-tty-table
Version:       0.12.0
Release:       alt1
Summary:       A flexible and intuitive table generator
License:       MIT
Group:         Development/Ruby
Url:           https://ttytoolkit.org/
Vcs:           https://github.com/piotrmurach/tty-table.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-benchmark) >= 0
BuildRequires: gem(yard) >= 0.9.12
BuildRequires: gem(coveralls) >= 0.8.22
BuildRequires: gem(simplecov) >= 0.16.1
BuildRequires: gem(yardstick) >= 0.9.9
BuildRequires: gem(benchmark-ips) >= 2.7.2
BuildRequires: gem(pastel) >= 0.8
BuildRequires: gem(strings) >= 0.2.0
BuildRequires: gem(tty-screen) >= 0.8
BuildConflicts: gem(yard) >= 0.10
BuildConflicts: gem(coveralls) >= 0.9
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(yardstick) >= 0.10
BuildConflicts: gem(benchmark-ips) >= 3
BuildConflicts: gem(pastel) >= 1
BuildConflicts: gem(strings) >= 0.3
BuildConflicts: gem(tty-screen) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency benchmark-ips >= 2.10.0,benchmark-ips < 3
Requires:      gem(pastel) >= 0.8
Requires:      gem(strings) >= 0.2.0
Requires:      gem(tty-screen) >= 0.8
Conflicts:     gem(pastel) >= 1
Conflicts:     gem(strings) >= 0.3
Conflicts:     gem(tty-screen) >= 1
Provides:      gem(tty-table) = 0.12.0


%description
A flexible and intuitive table generator.


%package       -n gem-tty-table-doc
Version:       0.12.0
Release:       alt1
Summary:       A flexible and intuitive table generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tty-table
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tty-table) = 0.12.0

%description   -n gem-tty-table-doc
A flexible and intuitive table generator documentation files.

%description   -n gem-tty-table-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tty-table.


%package       -n gem-tty-table-devel
Version:       0.12.0
Release:       alt1
Summary:       A flexible and intuitive table generator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tty-table
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tty-table) = 0.12.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rspec-benchmark) >= 0
Requires:      gem(yard) >= 0.9.12
Requires:      gem(coveralls) >= 0.8.22
Requires:      gem(simplecov) >= 0.16.1
Requires:      gem(yardstick) >= 0.9.9
Requires:      gem(benchmark-ips) >= 2.7.2
Conflicts:     gem(yard) >= 0.10
Conflicts:     gem(coveralls) >= 0.9
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(yardstick) >= 0.10
Conflicts:     gem(benchmark-ips) >= 3

%description   -n gem-tty-table-devel
A flexible and intuitive table generator development package.

%description   -n gem-tty-table-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tty-table.


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

%files         -n gem-tty-table-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-tty-table-devel
%doc README.md


%changelog
* Tue Feb 07 2023 Pavel Skrylev <majioa@altlinux.org> 0.12.0-alt1
- ^ 0.11.0.1 -> 0.12.0

* Tue Sep 8 2020 Pavel Skrylev <majioa@altlinux.org> 0.11.0.1-alt0.1
- + packaged gem with usage Ruby Policy 2.0
