%define        gemname logging-journald

Name:          gem-logging-journald
Version:       2.1.0.1
Release:       alt0.1
Summary:       Plugin for logging gem providing journald appender
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lzap/logging-journald
Vcs:           https://github.com/lzap/logging-journald.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(journald-logger) >= 3.0 gem(journald-logger) < 4
BuildRequires: gem(logging) >= 0
BuildRequires: gem(rake) >= 11.0 gem(rake) < 14
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(test-unit) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_version logging-journald:2.1.0.1
Requires:      gem(journald-logger) >= 3.0 gem(journald-logger) < 4
Requires:      gem(logging) >= 0
Provides:      gem(logging-journald) = 2.1.0.1


%description
Logging Journald is a plugin for logging gem - the flexible logging library for
use in Ruby programs. It supports logging to system journal via journald-logger
and journald-native gems.


%package       -n gem-logging-journald-doc
Version:       2.1.0.1
Release:       alt0.1
Summary:       Plugin for logging gem providing journald appender documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета logging-journald
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(logging-journald) = 2.1.0.1

%description   -n gem-logging-journald-doc
Plugin for logging gem providing journald appender documentation files.

Logging Journald is a plugin for logging gem - the flexible logging library for
use in Ruby programs. It supports logging to system journal via journald-logger
and journald-native gems.

%description   -n gem-logging-journald-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета logging-journald.


%package       -n gem-logging-journald-devel
Version:       2.1.0.1
Release:       alt0.1
Summary:       Plugin for logging gem providing journald appender development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета logging-journald
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(logging-journald) = 2.1.0.1
Requires:      gem(rake) >= 11.0 gem(rake) < 14
Requires:      gem(bundler) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-logging-journald-devel
Plugin for logging gem providing journald appender development package.

Logging Journald is a plugin for logging gem - the flexible logging library for
use in Ruby programs. It supports logging to system journal via journald-logger
and journald-native gems.

%description   -n gem-logging-journald-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета logging-journald.


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

%files         -n gem-logging-journald-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-logging-journald-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.0.1-alt0.1
- ^ 2.0.3 -> 2.1.0[.1]

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.3-alt1.1
- ! spec according to changelog rules

* Wed Aug 21 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.3-alt1
- + packaged gem with usage Ruby Policy 2.0
