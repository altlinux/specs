%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname uber

Name:          gem-uber
Version:       0.1.0.3
Release:       alt0.1
Summary:       Gem-authoring extensions for classes and modules
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/apotonick/uber
Vcs:           https://github.com/apotonick/uber.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(minitest) >= 4.0
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 4.0
Requires:      gem(benchmark-ips) >= 0
Obsoletes:     ruby-uber < %EVR
Provides:      ruby-uber = %EVR
Provides:      gem(uber) = 0.1.0.3

%ruby_use_gem_version uber:0.1.0.3

%description
Gem-authoring extensions for classes and modules.

Gem-authoring tools like class method inheritance in modules, dynamic options
and more.


%if_enabled    doc
%package       -n gem-uber-doc
Version:       0.1.0.3
Release:       alt0.1
Summary:       Gem-authoring extensions for classes and modules documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета uber
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(uber) = 0.1.0.3

%description   -n gem-uber-doc
Gem-authoring extensions for classes and modules documentation files.

Gem-authoring tools like class method inheritance in modules, dynamic options
and more.

%description   -n gem-uber-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета uber.
%endif


%if_enabled    devel
%package       -n gem-uber-devel
Version:       0.1.0.3
Release:       alt0.1
Summary:       Gem-authoring extensions for classes and modules development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета uber
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(uber) = 0.1.0.3
Requires:      gem(minitest) >= 4.0
Requires:      gem(rake) >= 0

%description   -n gem-uber-devel
Gem-authoring extensions for classes and modules development package.

Gem-authoring tools like class method inheritance in modules, dynamic options
and more.

%description   -n gem-uber-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета uber.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-uber-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-uber-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Aug 31 2026 Pavel Skrylev <majioa@altlinux.org> 0.1.0.3-alt0.1
- ^ 0.1.0 -> 0.1.0p3

* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Sun May 27 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
