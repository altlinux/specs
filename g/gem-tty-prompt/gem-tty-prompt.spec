# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname tty-prompt

Name:          gem-tty-prompt
Version:       0.23.1
Release:       alt1
Summary:       A beautiful and powerful interactive command line prompt
License:       MIT
Group:         Development/Ruby
Url:           https://ttytoolkit.org/
Vcs:           https://github.com/piotrmurach/tty-prompt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(benchmark-ips) >= 2.7.2
BuildRequires: gem(coveralls_reborn) >= 0.21.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(pastel) >= 0.8
BuildRequires: gem(tty-reader) >= 0.8
BuildConflicts: gem(benchmark-ips) >= 3
BuildConflicts: gem(coveralls_reborn) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(pastel) >= 1
BuildConflicts: gem(tty-reader) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency benchmark-ips >= 2.10.0,benchmark-ips < 3
%ruby_use_gem_dependency coveralls_reborn >= 0.27,coveralls_reborn < 1
Requires:      gem(pastel) >= 0.8
Requires:      gem(tty-reader) >= 0.8
Conflicts:     gem(pastel) >= 1
Conflicts:     gem(tty-reader) >= 1
Provides:      gem(tty-prompt) = 0.23.1


%description
A beautiful and powerful interactive command line prompt.

TTY::Prompt provides independent prompt component for TTY toolkit.


%package       -n gem-tty-prompt-doc
Version:       0.23.1
Release:       alt1
Summary:       A beautiful and powerful interactive command line prompt documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tty-prompt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tty-prompt) = 0.23.1

%description   -n gem-tty-prompt-doc
A beautiful and powerful interactive command line prompt documentation files.

%description   -n gem-tty-prompt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tty-prompt.


%package       -n gem-tty-prompt-devel
Version:       0.23.1
Release:       alt1
Summary:       A beautiful and powerful interactive command line prompt development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tty-prompt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tty-prompt) = 0.23.1
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(benchmark-ips) >= 2.7.2
Requires:      gem(coveralls_reborn) >= 0.21.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(benchmark-ips) >= 3
Conflicts:     gem(coveralls_reborn) >= 1
Conflicts:     gem(simplecov) >= 1

%description   -n gem-tty-prompt-devel
A beautiful and powerful interactive command line prompt development package.

%description   -n gem-tty-prompt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tty-prompt.


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

%files         -n gem-tty-prompt-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-tty-prompt-devel
%doc README.md


%changelog
* Tue Feb 07 2023 Pavel Skrylev <majioa@altlinux.org> 0.23.1-alt1
- ^ 0.22.0.1 -> 0.23.1

* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 0.22.0.1-alt0.1
- ^ 0.19.0 -> 0.22.0.1
- ! spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.19.0-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 0.19.0-alt1
- + packaged gem with usage Ruby Policy 2.0
