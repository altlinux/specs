%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname logging

Name:          gem-logging
Version:       2.4.0
Release:       alt1
Summary:       A flexible logging library for use in Ruby programs based on the design of Java's log4j library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/TwP/logging
Vcs:           https://github.com/twp/logging.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bones) >= 3.9.0
BuildRequires: gem(bones-git) >= 1.3
BuildRequires: gem(little-plugger) >= 1.1
BuildRequires: gem(multi_json) >= 1.14
BuildRequires: gem(test-unit) >= 3.3
BuildConflicts: gem(bones) >= 3.10
BuildConflicts: gem(bones-git) >= 2
BuildConflicts: gem(little-plugger) >= 2
BuildConflicts: gem(multi_json) >= 2
BuildConflicts: gem(test-unit) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(little-plugger) >= 1.1
Requires:      gem(multi_json) >= 1.14
Conflicts:     gem(little-plugger) >= 2
Conflicts:     gem(multi_json) >= 2
Obsoletes:     ruby-logging < %EVR
Provides:      ruby-logging = %EVR
Provides:      gem(logging) = 2.4.0

%description
Logging is a flexible logging library for use in Ruby programs based on the
design of Java's log4j library. It features a hierarchical logging system,
custom level names, multiple output destinations per log event, custom
formatting, and more.


%if_enabled    doc
%package       -n gem-logging-doc
Version:       2.4.0
Release:       alt1
Summary:       A flexible logging library for use in Ruby programs based on the design of Java's log4j library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета logging
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(logging) = 2.4.0

%description   -n gem-logging-doc
A flexible logging library for use in Ruby programs based on the design of
Java's log4j library documentation files.

Logging is a flexible logging library for use in Ruby programs based on the
design of Java's log4j library. It features a hierarchical logging system,
custom level names, multiple output destinations per log event, custom
formatting, and more.

%description   -n gem-logging-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета logging.
%endif


%if_enabled    devel
%package       -n gem-logging-devel
Version:       2.4.0
Release:       alt1
Summary:       A flexible logging library for use in Ruby programs based on the design of Java's log4j library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета logging
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(logging) = 2.4.0
Requires:      gem(bones) >= 3.9.0
Requires:      gem(bones-git) >= 1.3
Requires:      gem(test-unit) >= 3.3
Conflicts:     gem(bones) >= 3.10
Conflicts:     gem(bones-git) >= 2
Conflicts:     gem(test-unit) >= 4

%description   -n gem-logging-devel
A flexible logging library for use in Ruby programs based on the design of
Java's log4j library development package.

Logging is a flexible logging library for use in Ruby programs based on the
design of Java's log4j library. It features a hierarchical logging system,
custom level names, multiple output destinations per log event, custom
formatting, and more.

%description   -n gem-logging-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета logging.
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
%doc History.txt LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-logging-doc
%doc History.txt LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-logging-devel
%doc History.txt LICENSE README.md
%endif


%changelog
* Tue Jan 28 2025 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- ^ 2.3.0 -> 2.4.0

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- ^ 2.2.2 -> 2.3.0
- ! spec

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.2-alt2.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.2-alt2
- used (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun May 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus
