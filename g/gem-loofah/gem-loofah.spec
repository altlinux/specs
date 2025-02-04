%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname loofah

Name:          gem-loofah
Version:       2.24.0
Release:       alt1
Summary:       HTML/XML manipulation and sanitization based on Nokogiri
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flavorjones/loofah
Vcs:           https://github.com/flavorjones/loofah.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(crass) >= 1.0.2
BuildRequires: gem(hoe-markdown) >= 1.5.1
BuildRequires: gem(json) >= 2.2
BuildRequires: gem(minitest) >= 5.14
BuildRequires: gem(nokogiri) >= 1.12.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(crass) >= 1.1
BuildConflicts: gem(hoe-markdown) >= 2
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(rubocop) >= 2
%if_enabled check
BuildRequires: gem(rubocop-minitest) >= 0.13.0
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-shopify) >= 2.12.0
BuildConflicts: gem(rubocop-minitest) >= 1
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-shopify) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_use_gem_dependency rubocop-shopify >= 2.14.0,rubocop-shopify < 3
Requires:      ruby >= 2.5.0
Requires:      gem(crass) >= 1.0.2
Requires:      gem(nokogiri) >= 1.12.0
Conflicts:     gem(crass) >= 1.1
Obsoletes:     ruby-loofah < %EVR
Provides:      ruby-loofah = %EVR
Provides:      loofah = %EVR
Provides:      gem(loofah) = 2.24.0

%description
Loofah is a general library for manipulating and transforming HTML/XML documents
and fragments, built on top of Nokogiri.

Loofah excels at HTML sanitization (XSS prevention). It includes some nice HTML
sanitizers, which are based on HTML5lib's safelist, so it most likely won't make
your codes less secure. (These statements have not been evaluated by
Netexperts.)

ActiveRecord extensions for sanitization are available in the
loofah-activerecord gem.


%if_enabled    doc
%package       -n gem-loofah-doc
Version:       2.24.0
Release:       alt1
Summary:       HTML/XML manipulation and sanitization based on Nokogiri documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета loofah
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(loofah) = 2.24.0

%description   -n gem-loofah-doc
HTML/XML manipulation and sanitization based on Nokogiri documentation
files.

Loofah is a general library for manipulating and transforming HTML/XML documents
and fragments, built on top of Nokogiri.

Loofah excels at HTML sanitization (XSS prevention). It includes some nice HTML
sanitizers, which are based on HTML5lib's safelist, so it most likely won't make
your codes less secure. (These statements have not been evaluated by
Netexperts.)

ActiveRecord extensions for sanitization are available in the
loofah-activerecord gem.

%description   -n gem-loofah-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета loofah.
%endif


%if_enabled    devel
%package       -n gem-loofah-devel
Version:       2.24.0
Release:       alt1
Summary:       HTML/XML manipulation and sanitization based on Nokogiri development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета loofah
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(loofah) = 2.24.0
Requires:      gem(hoe-markdown) >= 1.5.1
Requires:      gem(json) >= 2.2
Requires:      gem(minitest) >= 5.14
Requires:      gem(rake) >= 13.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-minitest) >= 0.13.0
Requires:      gem(rubocop-packaging) >= 0.5.2
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-shopify) >= 2.12.0
Conflicts:     gem(hoe-markdown) >= 2
Conflicts:     gem(json) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-minitest) >= 1
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-shopify) >= 3

%description   -n gem-loofah-devel
HTML/XML manipulation and sanitization based on Nokogiri development
package.

Loofah is a general library for manipulating and transforming HTML/XML documents
and fragments, built on top of Nokogiri.

Loofah excels at HTML sanitization (XSS prevention). It includes some nice HTML
sanitizers, which are based on HTML5lib's safelist, so it most likely won't make
your codes less secure. (These statements have not been evaluated by
Netexperts.)

ActiveRecord extensions for sanitization are available in the
loofah-activerecord gem.

%description   -n gem-loofah-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета loofah.
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
%doc CHANGELOG.md MIT-LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-loofah-doc
%doc CHANGELOG.md MIT-LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-loofah-devel
%doc CHANGELOG.md MIT-LICENSE.txt README.md
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 2.24.0-alt1
- ^ 2.19.1 -> 2.24.0

* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 2.19.1-alt1
- ^ 2.19.0 -> 2.19.1

* Tue Nov 22 2022 Pavel Skrylev <majioa@altlinux.org> 2.19.0-alt1
- ^ 2.12.0 -> 2.19.0

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.12.0-alt1
- ^ 2.4.0 -> 2.12.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- used (>) Ruby Policy 2.0
- updated (^) 2.2.3 -> 2.4.0

* Wed Mar 27 2019 Ivan A. Melnikov <iv@altlinux.org> 2.2.3-alt1
- 2.2.3 (CVE-2018-16468);
- fix version in gamespec for packaging (closes: #36441).

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus
