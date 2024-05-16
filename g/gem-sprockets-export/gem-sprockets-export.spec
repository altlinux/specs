%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sprockets-export

Name:          gem-sprockets-export
Version:       1.0.0
Release:       alt1
Summary:       Sprockets Export
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/javan/sprockets-export
Vcs:           https://github.com/javan/sprockets-export.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(sprockets) >= 3.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildConflicts: gem(rack) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 3.0.0,rack < 4
Provides:      gem(sprockets-export) = 1.0.0


%description
A Sprockets directive for hassle-free UMD-style JavaScript module definitions.


%if_enabled    doc
%package       -n gem-sprockets-export-doc
Version:       1.0.0
Release:       alt1
Summary:       Sprockets Export documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sprockets-export
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sprockets-export) = 1.0.0

%description   -n gem-sprockets-export-doc
Sprockets Export documentation files.

A Sprockets directive for hassle-free UMD-style JavaScript module definitions.

%description   -n gem-sprockets-export-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sprockets-export.
%endif


%if_enabled    devel
%package       -n gem-sprockets-export-devel
Version:       1.0.0
Release:       alt1
Summary:       Sprockets Export development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sprockets-export
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sprockets-export) = 1.0.0
Requires:      gem(sprockets) >= 3.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Conflicts:     gem(rack) >= 4

%description   -n gem-sprockets-export-devel
Sprockets Export development package.

A Sprockets directive for hassle-free UMD-style JavaScript module definitions.

%description   -n gem-sprockets-export-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sprockets-export.
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
%files         -n gem-sprockets-export-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sprockets-export-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
