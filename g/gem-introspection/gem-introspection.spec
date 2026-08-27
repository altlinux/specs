%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname introspection

Name:          gem-introspection
Version:       0.0.4.30
Release:       alt0.1
Summary:       Dynamic inspection of the hierarchy of method definitions on a Ruby object
License:       MIT
Group:         Development/Ruby
Url:           http://jamesmead.org
Vcs:           https://github.com/floehopper/introspection.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(blankslate) >= 0
BuildRequires: gem(metaclass) >= 0.0.1
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(metaclass) >= 0.1
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
Requires:      rubygems >= 1.3.6
Requires:      gem(metaclass) >= 0.0.1
Conflicts:     gem(metaclass) >= 0.1
Provides:      gem(introspection) = 0.0.4.30

%ruby_use_gem_version introspection:0.0.4.30

%description
Dynamic inspection of the hierarchy of method definitions on a Ruby object.


%if_enabled    doc
%package       -n gem-introspection-doc
Version:       0.0.4.30
Release:       alt0.1
Summary:       Dynamic inspection of the hierarchy of method definitions on a Ruby object documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета introspection
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(introspection) = 0.0.4.30

%description   -n gem-introspection-doc
Dynamic inspection of the hierarchy of method definitions on a Ruby object
documentation files.

%description   -n gem-introspection-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета introspection.
%endif


%if_enabled    devel
%package       -n gem-introspection-devel
Version:       0.0.4.30
Release:       alt0.1
Summary:       Dynamic inspection of the hierarchy of method definitions on a Ruby object development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета introspection
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(introspection) = 0.0.4.30
Requires:      gem(blankslate) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 0
Conflicts:     gem(minitest) >= 7

%description   -n gem-introspection-devel
Dynamic inspection of the hierarchy of method definitions on a Ruby object
development package.

%description   -n gem-introspection-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета introspection.
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
%doc COPYING.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-introspection-doc
%doc COPYING.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-introspection-devel
%doc COPYING.txt README.md
%endif


%changelog
* Fri Aug 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.0.4.30-alt0.1
- ^ 0.0.4 -> 0.0.4p30
- ! fixed dep to minitest gem

* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt1
- + packaged gem with Ruby Policy 2.0
