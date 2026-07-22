%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname transproc

Name:          gem-transproc
Version:       1.1.1
Release:       alt1
Summary:       Transform Ruby objects in functional style
License:       MIT
Group:         Development/Ruby
Url:           http://solnic.github.io/transproc/
Vcs:           https://github.com/solnic/transproc.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(dry-equalizer) >= 0.2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(warning) >= 0
BuildConflicts: gem(dry-equalizer) >= 1
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.3.0
Provides:      gem(transproc) = 1.1.1

%description
Transform Ruby objects in functional style


%if_enabled    doc
%package       -n gem-transproc-doc
Version:       1.1.1
Release:       alt1
Summary:       Transform Ruby objects in functional style documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета transproc
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(transproc) = 1.1.1

%description   -n gem-transproc-doc
Transform Ruby objects in functional style documentation files.

%description   -n gem-transproc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета transproc.
%endif


%if_enabled    devel
%package       -n gem-transproc-devel
Version:       1.1.1
Release:       alt1
Summary:       Transform Ruby objects in functional style development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета transproc
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(transproc) = 1.1.1
Requires:      gem(dry-equalizer) >= 0.2
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.8
Requires:      gem(warning) >= 0
Conflicts:     gem(dry-equalizer) >= 1
Conflicts:     gem(rspec) >= 4

%description   -n gem-transproc-devel
Transform Ruby objects in functional style development package.

%description   -n gem-transproc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета transproc.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-transproc-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-transproc-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
