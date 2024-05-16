%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname tracer

Name:          gem-tracer
Version:       0.2.3
Release:       alt1
Summary:       A Ruby tracer
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/tracer
Vcs:           https://github.com/ruby/tracer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(irb) >= 0
BuildRequires: gem(test-unit) >= 3.0
BuildRequires: gem(syntax_tree) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(test-unit) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(tracer) = 0.2.3


%description
A Ruby tracer


%if_enabled    doc
%package       -n gem-tracer-doc
Version:       0.2.3
Release:       alt1
Summary:       A Ruby tracer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tracer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tracer) = 0.2.3

%description   -n gem-tracer-doc
A Ruby tracer documentation files.
%description   -n gem-tracer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tracer.
%endif


%if_enabled    devel
%package       -n gem-tracer-devel
Version:       0.2.3
Release:       alt1
Summary:       A Ruby tracer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tracer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tracer) = 0.2.3
Requires:      gem(rake) >= 13.0
Requires:      gem(irb) >= 0
Requires:      gem(test-unit) >= 3.0
Requires:      gem(syntax_tree) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(test-unit) >= 4

%description   -n gem-tracer-devel
A Ruby tracer development package.
%description   -n gem-tracer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tracer.
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
%files         -n gem-tracer-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-tracer-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt1
- + packaged gem with Ruby Policy 2.0
