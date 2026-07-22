%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-equalizer

Name:          gem-dry-equalizer
Version:       0.3.0
Release:       alt1
Summary:       Module to define equality, equivalence and inspection methods
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/dry-rb/dry-equalizer
Vcs:           https://github.com/dry-rb/dry-equalizer.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.5
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.4.0
Provides:      gem(dry-equalizer) = 0.3.0

%description
Module to define equality, equivalence and inspection methods


%if_enabled    doc
%package       -n gem-dry-equalizer-doc
Version:       0.3.0
Release:       alt1
Summary:       Module to define equality, equivalence and inspection methods documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-equalizer
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(dry-equalizer) = 0.3.0

%description   -n gem-dry-equalizer-doc
Module to define equality, equivalence and inspection methods documentation
files.

%description   -n gem-dry-equalizer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-equalizer.
%endif


%if_enabled    devel
%package       -n gem-dry-equalizer-devel
Version:       0.3.0
Release:       alt1
Summary:       Module to define equality, equivalence and inspection methods development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-equalizer
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(dry-equalizer) = 0.3.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.5
Conflicts:     gem(rspec) >= 4

%description   -n gem-dry-equalizer-devel
Module to define equality, equivalence and inspection methods development
package.

%description   -n gem-dry-equalizer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-equalizer.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-dry-equalizer-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-equalizer-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%endif


%changelog
* Mon Jul 06 2026 Alexander Burmatov <thatman@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
