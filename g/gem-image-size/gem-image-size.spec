%define        gemname image_size

Name:          gem-image-size
Version:       3.0.1
Release:       alt1
Summary:       HTML entity encoding and decoding for Ruby
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/toy/image_size
Vcs:           https://github.com/toy/image_size.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 1.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-rspec) >= 2.0 gem(rubocop-rspec) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names image_size,image-size
Provides:      gem(image_size) = 3.0.1


%description
HTMLEntities is a simple library to facilitate encoding and decoding of named
(&yacute; and so on) or numerical (&#123; or &#x12a;) entities in HTML and XHTML
documents.


%package       -n gem-image-size-doc
Version:       3.0.1
Release:       alt1
Summary:       HTML entity encoding and decoding for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета image_size
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(image_size) = 3.0.1

%description   -n gem-image-size-doc
HTML entity encoding and decoding for Ruby documentation files.

HTMLEntities is a simple library to facilitate encoding and decoding of named
(&yacute; and so on) or numerical (&#123; or &#x12a;) entities in HTML and XHTML
documents.

%description   -n gem-image-size-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета image_size.


%package       -n gem-image-size-devel
Version:       3.0.1
Release:       alt1
Summary:       HTML entity encoding and decoding for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета image_size
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(image_size) = 3.0.1
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rubocop) >= 1.0 gem(rubocop) < 2
Requires:      gem(rubocop-rspec) >= 2.0 gem(rubocop-rspec) < 3

%description   -n gem-image-size-devel
HTML entity encoding and decoding for Ruby development package.

HTMLEntities is a simple library to facilitate encoding and decoding of named
(&yacute; and so on) or numerical (&#123; or &#x12a;) entities in HTML and XHTML
documents.

%description   -n gem-image-size-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета image_size.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-image-size-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-image-size-devel
%doc README.markdown


%changelog
* Fri Mar 11 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- ^ 2.1.1 -> 3.0.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- ^ 2.0.0 -> 2.1.1

* Sat Feb 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus, packaged as a gem according to Ruby Policy 2.0.
