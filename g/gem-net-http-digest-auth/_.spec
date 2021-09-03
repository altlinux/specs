%define        gemname net-http-digest_auth

Name:          gem-net-http-digest-auth
Version:       1.4.1
Release:       alt1.1
Summary:       An implementation of RFC 2617 Digest Access Authentication
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/drbrain/net-http-digest_auth
Vcs:           https://github.com/drbrain/net-http-digest_auth.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hoe) >= 3.15 gem(hoe) < 4
BuildRequires: gem(minitest) >= 5.8 gem(minitest) < 6
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.0,rdoc < 7
%ruby_alias_names net-http-digest_auth,net-http-digest-auth
Provides:      gem(net-http-digest_auth) = 1.4.1


%description
An implementation of RFC 2617 - Digest Access Authentication. At this time the
gem does not drop in to Net::HTTP and can be used for with other HTTP
clients.

In order to use net-http-digest_auth you'll need to perform some request
wrangling on your own. See the class documentation at Net::HTTP::DigestAuth for
an example.


%package       -n gem-net-http-digest-auth-doc
Version:       1.4.1
Release:       alt1.1
Summary:       An implementation of RFC 2617 Digest Access Authentication documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-http-digest_auth
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-http-digest_auth) = 1.4.1

%description   -n gem-net-http-digest-auth-doc
An implementation of RFC 2617 Digest Access Authentication documentation
files.

An implementation of RFC 2617 - Digest Access Authentication. At this time the
gem does not drop in to Net::HTTP and can be used for with other HTTP
clients.

In order to use net-http-digest_auth you'll need to perform some request
wrangling on your own. See the class documentation at Net::HTTP::DigestAuth for
an example.

%description   -n gem-net-http-digest-auth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-http-digest_auth.


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

%files         -n gem-net-http-digest-auth-doc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1.1
- ! spec

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
