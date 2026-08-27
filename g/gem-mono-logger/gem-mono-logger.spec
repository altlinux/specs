%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname mono_logger

Name:          gem-mono-logger
Version:       1.1.2
Release:       alt1
Summary:       A lock-free logger for Ruby 2.0
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/steveklabnik/mono_logger
Vcs:           https://github.com/steveklabnik/mono_logger.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(logger-application) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
%ruby_alias_names mono_logger,mono-logger
Requires:      gem(logger-application) >= 0
Obsoletes:     ruby-mono-logger < %EVR
Obsoletes:     ruby-mono_logger < %EVR
Provides:      ruby-mono-logger = %EVR
Provides:      ruby-mono_logger = %EVR
Provides:      gem(mono_logger) = 1.1.2

%description
A lock-free logger compatible with Ruby 2.0. Ruby does not allow you to request
a lock in a trap handler because that could deadlock, so Logger is not
sufficient.


%if_enabled    doc
%package       -n gem-mono-logger-doc
Version:       1.1.2
Release:       alt1
Summary:       A lock-free logger for Ruby 2.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mono_logger
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mono_logger) = 1.1.2

%description   -n gem-mono-logger-doc
A lock-free logger for Ruby 2.0 documentation files.

A lock-free logger compatible with Ruby 2.0. Ruby does not allow you to request
a lock in a trap handler because that could deadlock, so Logger is not
sufficient.

%description   -n gem-mono-logger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mono_logger.
%endif


%if_enabled    devel
%package       -n gem-mono-logger-devel
Version:       1.1.2
Release:       alt1
Summary:       A lock-free logger for Ruby 2.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mono_logger
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mono_logger) = 1.1.2
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 0
Conflicts:     gem(minitest) >= 7

%description   -n gem-mono-logger-devel
A lock-free logger for Ruby 2.0 development package.

A lock-free logger compatible with Ruby 2.0. Ruby does not allow you to request
a lock in a trap handler because that could deadlock, so Logger is not
sufficient.

%description   -n gem-mono-logger-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mono_logger.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-mono-logger-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mono-logger-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Fri Aug 21 2026 Pavel Skrylev <majioa@altlinux.org> 1.1.2-alt1
- ^ 1.1.1 -> 1.1.2

* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 1.1.0 -> 1.1.1
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
