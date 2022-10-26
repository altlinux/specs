%define        gemname async-process

Name:          gem-async-process
Version:       1.3.1
Release:       alt1
Summary:       Asynchronous process spawning
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-process
Vcs:           https://github.com/socketry/async-process.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(async) >= 0
BuildRequires: gem(async-io) >= 0
BuildRequires: gem(async-rspec) >= 1.1 gem(async-rspec) < 2
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async) >= 0
Requires:      gem(async-io) >= 0
Provides:      gem(async-process) = 1.3.1

%description
Asynchronous process spawning.


%package       -n gem-async-process-doc
Version:       1.3.1
Release:       alt1
Summary:       Asynchronous process spawning documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-process
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-process) = 1.3.1

%description   -n gem-async-process-doc
Asynchronous process spawning documentation files.

%description   -n gem-async-process-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-process.


%package       -n gem-async-process-devel
Version:       1.3.1
Release:       alt1
Summary:       Asynchronous process spawning development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-process
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-process) = 1.3.1
Requires:      gem(async-rspec) >= 1.1 gem(async-rspec) < 2
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-async-process-devel
Asynchronous process spawning development package.

%description   -n gem-async-process-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-process.


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

%files         -n gem-async-process-doc
%ruby_gemdocdir

%files         -n gem-async-process-devel


%changelog
* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- + packaged gem with Ruby Policy 2.0
