%define        gemname journald-logger

Name:          gem-journald-logger
Version:       3.1.0
Release:       alt1
Summary:       systemd-journal native logger
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sandfoxme/journald-logger
Vcs:           https://github.com/sandfoxme/journald-logger.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rufo) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(journald-native) >= 1.0
BuildConflicts: gem(journald-native) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(journald-native) >= 1.0
Conflicts:     gem(journald-native) >= 2
Provides:      gem(journald-logger) = 3.1.0


%description
A Logger drop-in replacement that logs directly to systemd-journal with some
additional features.


%package       -n gem-journald-logger-doc
Version:       3.1.0
Release:       alt1
Summary:       systemd-journal native logger documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета journald-logger
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(journald-logger) = 3.1.0

%description   -n gem-journald-logger-doc
systemd-journal native logger documentation files.

A Logger drop-in replacement that logs directly to systemd-journal with some
additional features.

%description   -n gem-journald-logger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета journald-logger.


%package       -n gem-journald-logger-devel
Version:       3.1.0
Release:       alt1
Summary:       systemd-journal native logger development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета journald-logger
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(journald-logger) = 3.1.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rufo) >= 0
Requires:      gem(simplecov) >= 0

%description   -n gem-journald-logger-devel
systemd-journal native logger development package.

A Logger drop-in replacement that logs directly to systemd-journal with some
additional features.

%description   -n gem-journald-logger-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета journald-logger.


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

%files         -n gem-journald-logger-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-journald-logger-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 3.0.1 -> 3.1.0

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- ^ 2.0.4 -> 3.0.1

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.4-alt1.1
- ! spec according to changelog rules

* Wed Aug 21 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.4-alt1
- + packaged gem with usage Ruby Policy 2.0
