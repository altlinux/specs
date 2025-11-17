%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname zendesk_api

Name:          gem-zendesk-api
Version:       3.1.1
Release:       alt1
Summary:       Official Ruby Zendesk API Client
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://developer.zendesk.com/
Vcs:           https://github.com/zendesk/zendesk_api_client_rb.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(actionpack) >= 5.2.4.6
BuildRequires: gem(addressable) >= 2.8.0
BuildRequires: gem(base64) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(faraday) > 2.0.0
BuildRequires: gem(faraday-multipart) >= 0
BuildRequires: gem(hashie) >= 3.5.2
BuildRequires: gem(inflection) >= 0
BuildRequires: gem(json) >= 2.3.0
BuildRequires: gem(mini_mime) >= 0
BuildRequires: gem(multipart-post) >= 2.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rspec-core) >= 3.10.1
BuildRequires: gem(rspec-expectations) >= 3.10.1
BuildRequires: gem(rspec-mocks) >= 3.10.2
BuildRequires: gem(rspec-support) >= 3.10.2
BuildRequires: gem(scrub_rb) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(vcr) >= 6.0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(multipart-post) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-core) >= 4
BuildConflicts: gem(rspec-expectations) >= 4
BuildConflicts: gem(rspec-mocks) >= 4
BuildConflicts: gem(rspec-support) >= 4
BuildConflicts: gem(vcr) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rspec-support >= 3.10.2,rspec-support < 4
%ruby_use_gem_dependency rspec-core >= 3.10.1,rspec-core < 4
%ruby_use_gem_dependency rspec-expectations >= 3.10.1,rspec-expectations < 4
%ruby_use_gem_dependency rspec-mocks >= 3.10.2,rspec-mocks < 4
%ruby_alias_names zendesk_api,zendesk-api
Requires:      ruby >= 3.1
Requires:      rubygems >= 1.3.6
Requires:      gem(base64) >= 0
Requires:      gem(faraday) > 2.0.0
Requires:      gem(faraday-multipart) >= 0
Requires:      gem(hashie) >= 3.5.2
Requires:      gem(inflection) >= 0
Requires:      gem(mini_mime) >= 0
Requires:      gem(multipart-post) >= 2.0
Requires:      gem(standard) >= 0
Conflicts:     gem(multipart-post) >= 3
Obsoletes:     ruby-zendesk_api < %EVR
Provides:      ruby-zendesk_api = %EVR
Provides:      gem(zendesk_api) = 3.1.1

%description
Zendesk Sunshine is our open and flexible platform, built natively on AWS. You
can create unique customer experiences using our APIs and SDKs, connect data
sources across your technology stack, and build any app or automation you want,
using the languages you love.

This Ruby gem is a wrapper around Zendesk's REST API.


%if_enabled    doc
%package       -n gem-zendesk-api-doc
Version:       3.1.1
Release:       alt1
Summary:       Official Ruby Zendesk API Client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета zendesk_api
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(zendesk_api) = 3.1.1

%description   -n gem-zendesk-api-doc
Official Ruby Zendesk API Client documentation files.

Zendesk Sunshine is our open and flexible platform, built natively on AWS. You
can create unique customer experiences using our APIs and SDKs, connect data
sources across your technology stack, and build any app or automation you want,
using the languages you love.

This Ruby gem is a wrapper around Zendesk's REST API.

%description   -n gem-zendesk-api-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета zendesk_api.
%endif


%if_enabled    devel
%package       -n gem-zendesk-api-devel
Version:       3.1.1
Release:       alt1
Summary:       Official Ruby Zendesk API Client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета zendesk_api
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(zendesk_api) = 3.1.1

%description   -n gem-zendesk-api-devel
Official Ruby Zendesk API Client development package.

Zendesk Sunshine is our open and flexible platform, built natively on AWS. You
can create unique customer experiences using our APIs and SDKs, connect data
sources across your technology stack, and build any app or automation you want,
using the languages you love.

This Ruby gem is a wrapper around Zendesk's REST API.

%description   -n gem-zendesk-api-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета zendesk_api.
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
%doc LICENSE CHANGELOG.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-zendesk-api-doc
%doc LICENSE CHANGELOG.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-zendesk-api-devel
%doc LICENSE CHANGELOG.md README.md
%endif


%changelog
* Wed Nov 05 2025 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt1
- ^ 1.38.0.rc1.1 -> 3.1.1

* Thu Dec 15 2022 Pavel Skrylev <majioa@altlinux.org> 1.38.0.rc1.1-alt1
- ^ 1.31.0 -> 1.38.0.rc1.1

* Wed Oct 19 2022 Pavel Skrylev <majioa@altlinux.org> 1.31.0-alt1.1
- !fix build deps to novel gems

* Fri Jul 16 2021 Pavel Skrylev <majioa@altlinux.org> 1.31.0-alt1
- ^ Ruby Policy 2.0
- ^ 1.17.0 -> 1.31.0

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.16.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Nov 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.16.0-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.15.0-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 1.14.4-alt1
- Initial build for Sisyphus.
