%define        _unpackaged_files_terminate_build 1
%define        gemname rake-compiler

Name:          gem-rake-compiler
Version:       1.2.5
Release:       alt1
Summary:       Provide a standard and simplified way to build and package Ruby C and Java extensions using Rake as glue
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rake-compiler/rake-compiler
Vcs:           https://github.com/rake-compiler/rake-compiler.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 2.9
BuildRequires: gem(cucumber) >= 1.2
BuildRequires: gem(bundler) >= 0
BuildConflicts: gem(cucumber) > 2.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(rake) >= 0
Provides:      gem(rake-compiler) = 1.2.5

%ruby_bindir_to %ruby_bindir

%description
rake-compiler is first and foremost a productivity tool for Ruby developers. Its
goal is to make the busy developer's life easier by simplifying the building and
packaging of Ruby extensions by simplifying code and reducing duplication.


%package       -n rake-compiler
Version:       1.2.5
Release:       alt1
Summary:       Provide a standard and simplified way to build and package Ruby C and Java extensions using Rake as glue executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rake-compiler
Group:         Other
BuildArch:     noarch

Requires:      gem(rake-compiler) = 1.2.5

%description   -n rake-compiler
Provide a standard and simplified way to build and package Ruby C and Java
extensions using Rake as glue executable(s).

rake-compiler is first and foremost a productivity tool for Ruby developers. Its
goal is to make the busy developer's life easier by simplifying the building and
packaging of Ruby extensions by simplifying code and reducing duplication.

%description   -n rake-compiler -l ru_RU.UTF-8
Исполнямка для самоцвета rake-compiler.


%package       -n gem-rake-compiler-doc
Version:       1.2.5
Release:       alt1
Summary:       Provide a standard and simplified way to build and package Ruby C and Java extensions using Rake as glue documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rake-compiler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rake-compiler) = 1.2.5

%description   -n gem-rake-compiler-doc
Provide a standard and simplified way to build and package Ruby C and Java
extensions using Rake as glue documentation files.

rake-compiler is first and foremost a productivity tool for Ruby developers. Its
goal is to make the busy developer's life easier by simplifying the building and
packaging of Ruby extensions by simplifying code and reducing duplication.

%description   -n gem-rake-compiler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rake-compiler.


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

%files         -n rake-compiler
%doc README.md
%ruby_bindir/rake-compiler

%files         -n gem-rake-compiler-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 1.2.5-alt1
- ^ 1.2.0 -> 1.2.5 without devel

* Sat Apr 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt0.1
- ^ 1.1.2 -> 1.2.0

* Mon Jun 28 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.2-alt1
- ^ 1.1.1 -> 1.1.2
- * policify name

* Tue Jul 21 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.

* Wed Dec 25 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Mon Dec 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.9-alt1
- New version.

* Wed Nov 06 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.8-alt1
- New version.

* Thu Jun 13 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt3
- Fix built provides (closes #36888)

* Tue Feb 26 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.7-alt2
- Use Ruby Policy 2.0.

* Fri Jan 04 2019 Andrey Cherepanov <cas@altlinux.org> 1.0.7-alt1
- New version.

* Mon Dec 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- New version.

* Wed Jul 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt2
- Package as gem.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
