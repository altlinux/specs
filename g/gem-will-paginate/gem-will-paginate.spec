# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%define        gemname will_paginate

Name:          gem-will-paginate
Version:       4.0.0
Release:       alt1
Summary:       Pagination library for Rails, Sinatra, Merb, DataMapper, and more
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mislav/will_paginate
Vcs:           https://github.com/mislav/will_paginate.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(activerecord) >= 6.1.7.1
BuildRequires: gem(actionpack) >= 6.1.7.1
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(mocha) >= 1.11.2
BuildRequires: gem(sqlite3) >= 1.4.0
BuildRequires: gem(mysql2) >= 0.5.2
BuildRequires: gem(pg) >= 1.2
BuildConflicts: gem(activerecord) >= 8
BuildConflicts: gem(actionpack) >= 8
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(sqlite3) >= 2
BuildConflicts: gem(mysql2) >= 0.6
BuildConflicts: gem(pg) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency sqlite3 >= 1.5.3,sqlite3 < 2
%ruby_use_gem_dependency activerecord >= 6.1.7.1,activerecord < 8
Obsoletes:     ruby-will_paginate < %EVR
Provides:      ruby-will_paginate = %EVR
Provides:      gem(will_paginate) = 4.0.0


%description
will_paginate is a pagination library that integrates with Ruby on Rails,
Sinatra, Merb, DataMapper and Sequel.


%package       -n gem-will-paginate-doc
Version:       4.0.0
Release:       alt1
Summary:       Pagination library for Rails, Sinatra, Merb, DataMapper, and more documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета will_paginate
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(will_paginate) = 4.0.0

%description   -n gem-will-paginate-doc
Pagination library for Rails, Sinatra, Merb, DataMapper, and more documentation
files.

will_paginate is a pagination library that integrates with Ruby on Rails,
Sinatra, Merb, DataMapper and Sequel.

%description   -n gem-will-paginate-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета will_paginate.


%package       -n gem-will-paginate-devel
Version:       4.0.0
Release:       alt1
Summary:       Pagination library for Rails, Sinatra, Merb, DataMapper, and more development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета will_paginate
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(will_paginate) = 4.0.0
Requires:      gem(activerecord) >= 6.1.7.1
Requires:      gem(actionpack) >= 6.1.7.1
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(mocha) >= 1.11.2
Requires:      gem(sqlite3) >= 1.4.0
Requires:      gem(mysql2) >= 0.5.2
Requires:      gem(pg) >= 1.2
Conflicts:     gem(activerecord) >= 8
Conflicts:     gem(actionpack) >= 8
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(sqlite3) >= 2
Conflicts:     gem(mysql2) >= 0.6
Conflicts:     gem(pg) >= 2

%description   -n gem-will-paginate-devel
Pagination library for Rails, Sinatra, Merb, DataMapper, and more development
package.

will_paginate is a pagination library that integrates with Ruby on Rails,
Sinatra, Merb, DataMapper and Sequel.

%description   -n gem-will-paginate-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета will_paginate.


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

%files         -n gem-will-paginate-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-will-paginate-devel
%doc README.md


%changelog
* Tue Dec 12 2023 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt1
- ^ 3.3.0 -> 4.0.0

* Tue Dec 15 2020 Pavel Skrylev <majioa@altlinux.org> 3.3.0-alt1
- ^ 3.1.8 -> 3.3.0
- * policied name

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.8-alt1
- ^ 3.1.7 -> 3.1.8
- ! spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.7-alt1
- ^ 3.1.6 -> 3.1.7
- > Ruby Policy 2.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 3.1.6-alt1
- + initial gemified build for Sisyphus
