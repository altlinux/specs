%define        gemname hurley

Name:          gem-hurley
Version:       0.2
Release:       alt1
Summary:       HTTP client wrapper
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/hurley
Vcs:           https://github.com/lostisland/hurley.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.0 gem(bundler) < 3
BuildRequires: gem(addressable) >= 2.3.6 gem(addressable) < 3
BuildRequires: gem(rake) >= 10.4.0
BuildRequires: gem(minitest) >= 5.6 gem(minitest) < 6
BuildRequires: gem(sinatra) >= 1.4.5 gem(sinatra) < 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency sinatra >= 2.1.0,sinatra < 3
Provides:      gem(hurley) = 0.2


%description
Hurley provides a common interface for working with different HTTP adapters.


%package       -n gem-hurley-doc
Version:       0.2
Release:       alt1
Summary:       HTTP client wrapper documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hurley
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hurley) = 0.2

%description   -n gem-hurley-doc
HTTP client wrapper documentation files.

Hurley provides a common interface for working with different HTTP adapters.

%description   -n gem-hurley-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hurley.


%package       -n gem-hurley-devel
Version:       0.2
Release:       alt1
Summary:       HTTP client wrapper development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hurley
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hurley) = 0.2
Requires:      gem(bundler) >= 1.0 gem(bundler) < 3
Requires:      gem(addressable) >= 2.3.6 gem(addressable) < 3
Requires:      gem(rake) >= 10.4.0
Requires:      gem(minitest) >= 5.6 gem(minitest) < 6
Requires:      gem(sinatra) >= 1.4.5 gem(sinatra) < 3

%description   -n gem-hurley-devel
HTTP client wrapper development package.

Hurley provides a common interface for working with different HTTP adapters.

%description   -n gem-hurley-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hurley.


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

%files         -n gem-hurley-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hurley-devel
%doc README.md


%changelog
* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.2-alt1
- + packaged gem with Ruby Policy 2.0
