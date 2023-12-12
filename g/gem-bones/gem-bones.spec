%define        _unpackaged_files_terminate_build 1
%define        gemname bones

Name:          gem-bones
Version:       3.9.0
Release:       alt1
Summary:       Mr Bones is a handy tool that creates new Ruby projects from a code skeleton
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/TwP/bones
Vcs:           https://github.com/twp/bones.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rdoc) >= 6.0
BuildRequires: gem(little-plugger) >= 1.1
BuildRequires: gem(loquacious) >= 1.9
BuildRequires: gem(rspec) >= 3.5
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(little-plugger) >= 2
BuildConflicts: gem(loquacious) >= 2
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 13.0
Requires:      gem(rdoc) >= 6.0
Requires:      gem(little-plugger) >= 1.1
Requires:      gem(loquacious) >= 1.9
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(little-plugger) >= 2
Conflicts:     gem(loquacious) >= 2
Provides:      gem(bones) = 3.9.0

%ruby_bindir_to %ruby_bindir

%description
Mr Bones is a handy tool that creates new Ruby projects from a code skeleton.
The skeleton contains some starter code and a collection of rake tasks to ease
the management and deployment of your source code. Several Mr Bones plugins are
available for creating git repositories, creating GitHub projects, running
various test suites and source code analysis tools.


%package       -n bones
Version:       3.9.0
Release:       alt1
Summary:       Mr Bones is a handy tool that creates new Ruby projects from a code skeleton executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bones
Group:         Other
BuildArch:     noarch

Requires:      gem(bones) = 3.9.0

%description   -n bones
Mr Bones is a handy tool that creates new Ruby projects from a code skeleton
executable(s).

%description   -n bones -l ru_RU.UTF-8
Исполнямка для самоцвета bones.


%package       -n gem-bones-doc
Version:       3.9.0
Release:       alt1
Summary:       Mr Bones is a handy tool that creates new Ruby projects from a code skeleton documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bones
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bones) = 3.9.0

%description   -n gem-bones-doc
Mr Bones is a handy tool that creates new Ruby projects from a code skeleton
documentation files.

%description   -n gem-bones-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bones.


%package       -n gem-bones-devel
Version:       3.9.0
Release:       alt1
Summary:       Mr Bones is a handy tool that creates new Ruby projects from a code skeleton development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bones
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bones) = 3.9.0
Requires:      gem(rspec) >= 3.5
Conflicts:     gem(rspec) >= 4

%description   -n gem-bones-devel
Mr Bones is a handy tool that creates new Ruby projects from a code skeleton
development package.

%description   -n gem-bones-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bones.


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

%files         -n bones
%doc README.rdoc
%ruby_bindir/bones

%files         -n gem-bones-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-bones-devel
%doc README.rdoc


%changelog
* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 3.9.0-alt1
- ^ 3.8.4 -> 3.9.0

* Tue Jun 30 2020 Pavel Skrylev <majioa@altlinux.org> 3.8.4-alt1
- + packaged as a gem with usage Ruby Policy 2.0.
