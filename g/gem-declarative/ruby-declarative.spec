%define        gemname declarative

Name:          gem-declarative
Version:       0.0.20
Release:       alt1
Summary:       DSL for nested schemas
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/apotonick/declarative
Vcs:           https://github.com/apotonick/declarative.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(minitest) >= 0 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-declarative < %EVR
Provides:      ruby-declarative = %EVR
Provides:      gem(declarative) = 0.0.20


%description
DSL for nested generic schemas with inheritance and refining.


%package       -n gem-declarative-doc
Version:       0.0.20
Release:       alt1
Summary:       DSL for nested schemas documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета declarative
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(declarative) = 0.0.20

%description   -n gem-declarative-doc
DSL for nested schemas documentation files.

DSL for nested generic schemas with inheritance and refining.

%description   -n gem-declarative-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета declarative.


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

%files         -n gem-declarative-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.20-alt1
- > Ruby Policy 2.0
- ^ 0.0.10 -> 0.0.20

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.10-alt1.1
- Rebuild for new Ruby autorequirements.

* Sun May 27 2018 Andrey Cherepanov <cas@altlinux.org> 0.0.10-alt1
- Initial build for Sisyphus
