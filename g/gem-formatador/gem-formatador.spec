%define        _unpackaged_files_terminate_build 1
%define        gemname formatador

Name:          gem-formatador
Version:       1.1.0
Release:       alt1
Summary:       Stdout text formatting
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/geemus/formatador
Vcs:           https://github.com/geemus/formatador.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(shindo) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-formatador < %EVR
Provides:      ruby-formatador = %EVR
Provides:      gem(formatador) = 1.1.0


%description
Stdout text formatting.


%package       -n gem-formatador-doc
Version:       1.1.0
Release:       alt1
Summary:       Stdout text formatting documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета formatador
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(formatador) = 1.1.0

%description   -n gem-formatador-doc
Stdout text formatting documentation files.

%description   -n gem-formatador-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета formatador.


%package       -n gem-formatador-devel
Version:       1.1.0
Release:       alt1
Summary:       Stdout text formatting development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета formatador
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(formatador) = 1.1.0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(shindo) >= 0

%description   -n gem-formatador-devel
Stdout text formatting development package.

%description   -n gem-formatador-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета formatador.


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

%files         -n gem-formatador-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-formatador-devel
%doc README.md


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 0.2.5 -> 1.1.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.5-alt2.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.5-alt2
- used (>) Ruby Policy 2.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.5-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus
