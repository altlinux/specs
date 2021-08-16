%define        gemname riot

Name:          gem-riot
Version:       0.12.7
Release:       alt1
Summary:       An extremely fast, expressive, and context-driven unit-testing framework
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/thumblemonks/riot
Vcs:           https://github.com/thumblemonks/riot.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rr) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rr) >= 0
Provides:      gem(riot) = 0.12.7


%description
An extremely fast, expressive, and context-driven unit-testing framework. A
replacement for all other testing frameworks. Protest the slow test.


%package       -n gem-riot-doc
Version:       0.12.7
Release:       alt1
Summary:       An extremely fast, expressive, and context-driven unit-testing framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета riot
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(riot) = 0.12.7

%description   -n gem-riot-doc
An extremely fast, expressive, and context-driven unit-testing framework
documentation files.

An extremely fast, expressive, and context-driven unit-testing framework. A
replacement for all other testing frameworks. Protest the slow test.

%description   -n gem-riot-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета riot.


%package       -n gem-riot-devel
Version:       0.12.7
Release:       alt1
Summary:       An extremely fast, expressive, and context-driven unit-testing framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета riot
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(riot) = 0.12.7

%description   -n gem-riot-devel
An extremely fast, expressive, and context-driven unit-testing framework
development package.

An extremely fast, expressive, and context-driven unit-testing framework. A
replacement for all other testing frameworks. Protest the slow test.

%description   -n gem-riot-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета riot.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-riot-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-riot-devel
%doc README.markdown


%changelog
* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.12.7-alt1
- + packaged gem with Ruby Policy 2.0
