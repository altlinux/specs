%define        gemname rubocop-checkstyle_formatter

Name:          gem-rubocop-checkstyle-formatter
Version:       0.4.0
Release:       alt1
Summary:       A formatter for rubocop that outputs in checkstyle format
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/eitoball/rubocop-checkstyle_formatter
Vcs:           https://github.com/eitoball/rubocop-checkstyle_formatter.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 0.35.1 gem(rubocop) < 2
BuildRequires: gem(appraisal) >= 1.0.0 gem(appraisal) < 3
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.1 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.5.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency appraisal >= 2.4.0,appraisal < 3
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(rubocop) >= 0.35.1 gem(rubocop) < 2
Provides:      gem(rubocop-checkstyle_formatter) = 0.4.0


%description
A formatter for rubocop that outputs in checkstyle format


%package       -n gem-rubocop-checkstyle-formatter-doc
Version:       0.4.0
Release:       alt1
Summary:       A formatter for rubocop that outputs in checkstyle format documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-checkstyle_formatter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-checkstyle_formatter) = 0.4.0

%description   -n gem-rubocop-checkstyle-formatter-doc
A formatter for rubocop that outputs in checkstyle format documentation
files.

A formatter for rubocop that outputs in checkstyle format

%description   -n gem-rubocop-checkstyle-formatter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-checkstyle_formatter.


%package       -n gem-rubocop-checkstyle-formatter-devel
Version:       0.4.0
Release:       alt1
Summary:       A formatter for rubocop that outputs in checkstyle format development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-checkstyle_formatter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-checkstyle_formatter) = 0.4.0
Requires:      gem(appraisal) >= 1.0.0 gem(appraisal) < 3
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(rake) >= 10.1 gem(rake) < 14
Requires:      gem(rspec) >= 3.5.0 gem(rspec) < 4

%description   -n gem-rubocop-checkstyle-formatter-devel
A formatter for rubocop that outputs in checkstyle format development
package.

A formatter for rubocop that outputs in checkstyle format

%description   -n gem-rubocop-checkstyle-formatter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-checkstyle_formatter.


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

%files         -n gem-rubocop-checkstyle-formatter-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-checkstyle-formatter-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with Ruby Policy 2.0
