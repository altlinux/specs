%define        gemname gem_hadar

Name:          gem-gem-hadar
Version:       1.11.0
Release:       alt1
Summary:       Library for the development of Ruby Gems
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/flori/gem_hadar
Vcs:           https://github.com/flori/gem_hadar.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(tins) >= 1.0 gem(tins) < 2
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(yard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_alias_names gem_hadar,gem-hadar
Requires:      gem(tins) >= 1.0 gem(tins) < 2
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(yard) >= 0
Provides:      gem(gem_hadar) = 1.11.0


%description
This library contains some useful functionality to support the development of
Ruby Gems


%package       -n gem-gem-hadar-doc
Version:       1.11.0
Release:       alt1
Summary:       Library for the development of Ruby Gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gem_hadar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gem_hadar) = 1.11.0

%description   -n gem-gem-hadar-doc
Library for the development of Ruby Gems documentation files.

This library contains some useful functionality to support the development of
Ruby Gems

%description   -n gem-gem-hadar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gem_hadar.


%package       -n gem-gem-hadar-devel
Version:       1.11.0
Release:       alt1
Summary:       Library for the development of Ruby Gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gem_hadar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gem_hadar) = 1.11.0
Requires:      gem(gem_hadar) >= 1.11.0 gem(gem_hadar) < 1.12

%description   -n gem-gem-hadar-devel
Library for the development of Ruby Gems development package.

This library contains some useful functionality to support the development of
Ruby Gems

%description   -n gem-gem-hadar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gem_hadar.


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

%files         -n gem-gem-hadar-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-gem-hadar-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.11.0-alt1
- + packaged gem with Ruby Policy 2.0
