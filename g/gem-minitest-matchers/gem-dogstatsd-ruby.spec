%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-matchers

Name:          gem-minitest-matchers
Version:       1.4.1
Release:       alt1
Summary:       Adds support for RSpec-style matchers
License:       Unlicense
Group:         Development/Ruby
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby
BuildRequires(pre): setup-rb
BuildRequires(pre): rake
%if_enabled check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) >= 5.0
Conflicts:     gem(minitest) >= 6
Provides:      gem(minitest-matchers) = 1.4.1

%description
Adds support for RSpec-style matchers


%if_enabled    doc
%package       -n gem-minitest-matchers-doc
Version:       1.4.1
Release:       alt1
Summary:       Adds support for RSpec-style matchers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-matchers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-matchers) = 1.4.1

%description   -n gem-minitest-matchers-doc
Adds support for RSpec-style matchers documentation files.

%description   -n gem-minitest-matchers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-matchers.
%endif


%if_enabled    devel
%package       -n gem-minitest-matchers-devel
Version:       1.4.1
Release:       alt1
Summary:       Adds support for RSpec-style matchers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-matchers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-matchers) = 1.4.1
Requires:      gem(rake) >= 0

%description   -n gem-minitest-matchers-devel
Adds support for RSpec-style matchers development package.

%description   -n gem-minitest-matchers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-matchers.
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
%doc History.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-matchers-doc
%doc History.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-matchers-devel
%doc History.txt README.md
%endif


%changelog
* Wed Apr 29 2026 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
