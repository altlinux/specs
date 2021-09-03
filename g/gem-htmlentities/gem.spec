%define        gemname htmlentities

Name:          gem-htmlentities
Version:       4.3.3
Release:       alt1.1
Summary:       HTML entity encoding and decoding for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/threedaymonk/htmlentities
Vcs:           https://github.com/threedaymonk/htmlentities.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(htmlentities) = 4.3.3


%description
HTMLEntities is a simple library to facilitate encoding and decoding of named
(&yacute; and so on) or numerical (&#123; or &#x12a;) entities in HTML and XHTML
documents.


%package       -n gem-htmlentities-doc
Version:       4.3.3
Release:       alt1.1
Summary:       HTML entity encoding and decoding for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета htmlentities
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(htmlentities) = 4.3.3

%description   -n gem-htmlentities-doc
HTML entity encoding and decoding for Ruby documentation files.

HTMLEntities is a simple library to facilitate encoding and decoding of named
(&yacute; and so on) or numerical (&#123; or &#x12a;) entities in HTML and XHTML
documents.

%description   -n gem-htmlentities-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета htmlentities.


%package       -n gem-htmlentities-devel
Version:       4.3.3
Release:       alt1.1
Summary:       HTML entity encoding and decoding for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета htmlentities
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(htmlentities) = 4.3.3
Requires:      gem(rake) >= 0

%description   -n gem-htmlentities-devel
HTML entity encoding and decoding for Ruby development package.

HTMLEntities is a simple library to facilitate encoding and decoding of named
(&yacute; and so on) or numerical (&#123; or &#x12a;) entities in HTML and XHTML
documents.

%description   -n gem-htmlentities-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета htmlentities.


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

%files         -n gem-htmlentities-doc
%ruby_gemdocdir

%files         -n gem-htmlentities-devel


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 4.3.3-alt1.1
- ! spec

* Sat Feb 23 2019 Pavel Skrylev <majioa@altlinux.org> 4.3.3-alt1
- Initial build for Sisyphus, packaged as a gem according to Ruby Policy 2.0.
