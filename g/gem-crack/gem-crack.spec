%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname crack

Name:          gem-crack
Version:       1.0.1
Release:       alt1
Summary:       Really simple JSON and XML parsing, ripped from Merb and Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jnunemaker/crack
Vcs:           https://github.com/jnunemaker/crack.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rexml) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.0
Requires:      gem(bigdecimal) >= 0
Requires:      gem(rexml) >= 0
Provides:      gem(crack) = 1.0.1

%description
Really simple JSON and XML parsing, ripped from Merb and Rails. The XML parser
is ripped from Merb and the JSON parser is ripped from Rails. I take no credit,
just packaged them for all to enjoy and easily use.


%if_enabled    doc
%package       -n gem-crack-doc
Version:       1.0.1
Release:       alt1
Summary:       Really simple JSON and XML parsing, ripped from Merb and Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета crack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(crack) = 1.0.1

%description   -n gem-crack-doc
Really simple JSON and XML parsing, ripped from Merb and Rails documentation
files.

Really simple JSON and XML parsing, ripped from Merb and Rails. The XML parser
is ripped from Merb and the JSON parser is ripped from Rails. I take no credit,
just packaged them for all to enjoy and easily use.

%description   -n gem-crack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета crack.
%endif


%if_enabled    devel
%package       -n gem-crack-devel
Version:       1.0.1
Release:       alt1
Summary:       Really simple JSON and XML parsing, ripped from Merb and Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета crack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(crack) = 1.0.1
Requires:      gem(bigdecimal) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rexml) >= 0

%description   -n gem-crack-devel
Really simple JSON and XML parsing, ripped from Merb and Rails development
package.

Really simple JSON and XML parsing, ripped from Merb and Rails. The XML parser
is ripped from Merb and the JSON parser is ripped from Rails. I take no credit,
just packaged them for all to enjoy and easily use.

%description   -n gem-crack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета crack.
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
%doc History LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-crack-doc
%doc History LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-crack-devel
%doc History LICENSE README.md
%endif


%changelog
* Wed Aug 12 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- ^ 0.4.4 -> 1.0.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.4-alt1
- ^ 0.4.3 -> 0.4.4

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
