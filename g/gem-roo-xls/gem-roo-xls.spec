%define        gemname roo-xls

Name:          gem-roo-xls
Version:       1.2.0
Release:       alt1
Summary:       Roo::Excel can access the contents of classic xls files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/roo-rb/roo-xls
Vcs:           https://github.com/roo-rb/roo-xls.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.7
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(shoulda) >= 0
BuildRequires: gem(rspec) >= 3.0.0
BuildRequires: gem(simplecov) >= 0.9.0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(guard-rspec) >= 4.3.1
BuildRequires: gem(guard-bundler) >= 0
BuildRequires: gem(guard-preek) >= 0
BuildRequires: gem(guard-rubocop) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(transpec) >= 0
BuildRequires: gem(roo) >= 2.0.0 gem(roo) < 3
BuildRequires: gem(spreadsheet) > 0.9.0
BuildRequires: gem(nokogiri) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(roo) >= 2.0.0 gem(roo) < 3
Requires:      gem(spreadsheet) > 0.9.0
Requires:      gem(nokogiri) >= 0
Provides:      gem(roo-xls) = 1.2.0


%description
Roo can access the contents of various spreadsheet files. It can handle
* OpenOffice
* Excel
* Google spreadsheets
* Excelx
* LibreOffice
* CSV


%package       -n gem-roo-xls-doc
Version:       1.2.0
Release:       alt1
Summary:       Roo::Excel can access the contents of classic xls files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета roo-xls
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(roo-xls) = 1.2.0

%description   -n gem-roo-xls-doc
Roo::Excel can access the contents of classic xls files documentation
files.

Roo can access the contents of various spreadsheet files. It can handle
* OpenOffice
* Excel
* Google spreadsheets
* Excelx
* LibreOffice
* CSV

%description   -n gem-roo-xls-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета roo-xls.


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

%files         -n gem-roo-xls-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
