%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pond

Name:          gem-pond
Version:       0.5.0
Release:       alt1
Summary:       A simple, generic, thread-safe pool
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chanks/pond
Vcs:           https://github.com/chanks/pond.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rspec) >= 2.14
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(pond) = 0.5.0


%description
A simple, generic, thread-safe pool for connections or whatever else.


%if_enabled    doc
%package       -n gem-pond-doc
Version:       0.5.0
Release:       alt1
Summary:       A simple, generic, thread-safe pool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pond
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pond) = 0.5.0

%description   -n gem-pond-doc
A simple, generic, thread-safe pool documentation files.

A simple, generic, thread-safe pool for connections or whatever else

%description   -n gem-pond-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pond.
%endif


%if_enabled    devel
%package       -n gem-pond-devel
Version:       0.5.0
Release:       alt1
Summary:       A simple, generic, thread-safe pool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pond
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pond) = 0.5.0
Requires:      gem(bundler) >= 1.3
Requires:      gem(rspec) >= 2.14
Requires:      gem(rake) >= 0

%description   -n gem-pond-devel
A simple, generic, thread-safe pool development package.

A simple, generic, thread-safe pool for connections or whatever else

%description   -n gem-pond-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pond.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-pond-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pond-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0
