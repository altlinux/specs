# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname git

Name:          gem-git
Version:       2.3.0
Release:       alt1
Summary:       Ruby/Git is a Ruby library that can be used to create
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-git/ruby-git
Vcs:           https://github.com/ruby-git/ruby-git.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(create_github_release) >= 1.4
BuildRequires: gem(minitar) >= 0.9
BuildRequires: gem(mocha) >= 1.11.2
BuildRequires: gem(rake) >= 13.1
BuildRequires: gem(test-unit) >= 3.3.5
BuildRequires: gem(redcarpet) >= 3.6
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yardstick) >= 0.9
BuildRequires: gem(activesupport) >= 5.0
BuildRequires: gem(addressable) >= 2.8
BuildRequires: gem(process_executer) >= 1.1
BuildRequires: gem(rchardet) >= 1.8
BuildConflicts: gem(create_github_release) >= 2
BuildConflicts: gem(minitar) >= 1
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(redcarpet) >= 4
BuildConflicts: gem(yardstick) >= 1
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(process_executer) >= 2
BuildConflicts: gem(rchardet) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      gem(activesupport) >= 5.0
Requires:      gem(addressable) >= 2.8
Requires:      gem(process_executer) >= 1.1
Requires:      gem(rchardet) >= 1.8
Requires:      git-core
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(process_executer) >= 2
Conflicts:     gem(rchardet) >= 2
Provides:      gem(git) = 2.3.0


%description
Ruby/Git is a Ruby library that can be used to create, read and manipulate Git
repositories by wrapping system calls to the git binary.


%if_enabled    doc
%package       -n gem-git-doc
Version:       2.3.0
Release:       alt1
Summary:       Ruby/Git is a Ruby library that can be used to create documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета git
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(git) = 2.3.0

%description   -n gem-git-doc
Ruby/Git is a Ruby library that can be used to create documentation
files.

Ruby/Git is a Ruby library that can be used to create, read and manipulate Git
repositories by wrapping system calls to the git binary.

%description   -n gem-git-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета git.
%endif


%if_enabled    devel
%package       -n gem-git-devel
Version:       2.3.0
Release:       alt1
Summary:       Ruby/Git is a Ruby library that can be used to create development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета git
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(git) = 2.3.0
Requires:      gem(create_github_release) >= 1.4
Requires:      gem(minitar) >= 0.9
Requires:      gem(mocha) >= 1.11.2
Requires:      gem(rake) >= 13.1
Requires:      gem(test-unit) >= 3.3.5
Requires:      gem(redcarpet) >= 3.6
Requires:      gem(yard) >= 0.9
Requires:      gem(yardstick) >= 0.9
Conflicts:     gem(create_github_release) >= 2
Conflicts:     gem(minitar) >= 1
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(yardstick) >= 1

%description   -n gem-git-devel
Ruby/Git is a Ruby library that can be used to create development
package.

Ruby/Git is a Ruby library that can be used to create, read and manipulate Git
repositories by wrapping system calls to the git binary.

%description   -n gem-git-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета git.
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
%files         -n gem-git-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-git-devel
%doc README.md
%endif


%changelog
* Wed Oct 23 2024 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- ^ 1.19.1 -> 2.3.0

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.19.1-alt1
- ^ 1.18.0 -> 1.19.1

* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 1.18.0-alt0.1
- ^ 1.7.0 -> 1.18.0 (no devel)

* Wed Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- + packaged gem with usage Ruby Policy 2.0
