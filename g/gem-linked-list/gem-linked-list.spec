%define        _unpackaged_files_terminate_build 1
%define        gemname linked-list

Name:          gem-linked-list
Version:       0.0.16
Release:       alt1
Summary:       Ruby implementation of Doubly Linked List, following some Ruby idioms
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/spectator/linked-list
Vcs:           https://github.com/spectator/linked-list.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         fix-bin-folder-in-gemspec.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(m) >= 1.5
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rake) >= 12.3.3
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(coveralls) >= 1
BuildConflicts: gem(m) >= 2
BuildConflicts: gem(minitest) >= 6.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(linked-list) = 0.0.16


%description
Ruby implementation of Doubly Linked List, following some Ruby idioms.


%package       -n gem-linked-list-doc
Version:       0.0.16
Release:       alt1
Summary:       Ruby implementation of Doubly Linked List, following some Ruby idioms documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета linked-list
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(linked-list) = 0.0.16

%description   -n gem-linked-list-doc
Ruby implementation of Doubly Linked List, following some Ruby idioms
documentation files.

%description   -n gem-linked-list-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета linked-list.


%package       -n gem-linked-list-devel
Version:       0.0.16
Release:       alt1
Summary:       Ruby implementation of Doubly Linked List, following some Ruby idioms development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета linked-list
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(linked-list) = 0.0.16
Requires:      gem(bundler) >= 2.0
Requires:      gem(coveralls) >= 0
Requires:      gem(m) >= 1.5
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 12.3.3
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(coveralls) >= 1
Conflicts:     gem(m) >= 2
Conflicts:     gem(minitest) >= 6.0

%description   -n gem-linked-list-devel
Ruby implementation of Doubly Linked List, following some Ruby idioms
development package.

%description   -n gem-linked-list-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета linked-list.


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

%files         -n gem-linked-list-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-linked-list-devel
%doc README.md


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.16-alt1
- ^ 0.0.13 -> 0.0.16

* Mon Sep 02 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.13-alt1
- first build for Sisyphus
