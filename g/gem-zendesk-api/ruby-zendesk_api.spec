%define        gemname zendesk_api

Name:          gem-zendesk-api
Version:       1.31.0
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
BuildRequires: gem(faraday) >= 0.9.0 gem(faraday) < 2.0.0
BuildRequires: gem(hashie) >= 3.5.2 gem(hashie) < 5.0.0
BuildRequires: gem(inflection) >= 0
BuildRequires: gem(multipart-post) >= 2.0 gem(multipart-post) < 3
BuildRequires: gem(mini_mime) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names train-test-fixture,train-local-rot13
Requires:      gem(faraday) >= 0.9.0 gem(faraday) < 2.0.0
Requires:      gem(hashie) >= 3.5.2 gem(hashie) < 5.0.0
Requires:      gem(inflection) >= 0
Requires:      gem(multipart-post) >= 2.0 gem(multipart-post) < 3
Requires:      gem(mini_mime) >= 0
Obsoletes:     ruby-zendesk_api < %EVR
Provides:      ruby-zendesk_api = %EVR
Provides:      gem(zendesk_api) = 1.31.0


%description
Zendesk Sunshine is our open and flexible platform, built natively on AWS. You
can create unique customer experiences using our APIs and SDKs, connect data
sources across your technology stack, and build any app or automation you want,
using the languages you love.

This Ruby gem is a wrapper around Zendesk's REST API.


%package       -n gem-zendesk-api-doc
Version:       1.31.0
Release:       alt1
Summary:       Official Ruby Zendesk API Client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета zendesk_api
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(zendesk_api) = 1.31.0

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
Version:       1.31.0
Release:       alt1
Summary:       Official Ruby Zendesk API Client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета zendesk_api
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(zendesk_api) = 1.31.0

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
