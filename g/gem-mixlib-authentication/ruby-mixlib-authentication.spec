%define        gemname mixlib-authentication

Name:          gem-mixlib-authentication
Version:       3.0.11
Release:       alt1
Summary:       AuthN signing and verification. Appears in both the client and server
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-authentication
Vcs:           https://github.com/chef/mixlib-authentication.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-mixlib-authentication < %EVR
Provides:      ruby-mixlib-authentication = %EVR
Provides:      gem(mixlib-authentication) = 3.0.11


%description
Mixlib::Authentication provides a class-based header signing authentication
object, like the one used in Chef.


%package       -n gem-mixlib-authentication-doc
Version:       3.0.11
Release:       alt1
Summary:       AuthN signing and verification. Appears in both the client and server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mixlib-authentication
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mixlib-authentication) = 3.0.11

%description   -n gem-mixlib-authentication-doc
AuthN signing and verification. Appears in both the client and server
documentation files.

Mixlib::Authentication provides a class-based header signing authentication
object, like the one used in Chef.

%description   -n gem-mixlib-authentication-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mixlib-authentication.


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

%files         -n gem-mixlib-authentication-doc
%ruby_gemdocdir


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.11-alt1
- ^ 2.1.4 -> 3.0.11

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.4-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux
