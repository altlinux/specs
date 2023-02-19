%define        gemname bones-git

Name:          gem-bones-git
Version:       1.3.1
Release:       alt1
Summary:       Tasks to incorporate git actions into gem release
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/TwP/bones-git
Vcs:           https://github.com/twp/bones-git.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(git) >= 1.2
BuildConflicts: gem(git) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(git) >= 1.2
Conflicts:     gem(git) >= 2
Provides:      gem(bones-git) = 1.3.1

%description
The git package for Mr Bones provides tasks to incorporate git actions into gem
release. It also provides some extensions to the Mr Bones "create" command that
allow you to initialize a git repository and to create a new GitHub project.


%package       -n gem-bones-git-doc
Version:       1.3.1
Release:       alt1
Summary:       Tasks to incorporate git actions into gem release documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bones-git
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bones-git) = 1.3.1

%description   -n gem-bones-git-doc
Tasks to incorporate git actions into gem release documentation files.

The git package for Mr Bones provides tasks to incorporate git actions into gem
release. It also provides some extensions to the Mr Bones "create" command that
allow you to initialize a git repository and to create a new GitHub project.

%description   -n gem-bones-git-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bones-git.


%package       -n gem-bones-git-devel
Version:       1.3.1
Release:       alt1
Summary:       Tasks to incorporate git actions into gem release development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bones-git
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bones-git) = 1.3.1

%description   -n gem-bones-git-devel
Tasks to incorporate git actions into gem release development package.

The git package for Mr Bones provides tasks to incorporate git actions into gem
release. It also provides some extensions to the Mr Bones "create" command that
allow you to initialize a git repository and to create a new GitHub project.

%description   -n gem-bones-git-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bones-git.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-bones-git-doc
%ruby_gemdocdir

%files         -n gem-bones-git-devel


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- + packaged gem with Ruby Policy 2.0
