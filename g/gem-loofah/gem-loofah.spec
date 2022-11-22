%define        gemname loofah

Name:          gem-loofah
Version:       2.19.0
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
BuildRequires: gem(hoe-markdown) >= 1.3 gem(hoe-markdown) < 2
BuildRequires: gem(json) >= 2.2 gem(json) < 3
BuildRequires: gem(minitest) >= 5.14 gem(minitest) < 6
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(rr) >= 1.2.0 gem(rr) < 4
BuildRequires: gem(rubocop) >= 1.1 gem(rubocop) < 2
BuildRequires: gem(crass) >= 1.0.2 gem(crass) < 1.1
BuildRequires: gem(nokogiri) >= 1.5.9
BuildRequires: gem(hoe-markdown) >= 1.3 gem(hoe-markdown) < 2
BuildRequires: gem(json) >= 2.2 gem(json) < 3
BuildRequires: gem(minitest) >= 5.14 gem(minitest) < 6
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(rr) >= 1.2.0 gem(rr) < 4
BuildRequires: gem(rubocop) >= 1.1 gem(rubocop) < 2
BuildRequires: gem(crass) >= 1.0.2 gem(crass) < 1.1
BuildRequires: gem(nokogiri) >= 1.5.9
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rr >= 3.0.4,rr < 4
Requires:      gem(crass) >= 1.0.2 gem(crass) < 1.1
Requires:      gem(nokogiri) >= 1.5.9
Obsoletes:     ruby-loofah < %EVR
Provides:      ruby-loofah = %EVR
Provides:      gem(loofah) = 2.19.0


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
Version:       2.19.0
Release:       alt1
Summary:       HTML/XML manipulation and sanitization based on Nokogiri documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета loofah
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(loofah) = 2.19.0

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
Version:       2.19.0
Release:       alt1
Summary:       HTML/XML manipulation and sanitization based on Nokogiri development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета loofah
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(loofah) = 2.19.0
Requires:      gem(hoe-markdown) >= 1.3 gem(hoe-markdown) < 2
Requires:      gem(json) >= 2.2 gem(json) < 3
Requires:      gem(minitest) >= 5.14 gem(minitest) < 6
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(rr) >= 1.2.0 gem(rr) < 4
Requires:      gem(rubocop) >= 1.1 gem(rubocop) < 2

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
