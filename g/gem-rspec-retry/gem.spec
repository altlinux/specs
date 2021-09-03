%define        gemname rspec-retry

Name:          gem-rspec-retry
Version:       0.6.2
Release:       alt1
Summary:       retry intermittently failing rspec examples
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/NoRedInk/rspec-retry
Vcs:           https://github.com/noredink/rspec-retry.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec-core) > 3.3
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(byebug) >= 9.0.6 gem(byebug) < 12
BuildRequires: gem(pry-byebug) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency byebug >= 11.1.3,byebug < 12
Requires:      gem(rspec-core) > 3.3
Provides:      gem(rspec-retry) = 0.6.2


%description
retry intermittently failing rspec examples


%package       -n gem-rspec-retry-doc
Version:       0.6.2
Release:       alt1
Summary:       retry intermittently failing rspec examples documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-retry
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-retry) = 0.6.2

%description   -n gem-rspec-retry-doc
retry intermittently failing rspec examples documentation files.

retry intermittently failing rspec examples

%description   -n gem-rspec-retry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-retry.


%package       -n gem-rspec-retry-devel
Version:       0.6.2
Release:       alt1
Summary:       retry intermittently failing rspec examples development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-retry
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-retry) = 0.6.2
Requires:      gem(appraisal) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(byebug) >= 9.0.6 gem(byebug) < 12
Requires:      gem(pry-byebug) >= 0

%description   -n gem-rspec-retry-devel
retry intermittently failing rspec examples development package.

retry intermittently failing rspec examples

%description   -n gem-rspec-retry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-retry.


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

%files         -n gem-rspec-retry-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-retry-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.2-alt1
- + packaged gem with Ruby Policy 2.0
