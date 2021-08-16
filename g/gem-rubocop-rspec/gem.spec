%define        gemname rubocop-rspec

Name:          gem-rubocop-rspec
Version:       2.4.0
Release:       alt1
Summary:       Code style checking for RSpec files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop/rubocop-rspec
Vcs:           https://github.com/rubocop/rubocop-rspec.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 1.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-ast) >= 1.1.0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.4 gem(rspec) < 4
BuildRequires: gem(rubocop-performance) >= 1.7 gem(rubocop-performance) < 2
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(yard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(rubocop) >= 1.0 gem(rubocop) < 2
Requires:      gem(rubocop-ast) >= 1.1.0
Provides:      gem(rubocop-rspec) = 2.4.0


%description
Code style checking for RSpec files. A plugin for the RuboCop code style
enforcing & linting tool.


%package       -n gem-rubocop-rspec-doc
Version:       2.4.0
Release:       alt1
Summary:       Code style checking for RSpec files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-rspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-rspec) = 2.4.0

%description   -n gem-rubocop-rspec-doc
Code style checking for RSpec files documentation files.

Code style checking for RSpec files. A plugin for the RuboCop code style
enforcing & linting tool.

%description   -n gem-rubocop-rspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-rspec.


%package       -n gem-rubocop-rspec-devel
Version:       2.4.0
Release:       alt1
Summary:       Code style checking for RSpec files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-rspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-rspec) = 2.4.0
Requires:      gem(rack) >= 0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 3.4 gem(rspec) < 4
Requires:      gem(rubocop-performance) >= 1.7 gem(rubocop-performance) < 2
Requires:      gem(simplecov) >= 0.17 gem(simplecov) < 1
Requires:      gem(yard) >= 0

%description   -n gem-rubocop-rspec-devel
Code style checking for RSpec files development package.

Code style checking for RSpec files. A plugin for the RuboCop code style
enforcing & linting tool.

%description   -n gem-rubocop-rspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-rspec.


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

%files         -n gem-rubocop-rspec-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-rspec-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- + packaged gem with Ruby Policy 2.0
