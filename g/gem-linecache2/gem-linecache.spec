%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname linecache2

Name:          gem-linecache2
Version:       1.4.0
Release:       alt1
Summary:       Module to read and cache Ruby program files and file information
License:       GPLv2
Group:         Development/Ruby
Url:           https://github.com/rocky/rb-linecache2
Vcs:           https://github.com/rocky/rb-linecache2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.1.4
BuildRequires: gem(term-ansicolor) >= 1.3
BuildRequires: gem(coderay) >= 1.1.1
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(term-ansicolor) >= 2
BuildConflicts: gem(coderay) >= 1.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(linecache2) = 1.4.0


%description
LineCache is a module for reading and caching lines. This may be useful for
example in a debugger where the same lines are shown many times.

This version works only with a Ruby 2.0 or greater.


%if_enabled    doc
%package       -n gem-linecache2-doc
Version:       1.4.0
Release:       alt1
Summary:       Module to read and cache Ruby program files and file information documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета linecache2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(linecache2) = 1.4.0

%description   -n gem-linecache2-doc
Module to read and cache Ruby program files and file information documentation
files.

LineCache is a module for reading and caching lines. This may be useful for
example in a debugger where the same lines are shown many times.

This version works only with a Ruby 2.0 or greater.

%description   -n gem-linecache2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета linecache2.
%endif


%if_enabled    devel
%package       -n gem-linecache2-devel
Version:       1.4.0
Release:       alt1
Summary:       Module to read and cache Ruby program files and file information development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета linecache2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(linecache2) = 1.4.0
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(term-ansicolor) >= 1.3
Requires:      gem(coderay) >= 1.1.1
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(term-ansicolor) >= 2
Conflicts:     gem(coderay) >= 1.2

%description   -n gem-linecache2-devel
Module to read and cache Ruby program files and file information development
package.

LineCache is a module for reading and caching lines. This may be useful for
example in a debugger where the same lines are shown many times.

This version works only with a Ruby 2.0 or greater.

%description   -n gem-linecache2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета linecache2.
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
%files         -n gem-linecache2-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-linecache2-devel
%doc README.md
%endif


%changelog
* Thu Aug 01 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- + packaged gem with Ruby Policy 2.0
