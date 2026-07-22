%define        _unpackaged_files_terminate_build 1
%def_disable    check
%def_enable    doc
%def_enable    devel
%define        gemname barsoom_utils

Name:          gem-barsoom-utils
Version:       0.2.0.75
Release:       alt1
Summary:       Various helpful utils
License:       MIT
Group:         Development/Ruby
Url:           https://dev.auctionet.com/
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(attr_extras) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(fixme) >= 0
BuildRequires: gem(honeybadger) >= 0
BuildRequires: gem(httparty) >= 0
BuildRequires: gem(lolcat) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(redis) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names barsoom_utils,barsoom-utils
Provides:      gem(barsoom_utils) = 0.2.0.75

%description
Various helpful utils


%if_enabled    doc
%package       -n gem-barsoom-utils-doc
Version:       0.2.0.75
Release:       alt1
Summary:       Various helpful utils documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета barsoom_utils
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(barsoom_utils) = 0.2.0.75

%description   -n gem-barsoom-utils-doc
Various helpful utils documentation files.

%description   -n gem-barsoom-utils-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета barsoom_utils.
%endif


%if_enabled    devel
%package       -n gem-barsoom-utils-devel
Version:       0.2.0.75
Release:       alt1
Summary:       Various helpful utils development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета barsoom_utils
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(barsoom_utils) = 0.2.0.75
Requires:      gem(attr_extras) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(fixme) >= 0
Requires:      gem(honeybadger) >= 0
Requires:      gem(httparty) >= 0
Requires:      gem(lolcat) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(redis) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-barsoom-utils-devel
Various helpful utils development package.

%description   -n gem-barsoom-utils-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета barsoom_utils.
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
%files         -n gem-barsoom-utils-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-barsoom-utils-devel
%doc README.md
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 0.2.0.75-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
