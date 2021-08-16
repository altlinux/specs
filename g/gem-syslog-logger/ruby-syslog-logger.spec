%define        gemname syslog-logger

Name:          gem-syslog-logger
Version:       1.6.8
Release:       alt2
Summary:       An improved Logger replacement that logs to syslog. It is almost drop-in with a few caveats
License:       BSD-2-Clause or Ruby
Group:         Development/Ruby
Url:           https://github.com/ngmoco/syslog_logger
Vcs:           https://github.com/ngmoco/syslog_logger.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-syslog-logger < %EVR
Provides:      ruby-syslog-logger = %EVR
Provides:      gem(syslog-logger) = 1.6.8


%description
Logger::Syslog is a Logger replacement that logs to syslog. It is almost drop-in
with a few caveats. You can add Logger::Syslog to your Rails production
environment to aggregate logs between multiple machines.


%package       -n gem-syslog-logger-doc
Version:       1.6.8
Release:       alt2
Summary:       An improved Logger replacement that logs to syslog. It is almost drop-in with a few caveats documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета syslog-logger
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(syslog-logger) = 1.6.8

%description   -n gem-syslog-logger-doc
An improved Logger replacement that logs to syslog. It is almost drop-in with a
few caveats documentation files.

Logger::Syslog is a Logger replacement that logs to syslog. It is almost drop-in
with a few caveats. You can add Logger::Syslog to your Rails production
environment to aggregate logs between multiple machines.

%description   -n gem-syslog-logger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета syslog-logger.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-syslog-logger-doc
%ruby_gemdocdir


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 1.6.8-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Aug 19 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1
- Initial build for ALT Linux
- Disable tests
