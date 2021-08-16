%define        gemname rubocop-performance

Name:          gem-rubocop-performance
Version:       1.11.3
Release:       alt1
Summary:       Automatic performance checking tool for Ruby code
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop/rubocop-performance
Vcs:           https://github.com/rubocop/rubocop-performance/.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 1.7.0 gem(rubocop) < 2.0
BuildRequires: gem(rubocop-ast) >= 0.4.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
Requires:      gem(rubocop) >= 1.7.0 gem(rubocop) < 2.0
Requires:      gem(rubocop-ast) >= 0.4.0
Provides:      gem(rubocop-performance) = 1.11.3


%description
A collection of RuboCop cops to check for performance optimizations in Ruby
code.


%package       -n gem-rubocop-performance-doc
Version:       1.11.3
Release:       alt1
Summary:       Automatic performance checking tool for Ruby code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-performance
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-performance) = 1.11.3

%description   -n gem-rubocop-performance-doc
Automatic performance checking tool for Ruby code documentation files.

A collection of RuboCop cops to check for performance optimizations in Ruby
code.

%description   -n gem-rubocop-performance-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-performance.


%package       -n gem-rubocop-performance-devel
Version:       1.11.3
Release:       alt1
Summary:       Automatic performance checking tool for Ruby code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-performance
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-performance) = 1.11.3

%description   -n gem-rubocop-performance-devel
Automatic performance checking tool for Ruby code development package.

A collection of RuboCop cops to check for performance optimizations in Ruby
code.

%description   -n gem-rubocop-performance-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-performance.


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

%files         -n gem-rubocop-performance-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-performance-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.11.3-alt1
- + packaged gem with Ruby Policy 2.0
