%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname attr_extras

Name:          gem-attr-extras
Version:       7.1.0
Release:       alt1
Summary:       Takes some boilerplate out of Ruby with methods like attr_initialize
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/barsoom/attr_extras
Vcs:           https://github.com/barsoom/attr_extras.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(barsoom_utils) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names attr_extras,attr-extras
Provides:      gem(attr_extras) = 7.1.0

%description
Takes some boilerplate out of Ruby with methods like attr_initialize.


%if_enabled    doc
%package       -n gem-attr-extras-doc
Version:       7.1.0
Release:       alt1
Summary:       Takes some boilerplate out of Ruby with methods like attr_initialize documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета attr_extras
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(attr_extras) = 7.1.0

%description   -n gem-attr-extras-doc
Takes some boilerplate out of Ruby with methods like attr_initialize
documentation files.

%description   -n gem-attr-extras-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета attr_extras.
%endif


%if_enabled    devel
%package       -n gem-attr-extras-devel
Version:       7.1.0
Release:       alt1
Summary:       Takes some boilerplate out of Ruby with methods like attr_initialize development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета attr_extras
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(attr_extras) = 7.1.0
Requires:      gem(barsoom_utils) >= 0
Requires:      gem(m) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-attr-extras-devel
Takes some boilerplate out of Ruby with methods like attr_initialize development
package.

%description   -n gem-attr-extras-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета attr_extras.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-attr-extras-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-attr-extras-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 7.1.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
