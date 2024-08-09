%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname date

Name:          gem-date
Version:       3.3.4
Release:       alt1
Summary:       A subclass of Object includes Comparable module for handling dates
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/date
Vcs:           https://github.com/ruby/date.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(date) = 3.3.4


%description
A subclass of Object includes Comparable module for handling dates.


%if_enabled    doc
%package       -n gem-date-doc
Version:       3.3.4
Release:       alt1
Summary:       A subclass of Object includes Comparable module for handling dates documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета date
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(date) = 3.3.4

%description   -n gem-date-doc
A subclass of Object includes Comparable module for handling dates documentation
files.

%description   -n gem-date-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета date.
%endif


%if_enabled    devel
%package       -n gem-date-devel
Version:       3.3.4
Release:       alt1
Summary:       A subclass of Object includes Comparable module for handling dates development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета date
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(date) = 3.3.4
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-date-devel
A subclass of Object includes Comparable module for handling dates development
package.

%description   -n gem-date-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета date.
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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-date-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-date-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 3.3.4-alt1
- ^ 3.2.2 -> 3.3.4

* Mon Apr 04 2022 Pavel Skrylev <majioa@altlinux.org> 3.2.2-alt1
- + packaged gem with Ruby Policy 2.0
