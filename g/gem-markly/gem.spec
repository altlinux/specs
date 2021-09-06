%define        gemname markly

Name:          gem-markly
Version:       0.6.0
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/markly
Vcs:           https://github.com/ioquatix/markly.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bake) >= 0
BuildRequires: gem(minitest) >= 5.6 gem(minitest) < 6
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0.9 gem(rake-compiler) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Provides:      gem(markly) = 0.6.0


%description
CommonMark parser and renderer. Written in C, wrapped in Ruby.


%package       -n markly
Version:       0.6.0
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета markly
Group:         Other
BuildArch:     noarch

Requires:      gem(markly) = 0.6.0

%description   -n markly
CommonMark parser and renderer. Written in C, wrapped in Ruby executable(s).

%description   -n markly -l ru_RU.UTF-8
Исполнямка для самоцвета markly.


%package       -n gem-markly-doc
Version:       0.6.0
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета markly
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(markly) = 0.6.0

%description   -n gem-markly-doc
CommonMark parser and renderer. Written in C, wrapped in Ruby documentation
files.

%description   -n gem-markly-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета markly.


%package       -n gem-markly-devel
Version:       0.6.0
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета markly
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(markly) = 0.6.0
Requires:      gem(bake) >= 0
Requires:      gem(minitest) >= 5.6 gem(minitest) < 6
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rake-compiler) >= 0.9 gem(rake-compiler) < 2

%description   -n gem-markly-devel
CommonMark parser and renderer. Written in C, wrapped in Ruby development
package.

%description   -n gem-markly-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета markly.


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
%ruby_gemextdir

%files         -n markly
%_bindir/markly

%files         -n gem-markly-doc
%ruby_gemdocdir

%files         -n gem-markly-devel
%ruby_includedir/*


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with Ruby Policy 2.0
