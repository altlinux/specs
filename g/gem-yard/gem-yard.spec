%define        gemname yard

Name:          gem-yard
Version:       0.9.27
Release:       alt1
Summary:       YARD is a Ruby Documentation tool. The Y stands for "Yay!"
License:       MIT
Group:         Development/Ruby
Url:           https://yardoc.org/
Vcs:           https://github.com/lsegal/yard.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(webrick) >= 1.7.0 gem(webrick) < 1.8

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(webrick) >= 1.7.0 gem(webrick) < 1.8
Obsoletes:     ruby-yard < %EVR
Provides:      ruby-yard = %EVR
Provides:      gem(yard) = 0.9.27


%description
YARD is a documentation generation tool for the Ruby programming language. It
enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.


%package       -n yard
Version:       0.9.27
Release:       alt1
Summary:       YARD is a Ruby Documentation tool. The Y stands for "Yay!" executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета yard
Group:         Documentation
BuildArch:     noarch

Requires:      gem(yard) = 0.9.27

%description   -n yard
YARD is a Ruby Documentation tool. The Y stands for "Yay!" executable(s).

YARD is a documentation generation tool for the Ruby programming language. It
enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.

%description   -n yard -l ru_RU.UTF-8
Исполнямка для самоцвета yard.


%package       -n gem-yard-doc
Version:       0.9.27
Release:       alt1
Summary:       YARD is a Ruby Documentation tool. The Y stands for "Yay!" documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yard
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yard) = 0.9.27

%description   -n gem-yard-doc
YARD is a Ruby Documentation tool. The Y stands for "Yay!" documentation
files.

YARD is a documentation generation tool for the Ruby programming language. It
enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.

%description   -n gem-yard-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yard.


%package       -n gem-yard-devel
Version:       0.9.27
Release:       alt1
Summary:       YARD is a Ruby Documentation tool. The Y stands for "Yay!" development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yard
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yard) = 0.9.27

%description   -n gem-yard-devel
YARD is a Ruby Documentation tool. The Y stands for "Yay!" development
package.

YARD is a documentation generation tool for the Ruby programming language. It
enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.

%description   -n gem-yard-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yard.


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

%files         -n yard
%doc README.md
%_bindir/yard
%_bindir/yardoc
%_bindir/yri

%files         -n gem-yard-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-yard-devel
%doc README.md


%changelog
* Wed May 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.27-alt1
- ^ 0.9.25 -> 0.9.27

* Tue Sep 15 2020 Pavel Skrylev <majioa@altlinux.org> 0.9.25-alt1
- ^ 0.9.19 -> 0.9.25
- ! spec tags

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.19-alt1
- 0.9.16 -> 0.9.19
- > Ruby Policy 2.0

* Sat Dec 29 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.16-alt1
- Initial build for Sisyphus, packaged as a gem
