%define        gemname rspec-its

Name:          gem-rspec-its
Version:       1.3.0
Release:       alt1
Summary:       Provides "its" method formerly part of rspec-core
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rspec/rspec-its
Vcs:           https://github.com/rspec/rspec-its.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec-core) >= 3.0.0
BuildRequires: gem(rspec-expectations) >= 3.0.0
BuildRequires: gem(bundler) > 1.3.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.1.0 gem(rake) < 14
# BuildRequires: gem(cucumber) >= 1.3.8 gem(cucumber) < 1.4
# BuildRequires: gem(aruba) >= 0.6.2 gem(aruba) < 0.7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(rspec-core) >= 3.0.0
Requires:      gem(rspec-expectations) >= 3.0.0
Provides:      gem(rspec-its) = 1.3.0


%description
RSpec extension gem for attribute matching.


%package       -n gem-rspec-its-doc
Version:       1.3.0
Release:       alt1
Summary:       Provides "its" method formerly part of rspec-core documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-its
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-its) = 1.3.0

%description   -n gem-rspec-its-doc
Provides "its" method formerly part of rspec-core documentation files.

RSpec extension gem for attribute matching.

%description   -n gem-rspec-its-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-its.


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

%files         -n gem-rspec-its-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- + packaged gem with Ruby Policy 2.0
