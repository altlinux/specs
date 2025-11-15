%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname image_size

Name:          gem-image-size
Version:       3.4.0
Release:       alt1
Summary:       HTML entity encoding and decoding for Ruby
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/toy/image_size
Vcs:           https://github.com/toy/image_size.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-rspec) >= 2.0
BuildRequires: gem(webrick) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
%ruby_alias_names image_size,image-size
Requires:      ruby >= 1.9.3
Requires:      gem(webrick) >= 0
Provides:      gem(image_size) = 3.4.0

%description
HTMLEntities is a simple library to facilitate encoding and decoding of named
(&yacute; and so on) or numerical (&#123; or &#x12a;) entities in HTML and XHTML
documents.


%if_enabled    doc
%package       -n gem-image-size-doc
Version:       3.4.0
Release:       alt1
Summary:       HTML entity encoding and decoding for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета image_size
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(image_size) = 3.4.0

%description   -n gem-image-size-doc
HTML entity encoding and decoding for Ruby documentation files.

HTMLEntities is a simple library to facilitate encoding and decoding of named
(&yacute; and so on) or numerical (&#123; or &#x12a;) entities in HTML and XHTML
documents.

%description   -n gem-image-size-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета image_size.
%endif


%if_enabled    devel
%package       -n gem-image-size-devel
Version:       3.4.0
Release:       alt1
Summary:       HTML entity encoding and decoding for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета image_size
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(image_size) = 3.4.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-rspec) >= 2.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-rspec) >= 4

%description   -n gem-image-size-devel
HTML entity encoding and decoding for Ruby development package.

HTMLEntities is a simple library to facilitate encoding and decoding of named
(&yacute; and so on) or numerical (&#123; or &#x12a;) entities in HTML and XHTML
documents.

%description   -n gem-image-size-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета image_size.
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
%doc CHANGELOG.markdown LICENSE.txt README.markdown
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-image-size-doc
%doc CHANGELOG.markdown LICENSE.txt README.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-image-size-devel
%doc CHANGELOG.markdown LICENSE.txt README.markdown
%endif


%changelog
* Sat Nov 15 2025 Pavel Skrylev <majioa@altlinux.org> 3.4.0-alt1
- ^ 3.0.1 -> 3.4.0

* Fri Mar 11 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- ^ 2.1.1 -> 3.0.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- ^ 2.0.0 -> 2.1.1

* Sat Feb 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus, packaged as a gem according to Ruby Policy 2.0.
