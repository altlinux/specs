%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname excon

Name:          gem-excon
Version:       1.7.1
Release:       alt1
Summary:       Usable, fast, simple HTTP 1.1 for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/excon/excon
Vcs:           https://github.com/excon/excon.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(eventmachine) >= 1.0.4
BuildRequires: gem(json) >= 1.8.5
BuildRequires: gem(logger) >= 0
BuildRequires: gem(open4) >= 0
BuildRequires: gem(puma) >= 0
BuildRequires: gem(rack) >= 2.2.3
BuildRequires: gem(rackup) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rspec) >= 3.5.0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(shindo) >= 0
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(sinatra-contrib) >= 0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(webrick) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.3.0
Requires:      gem(logger) >= 0
Obsoletes:     ruby-excon < %EVR
Provides:      ruby-excon = %EVR
Provides:      gem(excon) = 1.7.1

%description
Usable, fast, simple Ruby HTTP 1.1

Excon was designed to be simple, fast and performant. It works great as a
general HTTP(s) client and is particularly well suited to usage in API clients.


%if_enabled    doc
%package       -n gem-excon-doc
Version:       1.7.1
Release:       alt1
Summary:       Usable, fast, simple HTTP 1.1 for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета excon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(excon) = 1.7.1

%description   -n gem-excon-doc
Usable, fast, simple HTTP 1.1 for Ruby documentation files.

Usable, fast, simple Ruby HTTP 1.1

Excon was designed to be simple, fast and performant. It works great as a
general HTTP(s) client and is particularly well suited to usage in API clients.

%description   -n gem-excon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета excon.
%endif


%if_enabled    devel
%package       -n gem-excon-devel
Version:       1.7.1
Release:       alt1
Summary:       Usable, fast, simple HTTP 1.1 for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета excon
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(excon) = 1.7.1
Requires:      gem(activesupport) >= 0
Requires:      gem(eventmachine) >= 1.0.4
Requires:      gem(json) >= 1.8.5
Requires:      gem(open4) >= 0
Requires:      gem(puma) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rspec) >= 3.5.0
Requires:      gem(shindo) >= 0
Requires:      gem(sinatra) >= 0
Requires:      gem(sinatra-contrib) >= 0
Requires:      gem(timecop) >= 0
Requires:      gem(webrick) >= 0

%description   -n gem-excon-devel
Usable, fast, simple HTTP 1.1 for Ruby development package.

Usable, fast, simple Ruby HTTP 1.1

Excon was designed to be simple, fast and performant. It works great as a
general HTTP(s) client and is particularly well suited to usage in API clients.

%description   -n gem-excon-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета excon.
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
%doc CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md changelog.txt
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-excon-doc
%doc CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md changelog.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-excon-devel
%doc CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md changelog.txt
%endif


%changelog
* Wed Sep 23 2026 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- ^ 0.105.0 -> 1.7.1

* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.105.0-alt1
- ^ 0.72.0 -> 0.105.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.72.0-alt1
- updated (^) 0.66.0 -> 0.72.0
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.66.0-alt1
- updated (^) 0.62.0 -> 0.66.0
- used (>) Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.62.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.62.0-alt1
- Initial build for Sisyphus
