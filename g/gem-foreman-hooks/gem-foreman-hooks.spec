%define        gemname foreman_hooks

Name:          gem-foreman-hooks
Version:       0.3.17
Release:       alt1
Summary:       Run custom hook scripts on Foreman events
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_hooks
Vcs:           https://github.com/theforeman/foreman_hooks.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(foreman_hooks) = 0.3.17

%ruby_alias_names foreman_hooks,foreman-hooks

%description
Plugin engine for Foreman that enables running custom hook scripts on Foreman
events


%package       -n gem-foreman-hooks-doc
Version:       0.3.17
Release:       alt1
Summary:       Run custom hook scripts on Foreman events documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_hooks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_hooks) = 0.3.17

%description   -n gem-foreman-hooks-doc
Run custom hook scripts on Foreman events documentation files.

Plugin engine for Foreman that enables running custom hook scripts on Foreman
events

%description   -n gem-foreman-hooks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_hooks.


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

%files         -n gem-foreman-hooks-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.17-alt1
- + packaged gem with Ruby Policy 2.0
