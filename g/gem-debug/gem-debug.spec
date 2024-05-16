%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname debug

Name:          gem-debug
Version:       1.9.2
Release:       alt1
Summary:       Debugging functionality for Ruby
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/debug
Vcs:           https://github.com/ruby/debug.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 3.0
BuildRequires: gem(test-unit-rr) >= 0
BuildRequires: gem(json-schema) >= 0
BuildRequires: gem(test-unit-launchable) >= 0
BuildRequires: gem(irb) >= 1.10
BuildRequires: gem(reline) >= 0.3.8
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(irb) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(irb) >= 1.10
Requires:      gem(reline) >= 0.3.8
Conflicts:     gem(irb) >= 2
Provides:      gem(debug) = 1.9.2


%description
Debugging functionality for Ruby. This is completely rewritten debug.rb which
was contained by the ancient Ruby versions.


%package       -n rdbg
Version:       1.9.2
Release:       alt1
Summary:       Debugging functionality for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета debug
Group:         Other
BuildArch:     noarch

Requires:      gem(debug) = 1.9.2

%description   -n rdbg
Debugging functionality for Ruby executable(s).

Debugging functionality for Ruby. This is completely rewritten debug.rb which
was contained by the ancient Ruby versions.

%description   -n rdbg -l ru_RU.UTF-8
Исполнямка для самоцвета debug.


%if_enabled    doc
%package       -n gem-debug-doc
Version:       1.9.2
Release:       alt1
Summary:       Debugging functionality for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета debug
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(debug) = 1.9.2

%description   -n gem-debug-doc
Debugging functionality for Ruby documentation files.

Debugging functionality for Ruby. This is completely rewritten debug.rb which
was contained by the ancient Ruby versions.
%description   -n gem-debug-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета debug.
%endif


%if_enabled    devel
%package       -n gem-debug-devel
Version:       1.9.2
Release:       alt1
Summary:       Debugging functionality for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета debug
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(debug) = 1.9.2
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(test-unit) >= 3.0
Requires:      gem(test-unit-rr) >= 0
Requires:      gem(json-schema) >= 0
Requires:      gem(test-unit-launchable) >= 0
Conflicts:     gem(test-unit) >= 4

%description   -n gem-debug-devel
Debugging functionality for Ruby development package.

Debugging functionality for Ruby. This is completely rewritten debug.rb which
was contained by the ancient Ruby versions.

%description   -n gem-debug-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета debug.
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
%doc README.md misc/README.md.erb
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n rdbg
%doc README.md misc/README.md.erb
%_bindir/rdbg

%if_enabled    doc
%files         -n gem-debug-doc
%doc README.md misc/README.md.erb
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-debug-devel
%doc README.md misc/README.md.erb
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.9.2-alt1
- ^ 1.6.3 -> 1.9.2

* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 1.6.3-alt1
- + packaged gem with Ruby Policy 2.0
