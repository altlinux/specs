%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname logger

Name:          gem-logger
Version:       1.7.0
Release:       alt1
Summary:       Provides a simple logging utility for outputting messages
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/logger
Vcs:           https://github.com/ruby/logger.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.5.0
Provides:      gem(logger) = 1.7.0

%description
Provides a simple logging utility for outputting messages.


%if_enabled    doc
%package       -n gem-logger-doc
Version:       1.7.0
Release:       alt1
Summary:       Provides a simple logging utility for outputting messages documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета logger
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(logger) = 1.7.0

%description   -n gem-logger-doc
Provides a simple logging utility for outputting messages documentation files.

%description   -n gem-logger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета logger.
%endif


%if_enabled    devel
%package       -n gem-logger-devel
Version:       1.7.0
Release:       alt1
Summary:       Provides a simple logging utility for outputting messages development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета logger
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(logger) = 1.7.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-logger-devel
Provides a simple logging utility for outputting messages development package.

%description   -n gem-logger-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета logger.
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
%doc COPYING README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-logger-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-logger-devel
%doc COPYING README.md
%endif


%changelog
* Tue Oct 21 2025 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
