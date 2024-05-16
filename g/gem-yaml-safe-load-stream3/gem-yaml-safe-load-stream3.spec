%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname yaml-safe_load_stream3

Name:          gem-yaml-safe-load-stream3
Version:       0.1.2
Release:       alt1
Summary:       Adds YAML.safe_load_stream for safely parsing multi-document YAML streams
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/sathish-progress/yaml-safe_load_stream3
Vcs:           https://github.com/sathish-progress/yaml-safe_load_stream3.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(yaml-safe_load_stream3) = 0.1.2


%description
The Ruby standard library defines YAML.safe_load and YAML.load_stream but
there's no way to safely load a multi document stream. This Gem adds
YAML.safe_load_stream.


%if_enabled    doc
%package       -n gem-yaml-safe-load-stream3-doc
Version:       0.1.2
Release:       alt1
Summary:       Adds YAML.safe_load_stream for safely parsing multi-document YAML streams documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yaml-safe_load_stream3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yaml-safe_load_stream3) = 0.1.2

%description   -n gem-yaml-safe-load-stream3-doc
Adds YAML.safe_load_stream for safely parsing multi-document YAML streams
documentation files.

%description   -n gem-yaml-safe-load-stream3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yaml-safe_load_stream3.
%endif


%if_enabled    devel
%package       -n gem-yaml-safe-load-stream3-devel
Version:       0.1.2
Release:       alt1
Summary:       Adds YAML.safe_load_stream for safely parsing multi-document YAML streams development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yaml-safe_load_stream3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yaml-safe_load_stream3) = 0.1.2
Requires:      gem(bundler) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(rspec) >= 4

%description   -n gem-yaml-safe-load-stream3-devel
Adds YAML.safe_load_stream for safely parsing multi-document YAML streams
development package.

%description   -n gem-yaml-safe-load-stream3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yaml-safe_load_stream3.
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
%files         -n gem-yaml-safe-load-stream3-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-yaml-safe-load-stream3-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
