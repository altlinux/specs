%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname googleauth

Name:          gem-googleauth
Epoch:         1
Version:       1.15.1
Release:       alt1
Summary:       Google Auth Library for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/googleapis/google-auth-library-ruby
Vcs:           https://github.com/googleapis/google-auth-library-ruby.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(fakefs) >= 1.0
BuildRequires: gem(fakeredis) >= 0.5
BuildRequires: gem(faraday) >= 1.0
BuildRequires: gem(gems) >= 1.2
BuildRequires: gem(google-cloud-env) >= 2.2
BuildRequires: gem(google-logging-utils) >= 0.1
BuildRequires: gem(google-style) >= 1.30.1
BuildRequires: gem(jwt) >= 1.4
BuildRequires: gem(logging) >= 2.0
BuildRequires: gem(minitest) >= 5.14
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(multi_json) >= 1.11
BuildRequires: gem(os) >= 0.9
BuildRequires: gem(rack-test) >= 2.0
BuildRequires: gem(redcarpet) >= 3.0
BuildRequires: gem(redis) >= 4.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(signet) >= 0.16
BuildRequires: gem(webmock) >= 3.8
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(fakefs) >= 4
BuildConflicts: gem(fakeredis) >= 1
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(gems) >= 2
BuildConflicts: gem(google-cloud-env) >= 3
BuildConflicts: gem(google-logging-utils) >= 1
BuildConflicts: gem(google-style) >= 2
BuildConflicts: gem(jwt) >= 4.0
BuildConflicts: gem(logging) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(multi_json) >= 2
BuildConflicts: gem(os) >= 2.0
BuildConflicts: gem(rack-test) >= 3
BuildConflicts: gem(redcarpet) >= 4
BuildConflicts: gem(redis) >= 6
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(signet) >= 2
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency google-style >= 1.31,google-style < 2
Requires:      ruby >= 3.0
Requires:      gem(fakefs) >= 1.0
Requires:      gem(fakeredis) >= 0.5
Requires:      gem(faraday) >= 1.0
Requires:      gem(gems) >= 1.2
Requires:      gem(google-cloud-env) >= 2.2
Requires:      gem(google-logging-utils) >= 0.1
Requires:      gem(google-style) >= 1.30.1
Requires:      gem(jwt) >= 1.4
Requires:      gem(logging) >= 2.0
Requires:      gem(minitest) >= 5.14
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(multi_json) >= 1.11
Requires:      gem(os) >= 0.9
Requires:      gem(rack-test) >= 2.0
Requires:      gem(redcarpet) >= 3.0
Requires:      gem(redis) >= 4.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(signet) >= 0.16
Requires:      gem(webmock) >= 3.8
Requires:      gem(yard) >= 0.9
Conflicts:     gem(fakefs) >= 4
Conflicts:     gem(fakeredis) >= 1
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(gems) >= 2
Conflicts:     gem(google-cloud-env) >= 3
Conflicts:     gem(google-logging-utils) >= 1
Conflicts:     gem(google-style) >= 2
Conflicts:     gem(jwt) >= 4.0
Conflicts:     gem(logging) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(multi_json) >= 2
Conflicts:     gem(os) >= 2.0
Conflicts:     gem(rack-test) >= 3
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(redis) >= 6
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(signet) >= 2
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(yard) >= 1
Provides:      gem(googleauth) = 1.15.1

%description
Implements simple authorization for accessing Google APIs, and provides support
for Application Default Credentials.


%if_enabled    doc
%package       -n gem-googleauth-doc
Version:       1.15.1
Release:       alt1
Summary:       Google Auth Library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета googleauth
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(googleauth) = 1.15.1

%description   -n gem-googleauth-doc
Google Auth Library for Ruby documentation files.

Implements simple authorization for accessing Google APIs, and provides support
for Application Default Credentials.

%description   -n gem-googleauth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета googleauth.
%endif


%if_enabled    devel
%package       -n gem-googleauth-devel
Version:       1.15.1
Release:       alt1
Summary:       Google Auth Library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета googleauth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(googleauth) = 1.15.1
Requires:      gem(fakefs) >= 1.0
Requires:      gem(fakeredis) >= 0.5
Requires:      gem(faraday) >= 1.0
Requires:      gem(gems) >= 1.2
Requires:      gem(google-cloud-env) >= 2.2
Requires:      gem(google-logging-utils) >= 0.1
Requires:      gem(google-style) >= 1.30.1
Requires:      gem(jwt) >= 1.4
Requires:      gem(logging) >= 2.0
Requires:      gem(minitest) >= 5.14
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(multi_json) >= 1.11
Requires:      gem(os) >= 0.9
Requires:      gem(rack-test) >= 2.0
Requires:      gem(redcarpet) >= 3.0
Requires:      gem(redis) >= 4.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(signet) >= 0.16
Requires:      gem(webmock) >= 3.8
Requires:      gem(yard) >= 0.9
Conflicts:     gem(fakefs) >= 4
Conflicts:     gem(fakeredis) >= 1
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(gems) >= 2
Conflicts:     gem(google-cloud-env) >= 3
Conflicts:     gem(google-logging-utils) >= 1
Conflicts:     gem(google-style) >= 2
Conflicts:     gem(jwt) >= 4.0
Conflicts:     gem(logging) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(multi_json) >= 2
Conflicts:     gem(os) >= 2.0
Conflicts:     gem(rack-test) >= 3
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(redis) >= 6
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(signet) >= 2
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-googleauth-devel
Google Auth Library for Ruby development package.

Implements simple authorization for accessing Google APIs, and provides support
for Application Default Credentials.

%description   -n gem-googleauth-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета googleauth.
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
%files         -n gem-googleauth-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-googleauth-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%endif


%changelog
* Sat Nov 01 2025 Pavel Skrylev <majioa@altlinux.org> 1:1.15.1-alt1
- ^ 1.4.0 -> 1.15.1

* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 1:1.4.0-alt1
- ^ 1.2.0 -> 1.4.0

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
