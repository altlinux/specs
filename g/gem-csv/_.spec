%define        gemname csv

Name:          gem-csv
Version:       3.2.0
Release:       alt1
Summary:       CSV Reading and Writing
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/csv
Vcs:           https://github.com/ruby/csv.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(benchmark_driver) >= 0
BuildRequires: gem(test-unit) >= 3.3.5 gem(test-unit) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(csv) = 3.2.0


%description
This library provides a complete interface to CSV files and data. It offers
tools to enable you to read and write to and from Strings or IO objects, as
needed.


%package       -n gem-csv-doc
Version:       3.2.0
Release:       alt1
Summary:       CSV Reading and Writing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета csv
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(csv) = 3.2.0

%description   -n gem-csv-doc
CSV Reading and Writing documentation files.

This library provides a complete interface to CSV files and data. It offers
tools to enable you to read and write to and from Strings or IO objects, as
needed.

%description   -n gem-csv-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета csv.


%package       -n gem-csv-devel
Version:       3.2.0
Release:       alt1
Summary:       CSV Reading and Writing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета csv
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(csv) = 3.2.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(benchmark_driver) >= 0
Requires:      gem(test-unit) >= 3.3.5 gem(test-unit) < 4

%description   -n gem-csv-devel
CSV Reading and Writing development package.

This library provides a complete interface to CSV files and data. It offers
tools to enable you to read and write to and from Strings or IO objects, as
needed.

%description   -n gem-csv-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета csv.


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

%files         -n gem-csv-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-csv-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- ^ 3.1.2 -> 3.2.0

* Mon Mar 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.2-alt1
- + packaged gem with usage Ruby Policy 2.0
