%define        gemname rubytree

Name:          gem-rubytree
Version:       1.0.1
Release:       alt1.1
Summary:       Simple implementation of the generic Tree data structure
License:       BSD
Group:         Development/Ruby
Url:           http://rubytree.anupamsg.me/
Vcs:           https://github.com/evolve75/rubytree.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(structured_warnings) >= 0.4.0 gem(structured_warnings) < 0.5
BuildRequires: gem(json) >= 2.3.0 gem(json) < 3
BuildRequires: gem(bundler) >= 2.1.4 gem(bundler) < 3
BuildRequires: gem(rdoc) >= 6.1.1 gem(rdoc) < 7
BuildRequires: gem(yard) >= 0.9.25 gem(yard) < 0.10
BuildRequires: gem(rtagstask) >= 0.0.4 gem(rtagstask) < 0.1
BuildRequires: gem(rspec) >= 3.9.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency json >= 2.3.0,json < 3
Requires:      gem(structured_warnings) >= 0.4.0 gem(structured_warnings) < 0.5
Requires:      gem(json) >= 2.3.0 gem(json) < 3
Obsoletes:     rubytree < %EVR
Provides:      rubytree = %EVR
Provides:      gem(rubytree) = 1.0.1


%description
Rubytree is a simple implementation of the generic Tree data structure. This
implementation is node-centric, where the individual nodes on the tree are the
primary objects and drive the structure.


%package       -n gem-rubytree-doc
Version:       1.0.1
Release:       alt1.1
Summary:       Simple implementation of the generic Tree data structure documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubytree
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubytree) = 1.0.1
Obsoletes:     rubytree-doc
Provides:      rubytree-doc

%description   -n gem-rubytree-doc
Simple implementation of the generic Tree data structure documentation
files.

Rubytree is a simple implementation of the generic Tree data structure. This
implementation is node-centric, where the individual nodes on the tree are the
primary objects and drive the structure.

%description   -n gem-rubytree-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubytree.


%package       -n gem-rubytree-devel
Version:       1.0.1
Release:       alt1.1
Summary:       Simple implementation of the generic Tree data structure development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubytree
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubytree) = 1.0.1
Requires:      gem(bundler) >= 2.1.4 gem(bundler) < 3
Requires:      gem(rdoc) >= 6.1.1 gem(rdoc) < 7
Requires:      gem(yard) >= 0.9.25 gem(yard) < 0.10
Requires:      gem(rtagstask) >= 0.0.4 gem(rtagstask) < 0.1
Requires:      gem(rspec) >= 3.9.0 gem(rspec) < 4

%description   -n gem-rubytree-devel
Simple implementation of the generic Tree data structure development
package.

Rubytree is a simple implementation of the generic Tree data structure. This
implementation is node-centric, where the individual nodes on the tree are the
primary objects and drive the structure.

%description   -n gem-rubytree-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubytree.


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

%files         -n gem-rubytree-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubytree-devel
%doc README.md


%changelog
* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1.1
- ! spec

* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- ^ 1.0.0 -> 1.0.1

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- > Ruby Policy 2.0

* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version.
- Disable tests.

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.5.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Nov 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5.2-alt1
- Built for Sisyphus
