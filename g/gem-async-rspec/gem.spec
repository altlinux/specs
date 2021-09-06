%define        gemname async-rspec

Name:          gem-async-rspec
Version:       1.16.1
Release:       alt1
Summary:       Helpers for writing specs against the async gem
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-rspec
Vcs:           https://github.com/socketry/async-rspec.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rspec-files) >= 1.0 gem(rspec-files) < 2
BuildRequires: gem(rspec-memory) >= 1.0 gem(rspec-memory) < 2
BuildRequires: gem(async) >= 0
BuildRequires: gem(async-io) >= 0
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rspec-files) >= 1.0 gem(rspec-files) < 2
Requires:      gem(rspec-memory) >= 1.0 gem(rspec-memory) < 2
Provides:      gem(async-rspec) = 1.16.1

%description
Provides useful RSpec.shared_contexts for testing code that builds on top of
async.


%package       -n gem-async-rspec-doc
Version:       1.16.1
Release:       alt1
Summary:       Helpers for writing specs against the async gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-rspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-rspec) = 1.16.1

%description   -n gem-async-rspec-doc
Helpers for writing specs against the async gem documentation files.

Provides useful RSpec.shared_contexts for testing code that builds on top of
async.

%description   -n gem-async-rspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-rspec.


%package       -n gem-async-rspec-devel
Version:       1.16.1
Release:       alt1
Summary:       Helpers for writing specs against the async gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-rspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-rspec) = 1.16.1
Requires:      gem(async) >= 0
Requires:      gem(async-io) >= 0
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(covered) >= 0

%description   -n gem-async-rspec-devel
Helpers for writing specs against the async gem development package.

Provides useful RSpec.shared_contexts for testing code that builds on top of
async.

%description   -n gem-async-rspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-rspec.


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

%files         -n gem-async-rspec-doc
%ruby_gemdocdir

%files         -n gem-async-rspec-devel


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.16.1-alt1
- + packaged gem with Ruby Policy 2.0
