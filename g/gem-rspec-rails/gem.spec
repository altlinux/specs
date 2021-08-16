%define        gemname rspec-rails

Name:          gem-rspec-rails
Version:       5.0.1
Release:       alt1
Summary:       RSpec for Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rspec/rspec-rails
Vcs:           https://github.com/rspec/rspec-rails.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(actionpack) >= 5.2
BuildRequires: gem(activesupport) >= 5.2
BuildRequires: gem(railties) >= 5.2
BuildRequires: gem(rspec-core) >= 3.10 gem(rspec-core) < 4
BuildRequires: gem(rspec-expectations) >= 3.10 gem(rspec-expectations) < 4
BuildRequires: gem(rspec-mocks) >= 3.10 gem(rspec-mocks) < 4
BuildRequires: gem(rspec-support) >= 3.10 gem(rspec-support) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(actionpack) >= 5.2
Requires:      gem(activesupport) >= 5.2
Requires:      gem(railties) >= 5.2
Requires:      gem(rspec-core) >= 3.10 gem(rspec-core) < 4
Requires:      gem(rspec-expectations) >= 3.10 gem(rspec-expectations) < 4
Requires:      gem(rspec-mocks) >= 3.10 gem(rspec-mocks) < 4
Requires:      gem(rspec-support) >= 3.10 gem(rspec-support) < 4
Provides:      gem(rspec-rails) = 5.0.1


%description
rspec-rails is a testing framework for Rails 5+.


%package       -n gem-rspec-rails-doc
Version:       5.0.1
Release:       alt1
Summary:       RSpec for Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-rails) = 5.0.1

%description   -n gem-rspec-rails-doc
RSpec for Rails documentation files.

rspec-rails is a testing framework for Rails 5+.

%description   -n gem-rspec-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-rails.


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

%files         -n gem-rspec-rails-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Jun 21 2021 Pavel Skrylev <majioa@altlinux.org> 5.0.1-alt1
- + packaged gem with Ruby Policy 2.0
