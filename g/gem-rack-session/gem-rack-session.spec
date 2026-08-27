%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rack-session

Name:          gem-rack-session
Version:       2.1.2
Release:       alt1
Summary:       A session implementation for Rack
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rack/rack-session
Vcs:           https://github.com/rack/rack-session.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(base64) >= 0.1.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-global_expectations) >= 0
BuildRequires: gem(minitest-sprint) >= 0
BuildRequires: gem(rack) >= 3.0.0
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
Requires:      ruby >= 2.5
Requires:      gem(base64) >= 0.1.0
Requires:      gem(rack) >= 3.0.0
Provides:      gem(rack-session) = 2.1.2

%description
Session management implementation for Rack.


%if_enabled    doc
%package       -n gem-rack-session-doc
Version:       2.1.2
Release:       alt1
Summary:       A session implementation for Rack documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-session
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-session) = 2.1.2

%description   -n gem-rack-session-doc
A session implementation for Rack documentation files.

Session management implementation for Rack.

%description   -n gem-rack-session-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-session.
%endif


%if_enabled    devel
%package       -n gem-rack-session-devel
Version:       2.1.2
Release:       alt1
Summary:       A session implementation for Rack development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-session
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-session) = 2.1.2
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-global_expectations) >= 0
Requires:      gem(minitest-sprint) >= 0
Requires:      gem(rake) >= 0
Conflicts:     gem(minitest) >= 7

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
%doc license.md readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rack-session-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rack-session-devel
%doc license.md readme.md
%endif


%changelog
* Sat Aug 22 2026 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1
- ^ 2.0.0 -> 2.1.2

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
