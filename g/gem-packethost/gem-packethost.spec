%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname packethost

Name:          gem-packethost
Version:       0.0.8.57
Release:       alt0.1
Summary:       A Ruby client for the Packet API
License:       GPLv2
Group:         Development/Ruby
Url:           https://www.packet.net
Vcs:           https://github.com/packethost/packet-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(activesupport) > 4.2
BuildRequires: gem(faraday) >= 0.9.0
BuildRequires: gem(faraday_middleware) >= 0.9.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rdoc) > 4
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(rubocop) >= 0.66
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sinatra) > 1.4
BuildRequires: gem(webmock) > 1.20
BuildConflicts: gem(activesupport) >= 8
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(sinatra) >= 5
BuildConflicts: gem(webmock) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency activesupport >= 7.1,activesupport < 8
%ruby_use_gem_dependency sinatra >= 4.0,sinatra < 5
Requires:      gem(activesupport) > 4.2
Requires:      gem(faraday) >= 0.9.0
Requires:      gem(faraday_middleware) >= 0.9.0
Conflicts:     gem(activesupport) >= 8
Provides:      gem(packethost) = 0.0.8.57

%ruby_use_gem_version packethost:0.0.8.57

%description
A Ruby client for the Packet API.


%if_enabled    doc
%package       -n gem-packethost-doc
Version:       0.0.8.57
Release:       alt0.1
Summary:       A Ruby client for the Packet API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета packethost
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(packethost) = 0.0.8.57

%description   -n gem-packethost-doc
A Ruby client for the Packet API documentation files.

%description   -n gem-packethost-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета packethost.
%endif


%if_enabled    devel
%package       -n gem-packethost-devel
Version:       0.0.8.57
Release:       alt0.1
Summary:       A Ruby client for the Packet API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета packethost
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(packethost) = 0.0.8.57
Requires:      gem(activesupport) > 4.2
Requires:      gem(bundler) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rdoc) > 4
Requires:      gem(rspec) >= 3
Requires:      gem(rubocop) >= 0.66
Requires:      gem(simplecov) >= 0
Requires:      gem(sinatra) > 1.4
Requires:      gem(webmock) > 1.20
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(sinatra) >= 5
Conflicts:     gem(webmock) >= 4

%description   -n gem-packethost-devel
A Ruby client for the Packet API development package.

%description   -n gem-packethost-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета packethost.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-packethost-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-packethost-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.0.8.57-alt0.1
- ^ 0.0.8[1] -> 0.0.8p57
- * define explicit dependencies

* Thu Dec 17 2020 Pavel Skrylev <majioa@altlinux.org> 0.0.8.1-alt0.1
- ^ 0.0.8 -> 0.0.8[.1]

* Tue Mar 19 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.8-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
