%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rack-session

Name:          gem-rack-session
Version:       2.0.0
Release:       alt1
Summary:       A session implementation for Rack
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rack/rack-session
Vcs:           https://github.com/rack/rack-session.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rack) >= 2.2.2
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-global_expectations) >= 0
BuildRequires: gem(minitest-sprint) >= 0
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rack) >= 2.2.2
Provides:      gem(rack-session) = 2.0.0


%description
Session management implementation for Rack.


%if_enabled    doc
%package       -n gem-rack-session-doc
Version:       2.0.0
Release:       alt1
Summary:       A session implementation for Rack documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-session
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-session) = 2.0.0

%description   -n gem-rack-session-doc
A session implementation for Rack documentation files.

Session management implementation for Rack.

%description   -n gem-rack-session-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-session.
%endif


%if_enabled    devel
%package       -n gem-rack-session-devel
Version:       2.0.0
Release:       alt1
Summary:       A session implementation for Rack development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-session
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-session) = 2.0.0
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-global_expectations) >= 0
Requires:      gem(minitest-sprint) >= 0
Requires:      gem(rake) >= 0
Conflicts:     gem(minitest) >= 6

%description   -n gem-rack-session-devel
A session implementation for Rack development package.

Session management implementation for Rack.

%description   -n gem-rack-session-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-session.
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
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rack-session-doc
%doc readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rack-session-devel
%doc readme.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
