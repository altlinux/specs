%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname turbolinks-source

Name:          gem-turbolinks-source
Version:       5.2.0
Release:       alt2.1
Summary:       Turbolinks JavaScript assets, packaged as a RubyGem
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/turbolinks/turbolinks-source-gem
Vcs:           https://github.com/turbolinks/turbolinks-source-gem.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-turbolinks-source-gem < %EVR
Provides:      ruby-turbolinks-source-gem = %EVR
Provides:      gem(turbolinks-source) = 5.2.0


%description
Turbolinks JavaScript assets, packaged as a RubyGem.


%if_enabled    doc
%package       -n gem-turbolinks-source-doc
Version:       5.2.0
Release:       alt2.1
Summary:       Turbolinks JavaScript assets, packaged as a RubyGem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета turbolinks-source
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(turbolinks-source) = 5.2.0

%description   -n gem-turbolinks-source-doc
Turbolinks JavaScript assets, packaged as a RubyGem documentation files.

%description   -n gem-turbolinks-source-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета turbolinks-source.
%endif


%if_enabled    devel
%package       -n gem-turbolinks-source-devel
Version:       5.2.0
Release:       alt2.1
Summary:       Turbolinks JavaScript assets, packaged as a RubyGem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета turbolinks-source
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(turbolinks-source) = 5.2.0

%description   -n gem-turbolinks-source-devel
Turbolinks JavaScript assets, packaged as a RubyGem development package.

%description   -n gem-turbolinks-source-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета turbolinks-source.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-turbolinks-source-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-turbolinks-source-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 5.2.0-alt2.1
- ! fixed spec by restoring package

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.0-alt2
- Use Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.

* Fri Jul 27 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- Initial build for Sisyphus
