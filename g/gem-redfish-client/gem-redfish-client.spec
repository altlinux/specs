%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname redfish_client

Name:          gem-redfish-client
Version:       0.6.0
Release:       alt1
Summary:       Simple Redfish client library
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/xlab-steampunk/redfish-client-ruby
Vcs:           https://github.com/xlab-steampunk/redfish-client-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(excon) >= 0.71
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 11.0
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(rubocop) >= 0.54.0
BuildRequires: gem(server_sent_events) >= 0.1
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(webmock) >= 3.4
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(excon) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(server_sent_events) >= 1
BuildConflicts: gem(webmock) >= 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names redfish_client,redfish-client
%ruby_ignore_names bare
Requires:      ruby >= 2.1
Requires:      gem(excon) >= 0.71
Requires:      gem(server_sent_events) >= 0.1
Conflicts:     gem(excon) >= 1
Conflicts:     gem(server_sent_events) >= 1
Provides:      redfish_client = %EVR
Provides:      gem(redfish_client) = 0.6.0

%description
This repository contains source code for redfish_client gem that can be used to
connect to Redfish services.


%if_enabled    doc
%package       -n gem-redfish-client-doc
Version:       0.6.0
Release:       alt1
Summary:       Simple Redfish client library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redfish_client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redfish_client) = 0.6.0

%description   -n gem-redfish-client-doc
Simple Redfish client library documentation files.

This repository contains source code for redfish_client gem that can be used to
connect to Redfish services.

%description   -n gem-redfish-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redfish_client.
%endif


%if_enabled    devel
%package       -n gem-redfish-client-devel
Version:       0.6.0
Release:       alt1
Summary:       Simple Redfish client library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redfish_client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redfish_client) = 0.6.0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 11.0
Requires:      gem(rspec) >= 3.7
Requires:      gem(rubocop) >= 0.54.0
Requires:      gem(simplecov) >= 0
Requires:      gem(webmock) >= 3.4
Requires:      gem(yard) >= 0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(webmock) >= 4

%description   -n gem-redfish-client-devel
Simple Redfish client library development package.

This repository contains source code for redfish_client gem that can be used to
connect to Redfish services.

%description   -n gem-redfish-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redfish_client.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-redfish-client-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-redfish-client-devel
%doc LICENSE README.md
%endif


%changelog
* Thu Jan 23 2025 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- ^ 0.5.4 -> 0.6.0

* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.5.4-alt1.1
- ! closes build deps under check condition

* Mon Nov 08 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.4-alt1
- + packaged gem with Ruby Policy 2.0
