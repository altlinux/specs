%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc

Name:          ruby-core-libraries
Version:       20240827
Release:       alt1
Summary:       This repository contains core Rubygems used by Ruby API clients
License:       Apache-2.0
Group:         Other
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(google-style) >= 1.30.0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(minitest-autotest) >= 1.1
BuildRequires: gem(minitest-focus) >= 1.4
BuildRequires: gem(minitest-rg) >= 5.3
BuildRequires: gem(redcarpet) >= 3.0
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(google-style) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-autotest) >= 2
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(minitest-rg) >= 6
BuildConflicts: gem(redcarpet) >= 4
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency google-style >= 1.31,google-style < 2
Requires:      gem(gapic) = 0.2.0
Requires:      gem(google-logging-utils) = 0.1.0

%description
This repository contains core Rubygems used by Ruby API clients.


%package       -n gem-gapic
Version:       0.2.0
Release:       alt1
Summary:       Core namespace for Google generated API client tools
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 3.0
Requires:      gem(gapic) >= 0
Requires:      gem(google-style) >= 1.30.0
Requires:      gem(minitest) >= 5.24
Requires:      gem(minitest-autotest) >= 1.1
Requires:      gem(minitest-focus) >= 1.4
Requires:      gem(minitest-rg) >= 5.3
Requires:      gem(redcarpet) >= 3.0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(google-style) >= 2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(minitest-rg) >= 6
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(yard) >= 1
Provides:      gem(gapic) = 0.2.0

%description   -n gem-gapic
Core namespace for Google generated API client tools.


%if_enabled    doc
%package       -n gem-gapic-doc
Version:       0.2.0
Release:       alt1
Summary:       Core namespace for Google generated API client tools documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gapic
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gapic) = 0.2.0

%description   -n gem-gapic-doc
Core namespace for Google generated API client tools documentation files.

%description   -n gem-gapic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gapic.
%endif


%if_enabled    devel
%package       -n gem-gapic-devel
Version:       0.2.0
Release:       alt1
Summary:       Core namespace for Google generated API client tools development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gapic
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic) = 0.2.0

%description   -n gem-gapic-devel
Core namespace for Google generated API client tools development package.

%description   -n gem-gapic-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gapic.
%endif


%package       -n google-logging-utils
Version:       0.1.0
Release:       alt1
Summary:       Utility classes for logging to Google Cloud Logging
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 3.0
Requires:      gem(google-logging-utils) >= 0
Requires:      gem(google-style) >= 1.30.0
Requires:      gem(minitest) >= 5.24
Requires:      gem(minitest-autotest) >= 1.1
Requires:      gem(minitest-focus) >= 1.4
Requires:      gem(minitest-rg) >= 5.3
Requires:      gem(redcarpet) >= 3.0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(google-style) >= 2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(minitest-rg) >= 6
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(yard) >= 1
Provides:      gem(google-logging-utils) = 0.1.0

%description   -n google-logging-utils
Utility classes for logging to Google Cloud Logging.


%if_enabled    doc
%package       -n gem-google-logging-utils-doc
Version:       0.1.0
Release:       alt1
Summary:       Utility classes for logging to Google Cloud Logging documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-logging-utils
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-logging-utils) = 0.1.0

%description   -n gem-google-logging-utils-doc
Utility classes for logging to Google Cloud Logging documentation files.

%description   -n gem-google-logging-utils-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-logging-utils.
%endif


%if_enabled    devel
%package       -n gem-google-logging-utils-devel
Version:       0.1.0
Release:       alt1
Summary:       Utility classes for logging to Google Cloud Logging development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-logging-utils
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-logging-utils) = 0.1.0

%description   -n gem-google-logging-utils-devel
Utility classes for logging to Google Cloud Logging development package.

%description   -n gem-google-logging-utils-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-logging-utils.
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

%files         -n gem-gapic
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemspecdir/gapic-0.2.0.gemspec
%ruby_gemslibdir/gapic-0.2.0

%if_enabled    doc
%files         -n gem-gapic-doc
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemsdocdir/gapic-0.2.0
%endif

%if_enabled    devel
%files         -n gem-gapic-devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%endif

%files         -n google-logging-utils
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemspecdir/google-logging-utils-0.1.0.gemspec
%ruby_gemslibdir/google-logging-utils-0.1.0

%if_enabled    doc
%files         -n gem-google-logging-utils-doc
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemsdocdir/google-logging-utils-0.1.0
%endif

%if_enabled    devel
%files         -n gem-google-logging-utils-devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%endif


%changelog
* Mon Nov 03 2025 Pavel Skrylev <majioa@altlinux.org> 20240827-alt1
- + packaged gem with Ruby Policy 2.0
