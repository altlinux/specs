%define        gemname pry-byebug

Name:          gem-pry-byebug
Version:       3.9.0
Release:       alt1
Summary:       Fast debugging with Pry
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/deivid-rodriguez/pry-byebug
Vcs:           https://github.com/deivid-rodriguez/pry-byebug.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(byebug) >= 11.0 gem(byebug) < 12
BuildRequires: gem(pry) >= 0.13.0 gem(pry) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
Requires:      gem(byebug) >= 11.0 gem(byebug) < 12
Requires:      gem(pry) >= 0.13.0 gem(pry) < 1
Provides:      gem(pry-byebug) = 3.9.0


%description
Combine 'pry' with 'byebug'. Adds 'step', 'next', 'finish', 'continue' and
'break' commands to control execution.


%package       -n gem-pry-byebug-doc
Version:       3.9.0
Release:       alt1
Summary:       Fast debugging with Pry documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pry-byebug
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pry-byebug) = 3.9.0

%description   -n gem-pry-byebug-doc
Fast debugging with Pry documentation files.

Combine 'pry' with 'byebug'. Adds 'step', 'next', 'finish', 'continue' and
'break' commands to control execution.

%description   -n gem-pry-byebug-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pry-byebug.


%package       -n gem-pry-byebug-devel
Version:       3.9.0
Release:       alt1
Summary:       Fast debugging with Pry development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pry-byebug
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pry-byebug) = 3.9.0

%description   -n gem-pry-byebug-devel
Fast debugging with Pry development package.

Combine 'pry' with 'byebug'. Adds 'step', 'next', 'finish', 'continue' and
'break' commands to control execution.

%description   -n gem-pry-byebug-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pry-byebug.


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

%files         -n gem-pry-byebug-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-pry-byebug-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 3.9.0-alt1
- + packaged gem with Ruby Policy 2.0
