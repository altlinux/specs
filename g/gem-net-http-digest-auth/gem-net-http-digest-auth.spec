%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname net-http-digest_auth

Name:          gem-net-http-digest-auth
Version:       1.4.1
Release:       alt2.1
Summary:       An implementation of RFC 2617 Digest Access Authentication
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/drbrain/net-http-digest_auth
Vcs:           https://github.com/drbrain/net-http-digest_auth.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(hoe) >= 0
BuildRequires: gem(minitest) >= 5.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.0
%ruby_alias_names net-http-digest_auth,net-http-digest-auth
Requires:      ruby >= 1.8.7
Provides:      gem(net-http-digest_auth) = 1.4.1

%description
An implementation of RFC 2617 - Digest Access Authentication. At this time the
gem does not drop in to Net::HTTP and can be used for with other HTTP
clients.

In order to use net-http-digest_auth you'll need to perform some request
wrangling on your own. See the class documentation at Net::HTTP::DigestAuth for
an example.


%if_enabled    doc
%package       -n gem-net-http-digest-auth-doc
Version:       1.4.1
Release:       alt2.1
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
%endif


%if_enabled    devel
%package       -n gem-net-http-digest-auth-devel
Version:       1.4.1
Release:       alt2.1
Summary:       An implementation of RFC 2617 Digest Access Authentication development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-http-digest_auth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-http-digest_auth) = 1.4.1
Requires:      gem(hoe) >= 0
Requires:      gem(minitest) >= 5.0

%description   -n gem-net-http-digest-auth-devel
An implementation of RFC 2617 Digest Access Authentication development
package.

An implementation of RFC 2617 - Digest Access Authentication. At this time the
gem does not drop in to Net::HTTP and can be used for with other HTTP
clients.

In order to use net-http-digest_auth you'll need to perform some request
wrangling on your own. See the class documentation at Net::HTTP::DigestAuth for
an example.

%description   -n gem-net-http-digest-auth-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-http-digest_auth.
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
%doc History.txt README.txt
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-net-http-digest-auth-doc
%doc History.txt README.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-net-http-digest-auth-devel
%doc History.txt README.txt
%endif


%changelog
* Mon Aug 31 2026 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt2.1
- ! fixed dep to minitest gem

* Wed Oct 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt2
- ! fixed .gear place and spec

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1.1
- ! spec

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
