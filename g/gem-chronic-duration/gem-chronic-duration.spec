%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chronic_duration

Name:          gem-chronic-duration
Version:       0.10.6.3
Release:       alt0.1
Summary:       A simple Ruby natural language parser for elapsed time
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/hpoydar/chronic_duration
Vcs:           https://github.com/hpoydar/chronic_duration.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 10.0.3
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(numerizer) >= 0.2.0
BuildRequires: gem(rspec) >= 2.12.0
BuildConflicts: gem(numerizer) >= 0.3
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_alias_names chronic_duration,chronic-duration
Requires:      gem(numerizer) >= 0.2.0
Conflicts:     gem(numerizer) >= 0.3
Provides:      gem(chronic_duration) = 0.10.6.3

%ruby_use_gem_version chronic_duration:0.10.6.3

%description
A simple Ruby natural language parser for elapsed time. (For example, 4 hours
and 30 minutes, 6 minutes 4 seconds, 3 days, etc.) Returns all results in
seconds. Will return an integer unless you get tricky and need a float. (4
minutes and 13.47 seconds, for example.) The reverse can also be performed via
the output method.


%if_enabled    doc
%package       -n gem-chronic-duration-doc
Version:       0.10.6.3
Release:       alt0.1
Summary:       A simple Ruby natural language parser for elapsed time documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chronic_duration
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chronic_duration) = 0.10.6.3

%description   -n gem-chronic-duration-doc
A simple Ruby natural language parser for elapsed time documentation files.

A simple Ruby natural language parser for elapsed time. (For example, 4 hours
and 30 minutes, 6 minutes 4 seconds, 3 days, etc.) Returns all results in
seconds. Will return an integer unless you get tricky and need a float. (4
minutes and 13.47 seconds, for example.) The reverse can also be performed via
the output method.

%description   -n gem-chronic-duration-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chronic_duration.
%endif


%if_enabled    devel
%package       -n gem-chronic-duration-devel
Version:       0.10.6.3
Release:       alt0.1
Summary:       A simple Ruby natural language parser for elapsed time development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chronic_duration
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chronic_duration) = 0.10.6.3
Requires:      gem(rake) >= 10.0.3
Requires:      gem(rspec) >= 2.12.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-chronic-duration-devel
A simple Ruby natural language parser for elapsed time development package.

A simple Ruby natural language parser for elapsed time. (For example, 4 hours
and 30 minutes, 6 minutes 4 seconds, 3 days, etc.) Returns all results in
seconds. Will return an integer unless you get tricky and need a float. (4
minutes and 13.47 seconds, for example.) The reverse can also be performed via
the output method.

%description   -n gem-chronic-duration-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chronic_duration.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-chronic-duration-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chronic-duration-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 0.10.6.3-alt0.1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
