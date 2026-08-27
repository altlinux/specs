%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname logger-application

Name:          gem-logger-application
Version:       0.0.2.35.1
Release:       alt0.1
Summary:       Add logging support to your application
License:       2-clause BSDL
Group:         Development/Ruby
Url:           https://github.com/ruby/logger-application
Vcs:           https://github.com/ruby/logger-application.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(mspec) >= 0
BuildRequires: gem(rake) >= 11.3
BuildRequires: gem(rspec) >= 2.14.1
BuildRequires: gem(test-unit) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(bundler) >= 0
Requires:      gem(mspec) >= 0
Requires:      gem(rake) >= 11.3
Requires:      gem(rspec) >= 2.14.1
Requires:      gem(test-unit) >= 0
Conflicts:     ruby >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Provides:      gem(logger-application) = 0.0.2.35.1

%ruby_use_gem_version logger-application:0.0.2.35.1

%description
Add logging support to your application.


%if_enabled    doc
%package       -n gem-logger-application-doc
Version:       0.0.2.35.1
Release:       alt0.1
Summary:       Add logging support to your application documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета logger-application
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(logger-application) = 0.0.2.35.1

%description   -n gem-logger-application-doc
Add logging support to your application documentation files.

%description   -n gem-logger-application-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета logger-application.
%endif


%if_enabled    devel
%package       -n gem-logger-application-devel
Version:       0.0.2.35.1
Release:       alt0.1
Summary:       Add logging support to your application development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета logger-application
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(logger-application) = 0.0.2.35.1

%description   -n gem-logger-application-devel
Add logging support to your application development package.

%description   -n gem-logger-application-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета logger-application.
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
%files         -n gem-logger-application-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-logger-application-devel
%doc README.md
%endif


%changelog
* Fri Aug 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.0.2.35.1-alt0.1
- + packaged gem with Ruby Policy 2.0 of version 0.0.2p35.1
- * define explicit dependencies
