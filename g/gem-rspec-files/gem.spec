%define        gemname rspec-files

Name:          gem-rspec-files
Version:       1.1.1
Release:       alt1
Summary:       RSpec helpers for buffering and detecting file descriptor leaks
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/rspec-files
Vcs:           https://github.com/socketry/rspec-files.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Provides:      gem(rspec-files) = 1.1.1


%description
RSpec helpers for buffering and detecting file descriptor leaks.


%package       -n gem-rspec-files-doc
Version:       1.1.1
Release:       alt1
Summary:       RSpec helpers for buffering and detecting file descriptor leaks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-files
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-files) = 1.1.1

%description   -n gem-rspec-files-doc
RSpec helpers for buffering and detecting file descriptor leaks documentation
files.

%description   -n gem-rspec-files-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-files.


%package       -n gem-rspec-files-devel
Version:       1.1.1
Release:       alt1
Summary:       RSpec helpers for buffering and detecting file descriptor leaks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-files
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-files) = 1.1.1
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0

%description   -n gem-rspec-files-devel
RSpec helpers for buffering and detecting file descriptor leaks development
package.

%description   -n gem-rspec-files-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-files.


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

%files         -n gem-rspec-files-doc
%ruby_gemdocdir

%files         -n gem-rspec-files-devel


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
