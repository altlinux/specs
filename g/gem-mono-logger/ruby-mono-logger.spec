%define        gemname mono_logger

Name:          gem-mono-logger
Version:       1.1.1
Release:       alt1
Summary:       A lock-free logger for Ruby 2.0
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/steveklabnik/mono_logger
Vcs:           https://github.com/steveklabnik/mono_logger.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names mono_logger,mono-logger
Obsoletes:     ruby-mono-logger < %EVR
Provides:      ruby-mono-logger = %EVR
Provides:      ruby-mono_logger = %EVR
Provides:      gem(mono_logger) = 1.1.1


%description
A lock-free logger compatible with Ruby 2.0. Ruby does not allow you to request
a lock in a trap handler because that could deadlock, so Logger is not
sufficient.


%package       -n gem-mono-logger-doc
Version:       1.1.1
Release:       alt1
Summary:       A lock-free logger for Ruby 2.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mono_logger
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mono_logger) = 1.1.1

%description   -n gem-mono-logger-doc
A lock-free logger for Ruby 2.0 documentation files.

A lock-free logger compatible with Ruby 2.0. Ruby does not allow you to request
a lock in a trap handler because that could deadlock, so Logger is not
sufficient.


%description   -n gem-mono-logger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mono_logger.


%package       -n gem-mono-logger-devel
Version:       1.1.1
Release:       alt1
Summary:       A lock-free logger for Ruby 2.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mono_logger
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mono_logger) = 1.1.1
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6

%description   -n gem-mono-logger-devel
A lock-free logger for Ruby 2.0 development package.

A lock-free logger compatible with Ruby 2.0. Ruby does not allow you to request
a lock in a trap handler because that could deadlock, so Logger is not
sufficient.


%description   -n gem-mono-logger-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mono_logger.


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

%files         -n gem-mono-logger-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mono-logger-devel
%doc README.md


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 1.1.0 -> 1.1.1
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
