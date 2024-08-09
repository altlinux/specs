%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname glu

Name:          gem-glu
Version:       8.3.0
Release:       alt2
Summary:       Glu bindings for the opengl gem, split into a separate gem because of Glu deprecation
License:       MIT
Group:         Development/Ruby
Url:           https://rubygems.org/gems/glu
Vcs:           https://git.altlinux.org/gears/g/gem-glu.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libGLEW-devel
%if_enabled check
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(rake-compiler) >= 1.0
BuildRequires: gem(rake-compiler-dock) >= 0.6.0
BuildRequires: gem(hoe) >= 3.16
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rake-compiler-dock) >= 2
BuildConflicts: gem(hoe) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler-dock >= 1.1.0,rake-compiler-dock < 2
Provides:      gem(glu) = 8.3.0


%description
Glu bindings for the opengl gem, split into a separate gem because of Glu
deprecation.


%if_enabled    doc
%package       -n gem-glu-doc
Version:       8.3.0
Release:       alt2
Summary:       Glu bindings for the opengl gem, split into a separate gem because of Glu deprecation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета glu
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(glu) = 8.3.0

%description   -n gem-glu-doc
Glu bindings for the opengl gem, split into a separate gem because of Glu
deprecation documentation files.

%description   -n gem-glu-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета glu.
%endif


%if_enabled    devel
%package       -n gem-glu-devel
Version:       8.3.0
Release:       alt2
Summary:       Glu bindings for the opengl gem, split into a separate gem because of Glu deprecation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета glu
Group:         Development/Ruby
BuildArch:     noarch

Requires:      libGLEW-devel
Requires:      gem(glu) = 8.3.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(rake-compiler) >= 1.0
Requires:      gem(rake-compiler-dock) >= 0.6.0
Requires:      gem(hoe) >= 3.16
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rake-compiler-dock) >= 2
Conflicts:     gem(hoe) >= 4

%description   -n gem-glu-devel
Glu bindings for the opengl gem, split into a separate gem because of Glu
deprecation development package.

%description   -n gem-glu-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета glu.
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
%doc History.rdoc MIT-LICENSE README.rdoc
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-glu-doc
%doc History.rdoc MIT-LICENSE README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-glu-devel
%doc History.rdoc MIT-LICENSE README.rdoc
%ruby_includedir/*
%endif


%changelog
* Mon Aug 05 2024 Pavel Skrylev <majioa@altlinux.org> 8.3.0-alt2
- ! spec with some new styles
- * restored lost libraric binary

* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 8.3.0-alt1
- + packaged gem with Ruby Policy 2.0
