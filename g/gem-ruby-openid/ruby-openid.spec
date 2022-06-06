%define        gemname ruby-openid

Name:          gem-ruby-openid
Version:       2.9.2
Release:       alt1.1
Summary:       OpenID library for Ruby
License:       Ruby or Apache Software License 2.0
Group:         Development/Ruby
Url:           https://github.com/openid/ruby-openid
Vcs:           https://github.com/openid/ruby-openid.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names %gemname,openid
Obsoletes:     ruby-openid
Provides:      ruby-openid
Provides:      gem(ruby-openid) = 2.9.2


%description
A Ruby library for verifying and serving OpenID identities.

* Easy to use API for verifying OpenID identites - OpenID::Consumer
* Support for serving OpenID identites - OpenID::Server
* Does not depend on underlying web framework
* Supports multiple storage mechanisms (Filesystem, ActiveRecord, Memory)
* Example code to help you get started, including:
  + Ruby on Rails based consumer and server
  + OpenIDLoginGenerator for quickly getting creating a rails app that uses
    OpenID for authentication
  + ActiveRecordOpenIDStore plugin
* Comprehensive test suite
* Supports both OpenID 1 and OpenID 2 transparently


%package       -n gem-ruby-openid-doc
Version:       2.9.2
Release:       alt1.1
Summary:       OpenID library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-openid
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-openid) = 2.9.2

%description   -n gem-ruby-openid-doc
OpenID library for Ruby documentation files.

A Ruby library for verifying and serving OpenID identities.

* Easy to use API for verifying OpenID identites - OpenID::Consumer
* Support for serving OpenID identites - OpenID::Server
* Does not depend on underlying web framework
* Supports multiple storage mechanisms (Filesystem, ActiveRecord, Memory)
* Example code to help you get started, including:
  + Ruby on Rails based consumer and server
  + OpenIDLoginGenerator for quickly getting creating a rails app that uses
    OpenID for authentication
  + ActiveRecordOpenIDStore plugin
* Comprehensive test suite
* Supports both OpenID 1 and OpenID 2 transparently

%description   -n gem-ruby-openid-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-openid.


%package       -n gem-openid-devel
Version:       2.9.2
Release:       alt1.1
Summary:       OpenID library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-openid
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-openid) = 2.9.2
Requires:      gem(minitest) >= 5

%description   -n gem-openid-devel
OpenID library for Ruby development package.

A Ruby library for verifying and serving OpenID identities.

* Easy to use API for verifying OpenID identites - OpenID::Consumer
* Support for serving OpenID identites - OpenID::Server
* Does not depend on underlying web framework
* Supports multiple storage mechanisms (Filesystem, ActiveRecord, Memory)
* Example code to help you get started, including:
  + Ruby on Rails based consumer and server
  + OpenIDLoginGenerator for quickly getting creating a rails app that uses
    OpenID for authentication
  + ActiveRecordOpenIDStore plugin
* Comprehensive test suite
* Supports both OpenID 1 and OpenID 2 transparently

%description   -n gem-openid-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-openid.


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

%files         -n gem-ruby-openid-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-openid-devel
%doc README.md


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.9.2-alt1.1
- ! spec

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.9.2-alt1
- updated (^) 2.9.1 -> 2.9.2
- fixed (!) spec

* Wed Sep 18 2019 Pavel Skrylev <majioa@altlinux.org> 2.9.1-alt1
- used (>) Ruby Policy 2.0
- updated (^) 2.8.0 -> 2.9.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- Initial build for Sisyphus
