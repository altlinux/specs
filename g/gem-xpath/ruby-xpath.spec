%define        gemname xpath

Name:          gem-xpath
Version:       3.2.0
Release:       alt1.1
Summary:       Ruby library for generating XPath expressions
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/teamcapybara/xpath
Vcs:           https://github.com/teamcapybara/xpath.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(nokogiri) >= 1.8 gem(nokogiri) < 2
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(yard) >= 0.5.8

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(nokogiri) >= 1.8 gem(nokogiri) < 2
Obsoletes:     ruby-xpath < %EVR
Provides:      ruby-xpath = %EVR
Provides:      gem(xpath) = 3.2.0


%description
XPath is a Ruby DSL around a subset of XPath 1.0. Its primary purpose is to
facilitate writing complex XPath queries from Ruby code.


%package       -n gem-xpath-doc
Version:       3.2.0
Release:       alt1.1
Summary:       Ruby library for generating XPath expressions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета xpath
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(xpath) = 3.2.0

%description   -n gem-xpath-doc
Ruby library for generating XPath expressions documentation files.

XPath is a Ruby DSL around a subset of XPath 1.0. Its primary purpose is to
facilitate writing complex XPath queries from Ruby code.

%description   -n gem-xpath-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета xpath.


%package       -n gem-xpath-devel
Version:       3.2.0
Release:       alt1.1
Summary:       Ruby library for generating XPath expressions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета xpath
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(xpath) = 3.2.0
Requires:      gem(pry) >= 0 gem(pry) < 1
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(yard) >= 0.5.8

%description   -n gem-xpath-devel
Ruby library for generating XPath expressions development package.

XPath is a Ruby DSL around a subset of XPath 1.0. Its primary purpose is to
facilitate writing complex XPath queries from Ruby code.

%description   -n gem-xpath-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета xpath.


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

%files         -n gem-xpath-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-xpath-devel
%doc README.md


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1.1
- ! spec

* Tue Oct 16 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version.

* Fri Jul 27 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus
