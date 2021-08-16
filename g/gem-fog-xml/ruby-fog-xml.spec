%define        gemname fog-xml

Name:          gem-fog-xml
Version:       0.1.3.1
Release:       alt1
Summary:       Shared XML related functionality for fog
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-xml
Vcs:           https://github.com/fog/fog-xml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(nokogiri) >= 1.5.11 gem(nokogiri) < 2.0.0
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(turn) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(coveralls) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 0
Requires:      gem(nokogiri) >= 1.5.11 gem(nokogiri) < 2.0.0
Obsoletes:     ruby-fog-xml < %EVR
Provides:      ruby-fog-xml = %EVR
Provides:      gem(fog-xml) = 0.1.3.1

%ruby_use_gem_version fog-xml:0.1.3.1

%description
%summary


%package       -n gem-fog-xml-doc
Version:       0.1.3.1
Release:       alt1
Summary:       Shared XML related functionality for fog documentation files
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-xml) = 0.1.3.1

%description   -n gem-fog-xml-doc
Shared XML related functionality for fog documentation files.

%summary

%description   -n gem-fog-xml-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-xml.


%package       -n gem-fog-xml-devel
Version:       0.1.3.1
Release:       alt1
Summary:       Shared XML related functionality for fog development package
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-xml) = 0.1.3.1
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(minitest) >= 0
Requires:      gem(turn) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(coveralls) >= 0

%description   -n gem-fog-xml-devel
Shared XML related functionality for fog development package.

%summary

%description   -n gem-fog-xml-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-xml.


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

%files         -n gem-fog-xml-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-xml-devel
%doc README.md


%changelog
* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.3.1-alt1
- ^ 0.1.3 -> 0.1.3.1
- * policify name

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus
