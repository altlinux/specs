%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname http-accept

Name:          gem-http-accept
Version:       2.2.1
Release:       alt1
Summary:       Parse Accept and Accept-Language HTTP headers in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/http-accept
Vcs:           https://github.com/socketry/http-accept.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.0
Provides:      gem(http-accept) = 2.2.1

%description
Provides a robust set of parsers for dealing with HTTP Accept, Accept-Language,
Accept-Encoding, Accept-Charset headers.


%if_enabled    doc
%package       -n gem-http-accept-doc
Version:       2.2.1
Release:       alt1
Summary:       Parse Accept and Accept-Language HTTP headers in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета http-accept
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(http-accept) = 2.2.1

%description   -n gem-http-accept-doc
Parse Accept and Accept-Language HTTP headers in Ruby documentation
files.

Provides a robust set of parsers for dealing with HTTP Accept, Accept-Language,
Accept-Encoding, Accept-Charset headers.

%description   -n gem-http-accept-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета http-accept.
%endif


%if_enabled    devel
%package       -n gem-http-accept-devel
Version:       2.2.1
Release:       alt1
Summary:       Parse Accept and Accept-Language HTTP headers in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета http-accept
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(http-accept) = 2.2.1

%description   -n gem-http-accept-devel
Parse Accept and Accept-Language HTTP headers in Ruby development
package.

Provides a robust set of parsers for dealing with HTTP Accept, Accept-Language,
Accept-Encoding, Accept-Charset headers.

%description   -n gem-http-accept-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета http-accept.
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
%doc license.md readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-http-accept-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-http-accept-devel
%doc license.md readme.md
%endif


%changelog
* Sun Aug 16 2026 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- ^ 2.1.1 -> 2.2.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- ^ 1.7.0 -> 2.1.1

* Wed Sep 25 2019 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
