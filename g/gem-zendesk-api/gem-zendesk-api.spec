%define        gemname zendesk_api

Name:          gem-zendesk-api
Version:       1.38.0.rc1.1
Release:       alt1
Summary:       Official Ruby Zendesk API Client
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://developer.zendesk.com/
Vcs:           https://github.com/zendesk/zendesk_api_client_rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(mini_mime) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(addressable) >= 2.8.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(json) >= 2.3.0
BuildRequires: gem(scrub_rb) >= 0
BuildRequires: gem(rubocop) >= 0.64.0 gem(rubocop) < 2
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(vcr) >= 6.0 gem(vcr) < 7
BuildRequires: gem(rspec-support) >= 3.10.2 gem(rspec-support) < 4
BuildRequires: gem(rspec-core) >= 3.10.1 gem(rspec-core) < 4
BuildRequires: gem(rspec-expectations) >= 3.10.1 gem(rspec-expectations) < 4
BuildRequires: gem(rspec-mocks) >= 3.10.2 gem(rspec-mocks) < 4
BuildRequires: gem(rspec) >= 3.10.0 gem(rspec) < 4
BuildRequires: gem(actionpack) >= 5.2.4.6
BuildRequires: gem(bump) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(faraday) > 2.0.0
BuildRequires: gem(faraday-multipart) >= 0
BuildRequires: gem(hashie) >= 3.5.2 gem(hashie) < 6.0.0
BuildRequires: gem(inflection) >= 0
BuildRequires: gem(multipart-post) >= 2.0 gem(multipart-post) < 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rspec-support >= 3.10.2,rspec-support < 4
%ruby_use_gem_dependency rspec-core >= 3.10.1,rspec-core < 4
%ruby_use_gem_dependency rspec-expectations >= 3.10.1,rspec-expectations < 4
%ruby_use_gem_dependency rspec-mocks >= 3.10.2,rspec-mocks < 4
%ruby_alias_names zendesk_api,zendesk-api
Requires:      gem(mini_mime) >= 0
Requires:      gem(faraday) > 2.0.0
Requires:      gem(faraday-multipart) >= 0
Requires:      gem(hashie) >= 3.5.2 gem(hashie) < 6.0.0
Requires:      gem(inflection) >= 0
Requires:      gem(multipart-post) >= 2.0 gem(multipart-post) < 3
Obsoletes:     ruby-zendesk_api < %EVR
Provides:      ruby-zendesk_api = %EVR
Provides:      gem(zendesk_api) = 1.38.0.rc1.1

%ruby_use_gem_version zendesk_api:1.38.0.rc1.1

%description
Zendesk Sunshine is our open and flexible platform, built natively on AWS. You
can create unique customer experiences using our APIs and SDKs, connect data
sources across your technology stack, and build any app or automation you want,
using the languages you love.

This Ruby gem is a wrapper around Zendesk's REST API.


%package       -n gem-zendesk-api-doc
Version:       1.38.0.rc1.1
Release:       alt1
Summary:       Official Ruby Zendesk API Client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета zendesk_api
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(zendesk_api) = 1.38.0.rc1.1

%description   -n gem-zendesk-api-doc
Official Ruby Zendesk API Client documentation files.

Zendesk Sunshine is our open and flexible platform, built natively on AWS. You
can create unique customer experiences using our APIs and SDKs, connect data
sources across your technology stack, and build any app or automation you want,
using the languages you love.

This Ruby gem is a wrapper around Zendesk's REST API.

%description   -n gem-zendesk-api-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета zendesk_api.


%package       -n gem-zendesk-api-devel
Version:       1.38.0.rc1.1
Release:       alt1
Summary:       Official Ruby Zendesk API Client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета zendesk_api
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(zendesk_api) = 1.38.0.rc1.1
Requires:      gem(rake) >= 0
Requires:      gem(addressable) >= 2.8.0
Requires:      gem(yard) >= 0
Requires:      gem(json) >= 2.3.0
Requires:      gem(scrub_rb) >= 0
Requires:      gem(rubocop) >= 0.64.0 gem(rubocop) < 2
Requires:      gem(webmock) >= 0
Requires:      gem(vcr) >= 6.0 gem(vcr) < 7
Requires:      gem(rspec-support) >= 3.10.2 gem(rspec-support) < 4
Requires:      gem(rspec-core) >= 3.10.1 gem(rspec-core) < 4
Requires:      gem(rspec-expectations) >= 3.10.1 gem(rspec-expectations) < 4
Requires:      gem(rspec-mocks) >= 3.10.2 gem(rspec-mocks) < 4
Requires:      gem(rspec) >= 3.10.0 gem(rspec) < 4
Requires:      gem(actionpack) >= 5.2.4.6
Requires:      gem(bump) >= 0
Requires:      gem(byebug) >= 0

%description   -n gem-zendesk-api-devel
Official Ruby Zendesk API Client development package.

Zendesk Sunshine is our open and flexible platform, built natively on AWS. You
can create unique customer experiences using our APIs and SDKs, connect data
sources across your technology stack, and build any app or automation you want,
using the languages you love.

This Ruby gem is a wrapper around Zendesk's REST API.

%description   -n gem-zendesk-api-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета zendesk_api.


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

%files         -n gem-zendesk-api-doc
%ruby_gemdocdir

%files         -n gem-zendesk-api-devel


%changelog
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
