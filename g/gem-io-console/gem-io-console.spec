%define        gemname io-console

Name:          gem-io-console
Version:       0.5.11
Release:       alt1
Summary:       Console interface
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/io-console
Vcs:           https://github.com/ruby/io-console.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(rake-compiler) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(io-console) = 0.5.11


%description
add console capabilities to IO instances.


%package       -n gem-io-console-doc
Version:       0.5.11
Release:       alt1
Summary:       Console interface documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета io-console
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(io-console) = 0.5.11

%description   -n gem-io-console-doc
Console interface documentation files.

add console capabilities to IO instances.

%description   -n gem-io-console-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета io-console.


%package       -n gem-io-console-devel
Version:       0.5.11
Release:       alt1
Summary:       Console interface development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета io-console
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(io-console) = 0.5.11
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(rake-compiler) >= 0

%description   -n gem-io-console-devel
Console interface development package.

add console capabilities to IO instances.

%description   -n gem-io-console-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета io-console.


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
%ruby_gemextdir

%files         -n gem-io-console-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-io-console-devel
%doc README.md


%changelog
* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.11-alt1
- + packaged gem with Ruby Policy 2.0
