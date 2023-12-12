%define        _unpackaged_files_terminate_build 1
%define        gemname session

Name:          gem-session
Version:       3.2.0
Release:       alt1
Summary:       session
License:       same as ruby's
Group:         Development/Ruby
Url:           https://github.com/ahoward/session
Vcs:           https://github.com/ahoward/session.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(session) = 3.2.0


%description
persistent connections with external programs like bash


%package       -n gem-session-doc
Version:       3.2.0
Release:       alt1
Summary:       session documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета session
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(session) = 3.2.0

%description   -n gem-session-doc
session documentation files.

persistent connections with external programs like bash

%description   -n gem-session-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета session.


%package       -n gem-session-devel
Version:       3.2.0
Release:       alt1
Summary:       session development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета session
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(session) = 3.2.0

%description   -n gem-session-devel
session development package.

persistent connections with external programs like bash

%description   -n gem-session-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета session.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-session-doc
%doc README
%ruby_gemdocdir

%files         -n gem-session-devel
%doc README


%changelog
* Wed Nov 22 2023 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- + packaged gem with Ruby Policy 2.0
