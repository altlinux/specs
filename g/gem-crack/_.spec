%define        gemname crack

Name:          gem-crack
Version:       0.4.4
Release:       alt1
Summary:       Really simple JSON and XML parsing, ripped from Merb and Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jnunemaker/crack
Vcs:           https://github.com/jnunemaker/crack.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(crack) = 0.4.4


%description
Really simple JSON and XML parsing, ripped from Merb and Rails. The XML parser
is ripped from Merb and the JSON parser is ripped from Rails. I take no credit,
just packaged them for all to enjoy and easily use.


%package       -n gem-crack-doc
Version:       0.4.4
Release:       alt1
Summary:       Really simple JSON and XML parsing, ripped from Merb and Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета crack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(crack) = 0.4.4

%description   -n gem-crack-doc
Really simple JSON and XML parsing, ripped from Merb and Rails documentation
files.

Really simple JSON and XML parsing, ripped from Merb and Rails. The XML parser
is ripped from Merb and the JSON parser is ripped from Rails. I take no credit,
just packaged them for all to enjoy and easily use.

%description   -n gem-crack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета crack.


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

%files         -n gem-crack-doc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.4-alt1
- ^ 0.4.3 -> 0.4.4

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
