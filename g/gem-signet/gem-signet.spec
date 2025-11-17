%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname signet

Name:          gem-signet
Version:       0.21.0
Release:       alt1
Summary:       Signet is an OAuth 1.0 / OAuth 2.0 implementation
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/google/signet/
Vcs:           https://github.com/googleapis/signet.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(addressable) >= 2.8
BuildRequires: gem(faraday) >= 0.17.5
BuildRequires: gem(gems) >= 1.2
BuildRequires: gem(google-style) >= 1.31.0
BuildRequires: gem(hurley) >= 0
BuildRequires: gem(jwt) >= 1.5
BuildRequires: gem(kramdown) >= 1.5
BuildRequires: gem(launchy) >= 2.4
BuildRequires: gem(multi_json) >= 1.10
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(redcarpet) >= 3.0
BuildRequires: gem(rspec) >= 3.1
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(gems) >= 2
BuildConflicts: gem(google-style) >= 1.32
BuildConflicts: gem(jwt) >= 4.0
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(launchy) >= 3
BuildConflicts: gem(multi_json) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(redcarpet) >= 4
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      ruby >= 3.1
Requires:      rubygems >= 1.3.5
Requires:      gem(addressable) >= 2.8
Requires:      gem(faraday) >= 0.17.5
Requires:      gem(jwt) >= 1.5
Requires:      gem(multi_json) >= 1.10
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(jwt) >= 4.0
Conflicts:     gem(multi_json) >= 2
Obsoletes:     ruby-signet < %EVR
Provides:      ruby-signet = %EVR
Provides:      gem(signet) = 0.21.0

%description
Signet is an OAuth 1.0 / OAuth 2.0 implementation.


%if_enabled    doc
%package       -n gem-signet-doc
Version:       0.21.0
Release:       alt1
Summary:       Signet is an OAuth 1.0 / OAuth 2.0 implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета signet
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(signet) = 0.21.0

%description   -n gem-signet-doc
Signet is an OAuth 1.0 / OAuth 2.0 implementation documentation files.

%description   -n gem-signet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета signet.
%endif


%if_enabled    devel
%package       -n gem-signet-devel
Version:       0.21.0
Release:       alt1
Summary:       Signet is an OAuth 1.0 / OAuth 2.0 implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета signet
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(signet) = 0.21.0
Requires:      gem(addressable) >= 2.8
Requires:      gem(faraday) >= 0.17.5
Requires:      gem(gems) >= 1.2
Requires:      gem(google-style) >= 1.31.0
Requires:      gem(hurley) >= 0
Requires:      gem(jwt) >= 1.5
Requires:      gem(kramdown) >= 1.5
Requires:      gem(launchy) >= 2.4
Requires:      gem(multi_json) >= 1.10
Requires:      gem(rake) >= 13.0
Requires:      gem(redcarpet) >= 3.0
Requires:      gem(rspec) >= 3.1
Requires:      gem(yard) >= 0.9
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(gems) >= 2
Conflicts:     gem(google-style) >= 1.32
Conflicts:     gem(jwt) >= 4.0
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(launchy) >= 3
Conflicts:     gem(multi_json) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(rspec) >= 4

%description   -n gem-signet-devel
Signet is an OAuth 1.0 / OAuth 2.0 implementation development package.

%description   -n gem-signet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета signet.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-signet-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-signet-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%endif


%changelog
* Sat Nov 15 2025 Pavel Skrylev <majioa@altlinux.org> 0.21.0-alt1
- ^ 0.17.0 -> 0.21.0

* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.17.0-alt1
- ^ 0.16.1 -> 0.17.0

* Wed Mar 30 2022 Pavel Skrylev <majioa@altlinux.org> 0.16.1-alt1
- ^ 0.15.0 -> 0.16.1

* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.15.0-alt1
- ^ 0.11.0 -> 0.15.0

* Fri Oct 12 2018 Andrey Cherepanov <cas@altlinux.org> 0.11.0-alt1
- New version.

* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.10.0-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus
