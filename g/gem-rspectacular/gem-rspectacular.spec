%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rspectacular

Name:          gem-rspectacular
Version:       0.70.8
Release:       alt1
Summary:       RSpec Support And Matchers
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/jfelchner/rspectacular
Vcs:           https://github.com/jfelchner/rspectacular.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(awesome_print) >= 0
BuildRequires: gem(fuubar) >= 2.0
BuildRequires: gem(rspec) >= 3.1
BuildConflicts: gem(fuubar) >= 3
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(awesome_print) >= 0
Requires:      gem(fuubar) >= 2.0
Requires:      gem(rspec) >= 3.1
Conflicts:     gem(fuubar) >= 3
Conflicts:     gem(rspec) >= 4
Provides:      gem(rspectacular) = 0.70.8

%description
We rock some RSpec configurations and matchers like it ain't nobody's bidnezz.


%package       -n rspectacular
Version:       0.70.8
Release:       alt1
Summary:       RSpec Support And Matchers executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rspectacular
Group:         Other
BuildArch:     noarch

Requires:      gem(rspectacular) = 0.70.8
Requires:      gem(awesome_print) >= 0
Requires:      gem(fuubar) >= 2.0
Conflicts:     gem(fuubar) >= 3

%description   -n rspectacular
RSpec Support And Matchers executable(s).

We rock some RSpec configurations and matchers like it ain't nobody's bidnezz.

%description   -n rspectacular -l ru_RU.UTF-8
Исполнямка для самоцвета rspectacular.


%if_enabled    doc
%package       -n gem-rspectacular-doc
Version:       0.70.8
Release:       alt1
Summary:       RSpec Support And Matchers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspectacular
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspectacular) = 0.70.8

%description   -n gem-rspectacular-doc
RSpec Support And Matchers documentation files.

We rock some RSpec configurations and matchers like it ain't nobody's bidnezz.

%description   -n gem-rspectacular-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspectacular.
%endif


%if_enabled    devel
%package       -n gem-rspectacular-devel
Version:       0.70.8
Release:       alt1
Summary:       RSpec Support And Matchers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspectacular
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspectacular) = 0.70.8

%description   -n gem-rspectacular-devel
RSpec Support And Matchers development package.

We rock some RSpec configurations and matchers like it ain't nobody's bidnezz.

%description   -n gem-rspectacular-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspectacular.
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
%doc README.md LICENSE
%ruby_gemspec
%ruby_gemlibdir

%files         -n rspectacular
%doc README.md LICENSE
%_bindir/deploy
%_bindir/rspectacular_test_bootstrap

%if_enabled    doc
%files         -n gem-rspectacular-doc
%doc README.md LICENSE
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspectacular-devel
%doc README.md LICENSE
%endif


%changelog
* Fri Oct 10 2025 Pavel Skrylev <majioa@altlinux.org> 0.70.8-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
