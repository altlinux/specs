%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname yard

Name:          gem-yard
Version:       0.9.36
Release:       alt1.1
Summary:       YARD is a Ruby Documentation tool. The Y stands for "Yay!"
License:       MIT
Group:         Development/Ruby
Url:           https://yardoc.org/
Vcs:           https://github.com/lsegal/yard.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(json) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(samus) >= 3.0.9
BuildRequires: gem(coveralls_reborn) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(asciidoctor) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(commonmarker) >= 0
BuildRequires: gem(RedCloth) >= 0
BuildRequires: gem(rack) >= 2.0
BuildRequires: gem(gettext) >= 0
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(samus) >= 3.1
BuildConflicts: gem(rack) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rack >= 3.0,rack < 4
Obsoletes:     ruby-yard < %EVR
Provides:      ruby-yard = %EVR
Provides:      gem(yard) = 0.9.36


%description
YARD is a documentation generation tool for the Ruby programming language. It
enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.


%package       -n yard
Version:       0.9.36
Release:       alt1.1
Summary:       YARD is a Ruby Documentation tool. The Y stands for "Yay!" executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета yard
Group:         Documentation
BuildArch:     noarch

Requires:      gem(yard) = 0.9.36

%description   -n yard
YARD is a Ruby Documentation tool. The Y stands for "Yay!" executable(s).

YARD is a documentation generation tool for the Ruby programming language. It
enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.
%description   -n yard -l ru_RU.UTF-8
Исполнямка для самоцвета yard.


%if_enabled    doc
%package       -n gem-yard-doc
Version:       0.9.36
Release:       alt1.1
Summary:       YARD is a Ruby Documentation tool. The Y stands for "Yay!" documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yard
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yard) = 0.9.36

%description   -n gem-yard-doc
YARD is a Ruby Documentation tool. The Y stands for "Yay!" documentation
files.

YARD is a documentation generation tool for the Ruby programming language. It
enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.
%description   -n gem-yard-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yard.
%endif


%if_enabled    devel
%package       -n gem-yard-devel
Version:       0.9.36
Release:       alt1.1
Summary:       YARD is a Ruby Documentation tool. The Y stands for "Yay!" development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yard
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yard) = 0.9.36
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(json) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(samus) >= 3.0.9
Requires:      gem(coveralls_reborn) >= 0
Requires:      gem(webrick) >= 0
Requires:      gem(asciidoctor) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(commonmarker) >= 0
Requires:      gem(RedCloth) >= 0
Requires:      gem(rack) >= 2.0
Requires:      gem(gettext) >= 0
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(samus) >= 3.1
Conflicts:     gem(rack) >= 4

%description   -n gem-yard-devel
YARD is a Ruby Documentation tool. The Y stands for "Yay!" development
package.

YARD is a documentation generation tool for the Ruby programming language. It
enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.
%description   -n gem-yard-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yard.
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
%doc README.md templates/default/onefile/html/readme.erb
%ruby_gemspec
%ruby_gemplugin
%ruby_gemlibdir

%files         -n yard
%doc README.md templates/default/onefile/html/readme.erb
%_bindir/yard
%_bindir/yardoc
%_bindir/yri

%if_enabled    doc
%files         -n gem-yard-doc
%doc README.md templates/default/onefile/html/readme.erb
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-yard-devel
%doc README.md templates/default/onefile/html/readme.erb
%endif


%changelog
* Mon May 20 2024 Pavel Skrylev <majioa@altlinux.org> 0.9.36-alt1.1
- ! dep to rack gem

* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 0.9.36-alt1
- ^ 0.9.34 -> 0.9.36

* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.34-alt1
- ^ 0.9.27 -> 0.9.34

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
