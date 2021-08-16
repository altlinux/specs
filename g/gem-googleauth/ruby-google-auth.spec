%define        gemname googleauth

Name:          gem-googleauth
Epoch:         1
Version:       0.16.2
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
BuildRequires: gem(faraday) >= 0.17.3 gem(faraday) < 2.0
BuildRequires: gem(jwt) >= 1.4 gem(jwt) < 3.0
BuildRequires: gem(memoist) >= 0.16 gem(memoist) < 1
BuildRequires: gem(multi_json) >= 1.11 gem(multi_json) < 2
BuildRequires: gem(os) >= 0.9 gem(os) < 2.0
BuildRequires: gem(signet) >= 0.14 gem(signet) < 1
BuildRequires: gem(yard) >= 0.9 gem(yard) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names googleauth,google-auth
Requires:      gem(faraday) >= 0.17.3 gem(faraday) < 2.0
Requires:      gem(jwt) >= 1.4 gem(jwt) < 3.0
Requires:      gem(memoist) >= 0.16 gem(memoist) < 1
Requires:      gem(multi_json) >= 1.11 gem(multi_json) < 2
Requires:      gem(os) >= 0.9 gem(os) < 2.0
Requires:      gem(signet) >= 0.14 gem(signet) < 1
Obsoletes:     ruby-google-auth < %EVR
Provides:      ruby-google-auth = %EVR
Provides:      gem(googleauth) = 0.16.2


%description
Allows simple authorization for accessing Google APIs. Provide support for
Application Default Credentials, as described at
https://developers.google.com/accounts/docs/application-default-credentials


%package       -n gem-googleauth-doc
Version:       0.16.2
Release:       alt1
Summary:       Google Auth Library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета googleauth
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(googleauth) = 0.16.2

%description   -n gem-googleauth-doc
Google Auth Library for Ruby documentation files.

Allows simple authorization for accessing Google APIs. Provide support for
Application Default Credentials, as described at
https://developers.google.com/accounts/docs/application-default-credentials

%description   -n gem-googleauth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета googleauth.


%package       -n gem-googleauth-devel
Version:       0.16.2
Release:       alt1
Summary:       Google Auth Library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета googleauth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(googleauth) = 0.16.2
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
