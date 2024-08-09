%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hoe-git2

Name:          gem-hoe-git2
Version:       1.8.0
Release:       alt1
Summary:       A set of Hoe plugins for tighter Git integration
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/halostatue/hoe-git
Vcs:           https://github.com/halostatue/hoe-git.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 3.0
BuildRequires: gem(hoe-doofus) >= 1.0
BuildRequires: gem(hoe-gemspec2) >= 1.1
BuildRequires: gem(standard) >= 1.0
BuildRequires: gem(rdoc) >= 4.0
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(hoe-doofus) >= 2
BuildConflicts: gem(hoe-gemspec2) >= 2
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(rdoc) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(hoe-git2) = 1.8.0


%description
A set of Hoe plugins for tighter Git integration. Provides tasks to automate
release tagging and pushing and changelog generation. I expect it'll learn a few
more tricks in the future.

This is an evolution of +hoe-git+ by John Barnette, which has been archived at
<http://github.com/jbarnette/hoe-git>.


%if_enabled    doc
%package       -n gem-hoe-git2-doc
Version:       1.8.0
Release:       alt1
Summary:       A set of Hoe plugins for tighter Git integration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-git2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-git2) = 1.8.0

%description   -n gem-hoe-git2-doc
A set of Hoe plugins for tighter Git integration documentation files.

A set of Hoe plugins for tighter Git integration. Provides tasks to automate
release tagging and pushing and changelog generation. I expect it'll learn a few
more tricks in the future.

This is an evolution of +hoe-git+ by John Barnette, which has been archived at
<http://github.com/jbarnette/hoe-git>.

%description   -n gem-hoe-git2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-git2.
%endif


%if_enabled    devel
%package       -n gem-hoe-git2-devel
Version:       1.8.0
Release:       alt1
Summary:       A set of Hoe plugins for tighter Git integration development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-git2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-git2) = 1.8.0
Requires:      gem(hoe) >= 3.0
Requires:      gem(hoe-doofus) >= 1.0
Requires:      gem(hoe-gemspec2) >= 1.1
Requires:      gem(standard) >= 1.0
Requires:      gem(rdoc) >= 4.0
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(hoe-doofus) >= 2
Conflicts:     gem(hoe-gemspec2) >= 2
Conflicts:     gem(standard) >= 2
Conflicts:     gem(rdoc) >= 7

%description   -n gem-hoe-git2-devel
A set of Hoe plugins for tighter Git integration development package.

A set of Hoe plugins for tighter Git integration. Provides tasks to automate
release tagging and pushing and changelog generation. I expect it'll learn a few
more tricks in the future.

This is an evolution of +hoe-git+ by John Barnette, which has been archived at
<http://github.com/jbarnette/hoe-git>.

%description   -n gem-hoe-git2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-git2.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-hoe-git2-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hoe-git2-devel
%doc README.rdoc
%endif


%changelog
* Wed Jul 31 2024 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- + packaged gem with Ruby Policy 2.0
