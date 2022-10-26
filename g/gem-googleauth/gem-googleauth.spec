%define        gemname googleauth

Name:          gem-googleauth
Epoch:         1
Version:       1.2.0
Release:       alt1
Summary:       Google Auth Library for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/googleapis/google-auth-library-ruby
Vcs:           https://github.com/googleapis/google-auth-library-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(fakefs) >= 1.0 gem(fakefs) < 2
BuildRequires: gem(fakeredis) >= 0.5 gem(fakeredis) < 1
BuildRequires: gem(gems) >= 1.2 gem(gems) < 2
BuildRequires: gem(google-style) >= 1.26.0 gem(google-style) < 1.27
BuildRequires: gem(logging) >= 2.0 gem(logging) < 3
BuildRequires: gem(minitest) >= 5.14 gem(minitest) < 6
BuildRequires: gem(minitest-focus) >= 1.1 gem(minitest-focus) < 2
BuildRequires: gem(rack-test) >= 1.0 gem(rack-test) < 2
BuildRequires: gem(redcarpet) >= 3.0 gem(redcarpet) < 4
BuildRequires: gem(redis) >= 4.0 gem(redis) < 5
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(webmock) >= 3.8 gem(webmock) < 4
BuildRequires: gem(yard) >= 0.9 gem(yard) < 1
BuildRequires: gem(faraday) >= 0.17.3 gem(faraday) < 3.a
BuildRequires: gem(jwt) >= 1.4 gem(jwt) < 3
BuildRequires: gem(memoist) >= 0.16 gem(memoist) < 1
BuildRequires: gem(multi_json) >= 1.11 gem(multi_json) < 2
BuildRequires: gem(os) >= 0.9 gem(os) < 2.0
BuildRequires: gem(signet) >= 0.16 gem(signet) < 2.a
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(faraday) >= 0.17.3 gem(faraday) < 3.a
Requires:      gem(jwt) >= 1.4 gem(jwt) < 3
Requires:      gem(memoist) >= 0.16 gem(memoist) < 1
Requires:      gem(multi_json) >= 1.11 gem(multi_json) < 2
Requires:      gem(os) >= 0.9 gem(os) < 2.0
Requires:      gem(signet) >= 0.16 gem(signet) < 2.a
Obsoletes:     ruby-google-auth < %EVR
Provides:      ruby-google-auth = %EVR
Provides:      gem(googleauth) = 1.2.0


%description
Allows simple authorization for accessing Google APIs. Provide support for
Application Default Credentials, as described at
https://developers.google.com/accounts/docs/application-default-credentials


%package       -n gem-googleauth-doc
Version:       1.2.0
Release:       alt1
Summary:       Google Auth Library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета googleauth
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(googleauth) = 1.2.0

%description   -n gem-googleauth-doc
Google Auth Library for Ruby documentation files.

Allows simple authorization for accessing Google APIs. Provide support for
Application Default Credentials, as described at
https://developers.google.com/accounts/docs/application-default-credentials

%description   -n gem-googleauth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета googleauth.


%package       -n gem-googleauth-devel
Version:       1.2.0
Release:       alt1
Summary:       Google Auth Library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета googleauth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(googleauth) = 1.2.0
Requires:      gem(fakefs) >= 1.0 gem(fakefs) < 2
Requires:      gem(fakeredis) >= 0.5 gem(fakeredis) < 1
Requires:      gem(gems) >= 1.2 gem(gems) < 2
Requires:      gem(google-style) >= 1.26.0 gem(google-style) < 1.27
Requires:      gem(logging) >= 2.0 gem(logging) < 3
Requires:      gem(minitest) >= 5.14 gem(minitest) < 6
Requires:      gem(minitest-focus) >= 1.1 gem(minitest-focus) < 2
Requires:      gem(rack-test) >= 1.0 gem(rack-test) < 2
Requires:      gem(redcarpet) >= 3.0 gem(redcarpet) < 4
Requires:      gem(redis) >= 4.0 gem(redis) < 5
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(sinatra) >= 0
Requires:      gem(webmock) >= 3.8 gem(webmock) < 4
Requires:      gem(yard) >= 0.9 gem(yard) < 1

%description   -n gem-googleauth-devel
Google Auth Library for Ruby development package.

Allows simple authorization for accessing Google APIs. Provide support for
Application Default Credentials, as described at
https://developers.google.com/accounts/docs/application-default-credentials

%description   -n gem-googleauth-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета googleauth.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-googleauth-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-googleauth-devel
%doc README.md


%changelog
* Thu Oct 13 2022 Pavel Skrylev <majioa@altlinux.org> 1:1.2.0-alt1
- ^ 0.16.2 -> 1.2.0

* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 1:0.16.2-alt1
- ^ 0.8.1 -> 0.16.2

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 1:0.8.1-alt1
- > Ruby Policy 2.0
- ^ 0.6.7 -> 0.8.1

* Wed Nov 14 2018 Pavel Skrylev <majioa@altlinux.org> 1:0.6.7-alt1
- v 0.7.1 -> 0.6.7

* Mon Oct 29 2018 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt1
- ^ 0.7.0 -> 0.7.1

* Wed Oct 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- ^ 0.6.6 -> 0.7.0

* Tue Sep 04 2018 Pavel Skrylev <majioa@altlinux.org> 0.6.6-alt1
- ^ 0.6.0 -> 0.6.6

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus
