%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname csv

Name:          gem-csv
Version:       3.3.5
Release:       alt1
Summary:       CSV Reading and Writing
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/csv
Vcs:           https://github.com/ruby/csv.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(benchmark_driver) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(psych) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(test-unit) >= 3.3.5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
Requires:      ruby >= 2.5.0
Provides:      gem(csv) = 3.3.5

%description
This library provides a complete interface to CSV files and data. It offers
tools to enable you to read and write to and from Strings or IO objects, as
needed.


%if_enabled    doc
%package       -n gem-csv-doc
Version:       3.3.5
Release:       alt1
Summary:       CSV Reading and Writing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета csv
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(csv) = 3.3.5

%description   -n gem-csv-doc
CSV Reading and Writing documentation files.

This library provides a complete interface to CSV files and data. It offers
tools to enable you to read and write to and from Strings or IO objects, as
needed.

%description   -n gem-csv-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета csv.
%endif


%if_enabled    devel
%package       -n gem-csv-devel
Version:       3.3.5
Release:       alt1
Summary:       CSV Reading and Writing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета csv
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(csv) = 3.3.5
Requires:      gem(benchmark_driver) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(psych) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(test-unit) >= 3.3.5

%description   -n gem-csv-devel
CSV Reading and Writing development package.

This library provides a complete interface to CSV files and data. It offers
tools to enable you to read and write to and from Strings or IO objects, as
needed.

%description   -n gem-csv-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета csv.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-csv-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-csv-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Thu Nov 20 2025 Pavel Skrylev <majioa@altlinux.org> 3.3.5-alt1
- ^ 3.2.6 -> 3.3.5

* Fri Apr 14 2023 Pavel Skrylev <majioa@altlinux.org> 3.2.6-alt1
- ^ 3.2.0 -> 3.2.6

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- ^ 3.1.2 -> 3.2.0

* Mon Mar 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.2-alt1
- + packaged gem with usage Ruby Policy 2.0
