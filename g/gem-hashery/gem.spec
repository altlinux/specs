%define        gemname hashery

Name:          gem-hashery
Version:       2.1.1
Release:       alt1
Summary:       Facets-bread collection of Hash-like classes
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://rubyworks.github.com/hashery
Vcs:           https://github.com/rubyworks/hashery.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(qed) >= 0
BuildRequires: gem(lemon) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(qed) >= 0
Requires:      gem(lemon) >= 0
Provides:      gem(hashery) = 2.1.1


%description
The Hashery is a tight collection of Hash-like classes. Included among its many
offerings are the auto-sorting Dictionary class, the efficient LRUHash, the
flexible OpenHash and the convenient KeyHash. Nearly every class is a subclass
of the CRUDHash which defines a CRUD model on top of Ruby's standard Hash making
it a snap to subclass and augment to fit any specific use case.


%package       -n gem-hashery-doc
Version:       2.1.1
Release:       alt1
Summary:       Facets-bread collection of Hash-like classes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hashery
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hashery) = 2.1.1

%description   -n gem-hashery-doc
Facets-bread collection of Hash-like classes documentation files.

The Hashery is a tight collection of Hash-like classes. Included among its many
offerings are the auto-sorting Dictionary class, the efficient LRUHash, the
flexible OpenHash and the convenient KeyHash. Nearly every class is a subclass
of the CRUDHash which defines a CRUD model on top of Ruby's standard Hash making
it a snap to subclass and augment to fit any specific use case.

%description   -n gem-hashery-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hashery.


%package       -n gem-hashery-devel
Version:       2.1.1
Release:       alt1
Summary:       Facets-bread collection of Hash-like classes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hashery
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hashery) = 2.1.1

%description   -n gem-hashery-devel
Facets-bread collection of Hash-like classes development package.

The Hashery is a tight collection of Hash-like classes. Included among its many
offerings are the auto-sorting Dictionary class, the efficient LRUHash, the
flexible OpenHash and the convenient KeyHash. Nearly every class is a subclass
of the CRUDHash which defines a CRUD model on top of Ruby's standard Hash making
it a snap to subclass and augment to fit any specific use case.

%description   -n gem-hashery-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hashery.


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

%files         -n gem-hashery-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hashery-devel
%doc README.md


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- + packaged gem with Ruby Policy 2.0
