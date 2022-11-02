%define        gemname roo

Name:          gem-roo
Version:       2.9.0
Release:       alt1
Summary:       Roo can access the contents of various spreadsheet files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/roo-rb/roo
Vcs:           https://github.com/roo-rb/roo.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 5.4
BuildRequires: gem(rack) < 3
BuildRequires: gem(matrix) >= 0
BuildRequires: gem(shoulda) >= 0
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(rspec) >= 3.0.0
BuildRequires: gem(simplecov) >= 0.9.0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(guard-rspec) >= 4.3.1
BuildRequires: gem(guard-minitest) >= 0
BuildRequires: gem(guard-bundler) >= 0
BuildRequires: gem(guard-rubocop) >= 0
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(nokogiri) >= 1 gem(nokogiri) < 2
BuildRequires: gem(rubyzip) >= 1.3.0 gem(rubyzip) < 3.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency activesupport >= 6.1.3.2,activesupport < 7
Requires:      gem(nokogiri) >= 1 gem(nokogiri) < 2
Requires:      gem(rubyzip) >= 1.3.0 gem(rubyzip) < 3.0.0
Provides:      gem(roo) = 2.9.0


%description
Roo can access the contents of various spreadsheet files. It can handle
* OpenOffice
* Excelx
* LibreOffice
* CSV


%package       -n gem-roo-doc
Version:       2.9.0
Release:       alt1
Summary:       Roo can access the contents of various spreadsheet files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета roo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(roo) = 2.9.0

%description   -n gem-roo-doc
Roo can access the contents of various spreadsheet files documentation
files.

Roo can access the contents of various spreadsheet files. It can handle
* OpenOffice
* Excelx
* LibreOffice
* CSV

%description   -n gem-roo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета roo.


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

%files         -n gem-roo-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 2.9.0-alt1
- + packaged gem with Ruby Policy 2.0
