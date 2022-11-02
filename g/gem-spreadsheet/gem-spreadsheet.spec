%define        gemname spreadsheet

Name:          gem-spreadsheet
Version:       1.3.0
Release:       alt1
Summary:       The Spreadsheet Library is designed to read and write Spreadsheet Documents
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/zdavatz/spreadsheet/
Vcs:           https://github.com/zdavatz/spreadsheet.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(ruby-ole) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(ruby-ole) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ruby-ole) >= 0
Provides:      gem(spreadsheet) = 1.3.0


%description
As of version 0.6.0, only Microsoft Excel compatible spreadsheets are supported


%package       -n xlsopcodes
Version:       1.3.0
Release:       alt1
Summary:       The Spreadsheet Library is designed to read and write Spreadsheet Documents executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета spreadsheet
Group:         Other
BuildArch:     noarch

Requires:      gem(spreadsheet) = 1.3.0

%description   -n xlsopcodes
The Spreadsheet Library is designed to read and write Spreadsheet Documents
executable(s).

As of version 0.6.0, only Microsoft Excel compatible spreadsheets are supported

%description   -n xlsopcodes -l ru_RU.UTF-8
Исполнямка для самоцвета spreadsheet.


%package       -n gem-spreadsheet-doc
Version:       1.3.0
Release:       alt1
Summary:       The Spreadsheet Library is designed to read and write Spreadsheet Documents documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета spreadsheet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(spreadsheet) = 1.3.0

%description   -n gem-spreadsheet-doc
The Spreadsheet Library is designed to read and write Spreadsheet Documents
documentation files.

As of version 0.6.0, only Microsoft Excel compatible spreadsheets are supported

%description   -n gem-spreadsheet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета spreadsheet.


%package       -n gem-spreadsheet-devel
Version:       1.3.0
Release:       alt1
Summary:       The Spreadsheet Library is designed to read and write Spreadsheet Documents development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета spreadsheet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(spreadsheet) = 1.3.0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(simplecov) >= 0

%description   -n gem-spreadsheet-devel
The Spreadsheet Library is designed to read and write Spreadsheet Documents
development package.

As of version 0.6.0, only Microsoft Excel compatible spreadsheets are supported

%description   -n gem-spreadsheet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета spreadsheet.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n xlsopcodes
%_bindir/xlsopcodes

%files         -n gem-spreadsheet-doc
%ruby_gemdocdir

%files         -n gem-spreadsheet-devel


%changelog
* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- + packaged gem with Ruby Policy 2.0
