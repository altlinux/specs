%define        gemname rfc

Name:          gem-rfc
Version:       0.2.0
Release:       alt1
Summary:       rfc-0.2.0
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/p-mongo/rfc
Vcs:           https://github.com/p-mongo/rfc.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec-core) >= 3.0 gem(rspec-core) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec-core) >= 3.0 gem(rspec-core) < 4
Provides:      gem(rfc) = 0.2.0


%description
RSpec Formatter Collection including a concise insta-failing formatter


%package       -n gem-rfc-doc
Version:       0.2.0
Release:       alt1
Summary:       rfc-0.2.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rfc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rfc) = 0.2.0

%description   -n gem-rfc-doc
rfc-0.2.0 documentation files.

RSpec Formatter Collection including a concise insta-failing formatter

%description   -n gem-rfc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rfc.


%package       -n gem-rfc-devel
Version:       0.2.0
Release:       alt1
Summary:       rfc-0.2.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rfc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rfc) = 0.2.0

%description   -n gem-rfc-devel
rfc-0.2.0 development package.

RSpec Formatter Collection including a concise insta-failing formatter

%description   -n gem-rfc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rfc.


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

%files         -n gem-rfc-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rfc-devel
%doc README.md


%changelog
* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
