%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname org-ruby

Name:          gem-org-ruby
Version:       0.9.12
Release:       alt1
Summary:       This gem contains Ruby routines for parsing org-mode files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/wallyqs/org-ruby
Vcs:           https://github.com/wallyqs/org-ruby.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby
BuildRequires(pre): setup-rb
BuildRequires(pre): rake
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(rubypants) >= 0.2
BuildRequires: gem(tilt) >= 0
BuildConflicts: gem(rubypants) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubypants) >= 0.2
Conflicts:     gem(rubypants) >= 1
Provides:      gem(org-ruby) = 0.9.12

%description
An Org mode parser written in Ruby.


%package       -n org-ruby
Version:       0.9.12
Release:       alt1
Summary:       This gem contains Ruby routines for parsing org-mode files executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета org-ruby
Group:         Other
BuildArch:     noarch

Requires:      gem(org-ruby) = 0.9.12

%description   -n org-ruby
This gem contains Ruby routines for parsing org-mode files executable(s).

An Org mode parser written in Ruby.

%description   -n org-ruby -l ru_RU.UTF-8
Исполнямка для самоцвета org-ruby.


%if_enabled    doc
%package       -n gem-org-ruby-doc
Version:       0.9.12
Release:       alt1
Summary:       This gem contains Ruby routines for parsing org-mode files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета org-ruby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(org-ruby) = 0.9.12

%description   -n gem-org-ruby-doc
This gem contains Ruby routines for parsing org-mode files documentation
files.

An Org mode parser written in Ruby.

%description   -n gem-org-ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета org-ruby.
%endif


%if_enabled    devel
%package       -n gem-org-ruby-devel
Version:       0.9.12
Release:       alt1
Summary:       This gem contains Ruby routines for parsing org-mode files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета org-ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(org-ruby) = 0.9.12
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3
Requires:      gem(tilt) >= 0

%description   -n gem-org-ruby-devel
This gem contains Ruby routines for parsing org-mode files development
package.

An Org mode parser written in Ruby.

%description   -n gem-org-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета org-ruby.
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
%doc History.org README.org
%ruby_gemspec
%ruby_gemlibdir

%files         -n org-ruby
%doc History.org README.org
%_bindir/org-ruby

%if_enabled    doc
%files         -n gem-org-ruby-doc
%doc History.org README.org
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-org-ruby-devel
%doc History.org README.org
%endif


%changelog
* Mon Jun 01 2026 Pavel Skrylev <majioa@altlinux.org> 0.9.12-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
