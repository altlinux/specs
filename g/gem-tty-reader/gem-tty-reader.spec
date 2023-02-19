# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname tty-reader

Name:          gem-tty-reader
Version:       0.9.0
Release:       alt1
Summary:       A set of methods for processing keyboard input in character, line and multiline modes
License:       MIT
Group:         Development/Ruby
Url:           https://ttytoolkit.org/
Vcs:           https://github.com/piotrmurach/tty-reader.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(benchmark-ips) >= 2.7.2
BuildRequires: gem(simplecov) >= 0.16.1
BuildRequires: gem(coveralls) >= 0.8.22
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yardstick) >= 0.9.9
BuildRequires: gem(tty-screen) >= 0.8
BuildRequires: gem(tty-cursor) >= 0.7
BuildRequires: gem(wisper) >= 2.0
BuildConflicts: gem(benchmark-ips) >= 2.8
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(coveralls) >= 0.9
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(yardstick) >= 0.10
BuildConflicts: gem(tty-screen) >= 1
BuildConflicts: gem(tty-cursor) >= 1
BuildConflicts: gem(wisper) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(tty-screen) >= 0.8
Requires:      gem(tty-cursor) >= 0.7
Requires:      gem(wisper) >= 2.0
Conflicts:     gem(tty-screen) >= 1
Conflicts:     gem(tty-cursor) >= 1
Conflicts:     gem(wisper) >= 3
Provides:      gem(tty-reader) = 0.9.0


%description
A set of methods for processing keyboard input in character, line and multiline
modes.

TTY::Reader provides independent reader component for TTY toolkit.


%package       -n gem-tty-reader-doc
Version:       0.9.0
Release:       alt1
Summary:       A set of methods for processing keyboard input in character, line and multiline modes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tty-reader
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tty-reader) = 0.9.0

%description   -n gem-tty-reader-doc
A set of methods for processing keyboard input in character, line and multiline
modes documentation files.

%description   -n gem-tty-reader-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tty-reader.


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

%files         -n gem-tty-reader-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- ^ 0.8.0 -> 0.9.0 (no devel)

* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- ^ 0.6.0 -> 0.8.0
- ! spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with usage Ruby Policy 2.0
