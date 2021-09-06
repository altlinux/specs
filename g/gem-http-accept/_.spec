%define        gemname http-accept

Name:          gem-http-accept
Version:       2.1.1
Release:       alt1
Summary:       Parse Accept and Accept-Language HTTP headers in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/http-accept
Vcs:           https://github.com/socketry/http-accept.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(covered) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(http-accept) = 2.1.1

%description
Provides a robust set of parsers for dealing with HTTP Accept, Accept-Language,
Accept-Encoding, Accept-Charset headers.


%package       -n gem-http-accept-doc
Version:       2.1.1
Release:       alt1
Summary:       Parse Accept and Accept-Language HTTP headers in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета http-accept
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(http-accept) = 2.1.1

%description   -n gem-http-accept-doc
Parse Accept and Accept-Language HTTP headers in Ruby documentation files.

Provides a robust set of parsers for dealing with HTTP Accept, Accept-Language,
Accept-Encoding, Accept-Charset headers.

%description   -n gem-http-accept-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета http-accept.


%package       -n gem-http-accept-devel
Version:       2.1.1
Release:       alt1
Summary:       Parse Accept and Accept-Language HTTP headers in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета http-accept
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(http-accept) = 2.1.1
Requires:      gem(covered) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-http-accept-devel
Parse Accept and Accept-Language HTTP headers in Ruby development package.

Provides a robust set of parsers for dealing with HTTP Accept, Accept-Language,
Accept-Encoding, Accept-Charset headers.

%description   -n gem-http-accept-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета http-accept.


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

%files         -n gem-http-accept-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-http-accept-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- ^ 1.7.0 -> 2.1.1

* Wed Sep 25 2019 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
