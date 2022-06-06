%define        gemname debase-ruby_core_source

Name:          gem-debase-ruby-core-source
Version:       0.10.15
Release:       alt1
Summary:       Provide Ruby core source files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-debug/debase-ruby_core_source
Vcs:           https://github.com/ruby-debug/debase-ruby_core_source.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitar) >= 0.5.2
BuildRequires: gem(rake) >= 0.9.2 gem(rake) < 14
BuildRequires: gem(minitar-cli) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(debase-ruby_core_source) = 0.10.15


%description
Provide Ruby core source files for C extensions that need them.


%package       -n gem-debase-ruby-core-source-doc
Version:       0.10.15
Release:       alt1
Summary:       Provide Ruby core source files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета debase-ruby_core_source
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(debase-ruby_core_source) = 0.10.15

%description   -n gem-debase-ruby-core-source-doc
Provide Ruby core source files documentation files.

Provide Ruby core source files for C extensions that need them.

%description   -n gem-debase-ruby-core-source-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета debase-ruby_core_source.


%package       -n gem-debase-ruby-core-source-devel
Version:       0.10.15
Release:       alt1
Summary:       Provide Ruby core source files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета debase-ruby_core_source
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(debase-ruby_core_source) = 0.10.15
Requires:      gem(minitar) >= 0.5.2
Requires:      gem(rake) >= 0.9.2 gem(rake) < 14
Requires:      gem(minitar-cli) >= 0

%description   -n gem-debase-ruby-core-source-devel
Provide Ruby core source files development package.

Provide Ruby core source files for C extensions that need them.

%description   -n gem-debase-ruby-core-source-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета debase-ruby_core_source.


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc OLD_README README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-debase-ruby-core-source-doc
%doc OLD_README README.md
%ruby_gemdocdir

%files         -n gem-debase-ruby-core-source-devel
%doc OLD_README README.md


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.10.15-alt1
- + packaged gem with Ruby Policy 2.0
