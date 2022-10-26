%define        gemname debugger-ruby_core_source

Name:          gem-debugger-ruby-core-source
Version:       1.3.8
Release:       alt1
Summary:       Provide Ruby core source files
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/cldwalker/debugger-ruby_core_source
Vcs:           https://github.com/cldwalker/debugger-ruby_core_source.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitar) >= 0.5.2
BuildRequires: gem(rake) >= 0.9.2 gem(rake) < 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(debugger-ruby_core_source) = 1.3.8


%description
Provide Ruby core source files for C extensions that need them.


%package       -n gem-debugger-ruby-core-source-doc
Version:       1.3.8
Release:       alt1
Summary:       Provide Ruby core source files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета debugger-ruby_core_source
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(debugger-ruby_core_source) = 1.3.8

%description   -n gem-debugger-ruby-core-source-doc
Provide Ruby core source files documentation files.

Provide Ruby core source files for C extensions that need them.

%description   -n gem-debugger-ruby-core-source-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета debugger-ruby_core_source.


%package       -n gem-debugger-ruby-core-source-devel
Version:       1.3.8
Release:       alt1
Summary:       Provide Ruby core source files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета debugger-ruby_core_source
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(debugger-ruby_core_source) = 1.3.8
Requires:      gem(minitar) >= 0.5.2
Requires:      gem(rake) >= 0.9.2 gem(rake) < 14

%description   -n gem-debugger-ruby-core-source-devel
Provide Ruby core source files development package.

Provide Ruby core source files for C extensions that need them.

%description   -n gem-debugger-ruby-core-source-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета debugger-ruby_core_source.


%prep
%setup
%autopatch -p1

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

%files         -n gem-debugger-ruby-core-source-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-debugger-ruby-core-source-devel
%doc README.md


%changelog
* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.8-alt1
- + packaged gem with Ruby Policy 2.0
