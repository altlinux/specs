%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-server

Name:          gem-minitest-server
Version:       1.0.8
Release:       alt1
Summary:       minitest-server provides a client/server setup with your minitest process, allowing your test run to send its results directly to a handler
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-server
Vcs:           https://github.com/seattlerb/minitest-server.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.16
BuildRequires: gem(drb) >= 2.0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 4.2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(drb) >= 3
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(hoe) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) >= 5.16
Requires:      gem(drb) >= 2.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(drb) >= 3
Provides:      gem(minitest-server) = 1.0.8


%description
minitest-server provides a client/server setup with your minitest process,
allowing your test run to send its results directly to a handler.


%if_enabled    doc
%package       -n gem-minitest-server-doc
Version:       1.0.8
Release:       alt1
Summary:       minitest-server provides a client/server setup with your minitest process, allowing your test run to send its results directly to a handler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-server
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-server) = 1.0.8

%description   -n gem-minitest-server-doc
minitest-server provides a client/server setup with your minitest process,
allowing your test run to send its results directly to a handler documentation
files.

%description   -n gem-minitest-server-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-server.
%endif


%if_enabled    devel
%package       -n gem-minitest-server-devel
Version:       1.0.8
Release:       alt1
Summary:       minitest-server provides a client/server setup with your minitest process, allowing your test run to send its results directly to a handler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-server
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-server) = 1.0.8
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 4.2
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

%description   -n gem-minitest-server-devel
minitest-server provides a client/server setup with your minitest process,
allowing your test run to send its results directly to a handler development
package.

%description   -n gem-minitest-server-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-server.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-server-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-server-devel
%doc README.rdoc
%endif


%changelog
* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.8-alt1
- ^ 1.0.6 -> 1.0.8

* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.6-alt1
- + packaged gem with Ruby Policy 2.0
