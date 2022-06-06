%define        gemname sidekiq

Name:          gem-sidekiq
Version:       6.4.1
Release:       alt1
Summary:       Simple, efficient background processing for Ruby
License:       LGPL-3.0
Group:         Development/Ruby
Url:           http://sidekiq.org
Vcs:           https://github.com/mperham/sidekiq.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(redis) >= 4.2.0
BuildRequires: gem(connection_pool) >= 2.2.2
BuildRequires: gem(rack) >= 2.0 gem(rack) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(redis) >= 4.2.0
Requires:      gem(connection_pool) >= 2.2.2
Requires:      gem(rack) >= 2.0 gem(rack) < 3
Provides:      gem(sidekiq) = 6.4.1


%description
Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.


%package       -n sidekiq
Version:       6.4.1
Release:       alt1
Summary:       Simple, efficient background processing for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sidekiq
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sidekiq) = 6.4.1

%description   -n sidekiq
Simple, efficient background processing for Ruby
executable(s).

Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.

%description   -n sidekiq -l ru_RU.UTF-8
Исполнямка для самоцвета sidekiq.


%package       -n gem-sidekiq-doc
Version:       6.4.1
Release:       alt1
Summary:       Simple, efficient background processing for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sidekiq
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sidekiq) = 6.4.1

%description   -n gem-sidekiq-doc
Simple, efficient background processing for Ruby documentation
files.

Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.

%description   -n gem-sidekiq-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sidekiq.


%package       -n gem-sidekiq-devel
Version:       6.4.1
Release:       alt1
Summary:       Simple, efficient background processing for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sidekiq
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sidekiq) = 6.4.1
Requires:      gem(rack) >= 2.0 gem(rack) < 3

%description   -n gem-sidekiq-devel
Simple, efficient background processing for Ruby development
package.

Sidekiq uses threads to handle many jobs at the same time in the same process.
It does not require Rails but will integrate tightly with Rails to make
background processing dead simple.

%description   -n gem-sidekiq-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sidekiq.


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

%files         -n sidekiq
%doc README.md
%_bindir/sidekiq
%_bindir/sidekiqmon

%files         -n gem-sidekiq-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sidekiq-devel
%doc README.md


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 6.4.1-alt1
- ^ 5.2.8 -> 6.4.1

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.8-alt1.1
- * gem deps for rack to ~> 2.0

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.8-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
