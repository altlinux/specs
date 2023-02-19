# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname tty-screen

Name:          gem-tty-screen
Version:       0.8.1.10
Release:       alt0.1
Summary:       Terminal screen detection - cross platform, major ruby interpreters
License:       MIT
Group:         Development/Ruby
Url:           https://ttytoolkit.org
Vcs:           https://github.com/piotrmurach/tty-screen.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(coveralls_reborn) >= 0.22.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(yardstick) >= 0.9.9
BuildRequires: gem(rspec-benchmark) >= 0.6.0
BuildRequires: gem(io-console) >= 0
BuildConflicts: gem(coveralls_reborn) >= 0.23
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(yardstick) >= 0.10
BuildConflicts: gem(rspec-benchmark) >= 0.7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Provides:      gem(tty-screen) = 0.8.1.10

%ruby_use_gem_version tty-screen:0.8.1.10

%description
Terminal screen size detection which works on Linux, OS X and Windows/Cygwin
platforms and supports MRI, JRuby and Rubinius interpreters.

TTY::Screen provides independent terminal screen size detection component for
TTY toolkit.


%package       -n gem-tty-screen-doc
Version:       0.8.1.10
Release:       alt0.1
Summary:       Terminal screen detection - cross platform, major ruby interpreters documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tty-screen
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tty-screen) = 0.8.1.10

%description   -n gem-tty-screen-doc
Terminal screen detection - cross platform, major ruby interpreters
documentation files.

Terminal screen size detection which works on Linux, OS X and Windows/Cygwin
platforms and supports MRI, JRuby and Rubinius interpreters.

TTY::Screen provides independent terminal screen size detection component for
TTY toolkit.

%description   -n gem-tty-screen-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tty-screen.


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

%files         -n gem-tty-screen-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.1.10-alt0.1
- ^ 0.8.1 -> 0.8.1p10 (no devel)

* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.1-alt1
- ^ 0.7.0 -> 0.8.1
- ! spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- + packaged gem with usage Ruby Policy 2.0
