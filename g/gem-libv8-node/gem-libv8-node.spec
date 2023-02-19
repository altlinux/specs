%define        gemname libv8-node

Name:          gem-libv8-node
Version:       16.10.0.0.1
Release:       alt0.1
Summary:       Node.JS's V8 JavaScript engine
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sqreen/ruby-libv8-node
Vcs:           https://github.com/sqreen/ruby-libv8-node.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Patch:         fix-ext.patch
BuildRequires(pre): rpm-build-ruby
# BuildRequires: libv8-3.14-devel
%if_with check
BuildRequires: gem(rake) >= 12
BuildRequires: gem(rubocop) >= 0.50.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Provides:      gem(libv8-node) = 16.10.0.0.1

%ruby_use_gem_version libv8-node:16.10.0.0.1

%description
Node.JS's V8 JavaScript engine for multiplatform goodness


%package       -n gem-libv8-node-doc
Version:       16.10.0.0.1
Release:       alt0.1
Summary:       Node.JS's V8 JavaScript engine documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета libv8-node
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(libv8-node) = 16.10.0.0.1

%description   -n gem-libv8-node-doc
Node.JS's V8 JavaScript engine documentation files.

Node.JS's V8 JavaScript engine for multiplatform goodness

%description   -n gem-libv8-node-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета libv8-node.


%package       -n gem-libv8-node-devel
Version:       16.10.0.0.1
Release:       alt0.1
Summary:       Node.JS's V8 JavaScript engine development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета libv8-node
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(libv8-node) = 16.10.0.0.1
Requires:      gem(rake) >= 12
Requires:      gem(rubocop) >= 0.50.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2

%description   -n gem-libv8-node-devel
Node.JS's V8 JavaScript engine development package.

Node.JS's V8 JavaScript engine for multiplatform goodness

%description   -n gem-libv8-node-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета libv8-node.


%prep
%setup
%autopatch

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
# %ruby_gemextdir

%files         -n gem-libv8-node-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-libv8-node-devel
%doc README.md


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 16.10.0.0.1-alt0.1
- + packaged gem version 16.10.0.0p1 with Ruby Policy 2.0 (no so-lib)
