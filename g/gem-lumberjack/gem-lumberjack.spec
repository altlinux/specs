%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname lumberjack

Name:          gem-lumberjack
Version:       2.0.5
Release:       alt1
Summary:       Extension of Ruby's standard Logger for advanced, structured logging. Includes log entry attributes, context isolation, customizable formatters, flexible output devices, and testing tools
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bdurand/lumberjack
Vcs:           https://github.com/bdurand/lumberjack.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(irb) >= 0
BuildRequires: gem(logger) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.12
BuildRequires: gem(timecop) >= 0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7
Requires:      gem(logger) >= 0
Provides:      gem(lumberjack) = 2.0.5

%description
Extension of Ruby's standard Logger for advanced, structured logging. Includes
log entry attributes, context isolation, customizable formatters, flexible
output devices, and testing tools.


%if_enabled    doc
%package       -n gem-lumberjack-doc
Version:       2.0.5
Release:       alt1
Summary:       Extension of Ruby's standard Logger for advanced, structured logging. Includes log entry attributes, context isolation, customizable formatters, flexible output devices, and testing tools documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета lumberjack
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(lumberjack) = 2.0.5

%description   -n gem-lumberjack-doc
Extension of Ruby's standard Logger for advanced, structured logging. Includes
log entry attributes, context isolation, customizable formatters, flexible
output devices, and testing tools documentation files.

%description   -n gem-lumberjack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета lumberjack.
%endif


%if_enabled    devel
%package       -n gem-lumberjack-devel
Version:       2.0.5
Release:       alt1
Summary:       Extension of Ruby's standard Logger for advanced, structured logging. Includes log entry attributes, context isolation, customizable formatters, flexible output devices, and testing tools development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета lumberjack
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(lumberjack) = 2.0.5
Requires:      gem(bundler) >= 0
Requires:      gem(irb) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.12
Requires:      gem(timecop) >= 0
Conflicts:     gem(rspec) >= 4

%description   -n gem-lumberjack-devel
Extension of Ruby's standard Logger for advanced, structured logging. Includes
log entry attributes, context isolation, customizable formatters, flexible
output devices, and testing tools development package.

%description   -n gem-lumberjack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета lumberjack.
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
%doc CHANGELOG.md MIT_LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-lumberjack-doc
%doc CHANGELOG.md MIT_LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-lumberjack-devel
%doc CHANGELOG.md MIT_LICENSE.txt README.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 2.0.5-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
