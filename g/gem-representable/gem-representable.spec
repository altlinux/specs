%define        gemname representable

Name:          gem-representable
Version:       3.2.0
Release:       alt1
Summary:       Maps representation documents from and to Ruby objects
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/trailblazer/representable/
Vcs:           https://github.com/trailblazer/representable.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test_xml) >= 0.1.6
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(virtus) >= 0
BuildRequires: gem(dry-types) >= 0
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(minitest-line) >= 0
BuildRequires: gem(multi_json) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(uber) < 0.2.0
BuildRequires: gem(declarative) < 0.1.0
BuildRequires: gem(trailblazer-option) >= 0.1.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(uber) < 0.2.0
Requires:      gem(declarative) < 0.1.0
Requires:      gem(trailblazer-option) >= 0.1.1
Conflicts:     gem(trailblazer-option) >= 0.2.0
Obsoletes:     ruby-representable < %EVR
Provides:      ruby-representable = %EVR
Provides:      gem(representable) = 3.2.0


%description
Maps representation documents from and to Ruby objects. Includes JSON, XML and
YAML support, plain properties and compositions.


%package       -n gem-representable-doc
Version:       3.2.0
Release:       alt1
Summary:       Maps representation documents from and to Ruby objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета representable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(representable) = 3.2.0

%description   -n gem-representable-doc
Maps representation documents from and to Ruby objects documentation
files.

Maps representation documents from and to Ruby objects. Includes JSON, XML and
YAML support, plain properties and compositions.

%description   -n gem-representable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета representable.


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

%files         -n gem-representable-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Oct 13 2022 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- ^ 3.1.1 -> 3.2.0

* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt1
- ^ 3.0.4 -> 3.1.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Sat May 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1
- Initial build for Sisyphus
