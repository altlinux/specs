%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname libv8-node

Name:          gem-libv8-node
Version:       22.5.1.0
Release:       alt1
Summary:       Node.JS's V8 JavaScript engine
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubyjs/libv8-node
Vcs:           https://github.com/rubyjs/libv8-node.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         fix-ext.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 12
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Provides:      gem(libv8-node) = 22.5.1.0


%description
Node.JS's V8 JavaScript engine for multiplatform goodness


%if_enabled    doc
%package       -n gem-libv8-node-doc
Version:       22.5.1.0
Release:       alt1
Summary:       Node.JS's V8 JavaScript engine documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета libv8-node
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(libv8-node) = 22.5.1.0

%description   -n gem-libv8-node-doc
Node.JS's V8 JavaScript engine documentation files.

Node.JS's V8 JavaScript engine for multiplatform goodness

%description   -n gem-libv8-node-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета libv8-node.
%endif


%if_enabled    devel
%package       -n gem-libv8-node-devel
Version:       22.5.1.0
Release:       alt1
Summary:       Node.JS's V8 JavaScript engine development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета libv8-node
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(libv8-node) = 22.5.1.0
Requires:      gem(rake) >= 12
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2

%description   -n gem-libv8-node-devel
Node.JS's V8 JavaScript engine development package.

Node.JS's V8 JavaScript engine for multiplatform goodness

%description   -n gem-libv8-node-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета libv8-node.
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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-libv8-node-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-libv8-node-devel
%doc README.md
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 22.5.1.0-alt1
- ^ 16.10.0.0p1 -> 22.5.1.0

* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 16.10.0.0.1-alt0.1
- + packaged gem version 16.10.0.0p1 with Ruby Policy 2.0 (no so-lib)
