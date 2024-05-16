%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sucker_punch

Name:          gem-sucker-punch
Version:       3.2.0
Release:       alt1
Summary:       Asynchronous processing library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/brandonhilkert/sucker_punch
Vcs:           https://github.com/brandonhilkert/sucker_punch.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(concurrent-ruby) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(concurrent-ruby) >= 1.0
Conflicts:     gem(concurrent-ruby) >= 2
Provides:      gem(sucker_punch) = 3.2.0


%description
Sucker Punch is a Ruby asynchronous processing using concurrent-ruby, heavily
influenced by Sidekiq and girl_friday.


%if_enabled    doc
%package       -n gem-sucker-punch-doc
Version:       3.2.0
Release:       alt1
Summary:       Asynchronous processing library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sucker_punch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sucker_punch) = 3.2.0

%description   -n gem-sucker-punch-doc
Asynchronous processing library for Ruby documentation files.

Sucker Punch is a Ruby asynchronous processing using concurrent-ruby, heavily
influenced by Sidekiq and girl_friday.

%description   -n gem-sucker-punch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sucker_punch.
%endif


%if_enabled    devel
%package       -n gem-sucker-punch-devel
Version:       3.2.0
Release:       alt1
Summary:       Asynchronous processing library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sucker_punch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sucker_punch) = 3.2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(minitest) >= 0
Requires:      gem(pry) >= 0
Conflicts:     gem(rake) >= 14

%description   -n gem-sucker-punch-devel
Asynchronous processing library for Ruby development package.

Sucker Punch is a Ruby asynchronous processing using concurrent-ruby, heavily
influenced by Sidekiq and girl_friday.

%description   -n gem-sucker-punch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sucker_punch.
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
%files         -n gem-sucker-punch-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sucker-punch-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- + packaged gem with Ruby Policy 2.0
