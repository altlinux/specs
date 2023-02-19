%define        gemname loofah

Name:          gem-loofah
Version:       2.19.1
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
%if_with check
BuildRequires: gem(hoe-markdown) >= 1.3
BuildRequires: gem(json) >= 2.2
BuildRequires: gem(minitest) >= 5.14
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(rr) >= 1.2.0
BuildRequires: gem(rubocop) >= 1.1
BuildRequires: gem(psych) >= 4.0
BuildRequires: gem(crass) >= 1.0.2
BuildRequires: gem(nokogiri) >= 1.5.9
BuildConflicts: gem(hoe-markdown) >= 2
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(rr) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(psych) >= 5
BuildConflicts: gem(crass) >= 1.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rr >= 3.0.4,rr < 4
Requires:      gem(crass) >= 1.0.2
Requires:      gem(nokogiri) >= 1.5.9
Conflicts:     gem(crass) >= 1.1
Obsoletes:     ruby-loofah < %EVR
Provides:      ruby-loofah = %EVR
Provides:      gem(loofah) = 2.19.1


%description
Loofah is a general library for manipulating and transforming HTML/XML documents
and fragments, built on top of Nokogiri.

Loofah excels at HTML sanitization (XSS prevention). It includes some nice HTML
sanitizers, which are based on HTML5lib's safelist, so it most likely won't make
your codes less secure. (These statements have not been evaluated by
Netexperts.)

ActiveRecord extensions for sanitization are available in the
loofah-activerecord gem.


%package       -n gem-loofah-doc
Version:       2.19.1
Release:       alt1
Summary:       HTML/XML manipulation and sanitization based on Nokogiri documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета loofah
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(loofah) = 2.19.1

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


%package       -n gem-loofah-devel
Version:       2.19.1
Release:       alt1
Summary:       HTML/XML manipulation and sanitization based on Nokogiri development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета loofah
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(loofah) = 2.19.1
Requires:      gem(hoe-markdown) >= 1.3
Requires:      gem(json) >= 2.2
Requires:      gem(minitest) >= 5.14
Requires:      gem(rake) >= 13.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(rr) >= 1.2.0
Requires:      gem(rubocop) >= 1.1
Requires:      gem(psych) >= 4.0
Conflicts:     gem(hoe-markdown) >= 2
Conflicts:     gem(json) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(rr) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(psych) >= 5

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

%files         -n gem-loofah-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-loofah-devel
%doc README.md


%changelog
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
