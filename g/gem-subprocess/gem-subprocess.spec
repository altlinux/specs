%define        gemname subprocess

Name:          gem-subprocess
Version:       1.5.6
Release:       alt1
Summary:       A port of Python's subprocess module to Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/stripe/subprocess
Vcs:           https://github.com/stripe/subprocess.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(rake) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(sord) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(subprocess) = 1.5.6


%description
Control and communicate with spawned processes


%package       -n gem-subprocess-doc
Version:       1.5.6
Release:       alt1
Summary:       A port of Python's subprocess module to Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета subprocess
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(subprocess) = 1.5.6

%description   -n gem-subprocess-doc
A port of Python's subprocess module to Ruby documentation files.

Control and communicate with spawned processes

%description   -n gem-subprocess-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета subprocess.


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

%files         -n gem-subprocess-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 1.5.6-alt1
- + packaged gem with Ruby Policy 2.0
