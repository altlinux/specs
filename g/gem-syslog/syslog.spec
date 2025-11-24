%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname syslog

Name:          gem-syslog
Version:       0.3.0
Release:       alt1
Summary:       Ruby interface for the POSIX system logging facility
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/syslog
Vcs:           https://github.com/ruby/syslog.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(logger) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.5.0
Requires:      gem(logger) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(test-unit) >= 0
Provides:      gem(syslog) = 0.3.0

%description
Ruby interface for the POSIX system logging facility.


%if_enabled    doc
%package       -n gem-syslog-doc
Version:       0.3.0
Release:       alt1
Summary:       Ruby interface for the POSIX system logging facility documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета syslog
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(syslog) = 0.3.0

%description   -n gem-syslog-doc
Ruby interface for the POSIX system logging facility documentation files.

%description   -n gem-syslog-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета syslog.
%endif


%if_enabled    devel
%package       -n gem-syslog-devel
Version:       0.3.0
Release:       alt1
Summary:       Ruby interface for the POSIX system logging facility development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета syslog
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(syslog) = 0.3.0

%description   -n gem-syslog-devel
Ruby interface for the POSIX system logging facility development package.

%description   -n gem-syslog-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета syslog.
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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-syslog-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-syslog-devel
%doc COPYING README.md
%endif


%changelog
* Thu Nov 20 2025 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
