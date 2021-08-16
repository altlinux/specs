%define        gemname ancestry

Name:          gem-ancestry
Version:       4.0.0
Release:       alt1
Summary:       Organise ActiveRecord model into a tree structure
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/stefankroes/ancestry
Vcs:           https://github.com/stefankroes/ancestry.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activerecord) >= 5.2.4.5
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(minitest) >= 0 gem(minitest) < 6
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(yard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activerecord) >= 5.2.4.5
Obsoletes:     ruby-ancestry
Provides:      ruby-ancestry
Provides:      gem(ancestry) = 4.0.0


%description
Ancestry is a gem that allows the records of a Ruby on Rails ActiveRecord model
to be organised as a tree structure (or hierarchy). It employs the materialised
path pattern and exposes all the standard tree structure relations (ancestors,
parent, root, children, siblings, descendants), allowing all of them to
be fetched in a single SQL query. Additional features include STI support,
scopes, depth caching, depth constraints, easy migration from older gems,
integrity checking, integrity restoration, arrangement of (sub)trees into
hashes, and various strategies for dealing with orphaned records.


%package       -n gem-ancestry-doc
Version:       4.0.0
Release:       alt1
Summary:       Organise ActiveRecord model into a tree structure documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ancestry
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ancestry) = 4.0.0

%description   -n gem-ancestry-doc
Organise ActiveRecord model into a tree structure documentation files.

Ancestry is a gem that allows the records of a Ruby on Rails ActiveRecord model
to be organised as a tree structure (or hierarchy). It employs the materialised
path pattern and exposes all the standard tree structure relations (ancestors,
parent, root, children, siblings, descendants), allowing all of them to
be fetched in a single SQL query. Additional features include STI support,
scopes, depth caching, depth constraints, easy migration from older gems,
integrity checking, integrity restoration, arrangement of (sub)trees into
hashes, and various strategies for dealing with orphaned records.

%description   -n gem-ancestry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ancestry.


%package       -n gem-ancestry-devel
Version:       4.0.0
Release:       alt1
Summary:       Organise ActiveRecord model into a tree structure development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ancestry
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ancestry) = 4.0.0
Requires:      gem(appraisal) >= 0
Requires:      gem(minitest) >= 0 gem(minitest) < 6
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(yard) >= 0

%description   -n gem-ancestry-devel
Organise ActiveRecord model into a tree structure development package.

Ancestry is a gem that allows the records of a Ruby on Rails ActiveRecord model
to be organised as a tree structure (or hierarchy). It employs the materialised
path pattern and exposes all the standard tree structure relations (ancestors,
parent, root, children, siblings, descendants), allowing all of them to
be fetched in a single SQL query. Additional features include STI support,
scopes, depth caching, depth constraints, easy migration from older gems,
integrity checking, integrity restoration, arrangement of (sub)trees into
hashes, and various strategies for dealing with orphaned records.

%description   -n gem-ancestry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ancestry.


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

%files         -n gem-ancestry-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ancestry-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt1
- ^ 3.2.1 -> 4.0.0

* Wed Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.2.1-alt1
- ^ 3.0.7 -> 3.2.1
- ! spec

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.7-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.7-alt1
- updated (^) 3.0.5 -> v3.0.7

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.5-alt1
- updated (^) 3.0.3 -> 3.0.5
- used (>) Ruby Policy 2.0

* Mon Oct 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.0.3-alt1
- updated (^) 3.0.2 -> 3.0.3

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 3.0.2-alt2
- fixed (!) gemify the package.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- adeed (+) initial build for Sisyphus
