%define        gemname minitest-around

Name:          gem-minitest-around
Version:       0.5.0
Release:       alt1
Summary:       Around block for minitest
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/splattael/minitest-around
Vcs:           https://github.com/splattael/minitest-around.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rake) >= 0
# BuildRequires: gem(cucumber) >= 2.4.0 gem(cucumber) < 2.5
BuildRequires: gem(bump) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) >= 5.0
Provides:      gem(minitest-around) = 0.5.0


%description
Alternative for setup/teardown dance.


%package       -n gem-minitest-around-doc
Version:       0.5.0
Release:       alt1
Summary:       Around block for minitest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-around
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-around) = 0.5.0

%description   -n gem-minitest-around-doc
Around block for minitest documentation files.

Alternative for setup/teardown dance.

%description   -n gem-minitest-around-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-around.


%package       -n gem-minitest-around-devel
Version:       0.5.0
Release:       alt1
Summary:       Around block for minitest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-around
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-around) = 0.5.0
Requires:      gem(rdoc) >= 0
Requires:      gem(rake) >= 0
# Requires:      gem(cucumber) >= 2.4.0 gem(cucumber) < 2.5
Requires:      gem(bump) >= 0

%description   -n gem-minitest-around-devel
Around block for minitest development package.

Alternative for setup/teardown dance.

%description   -n gem-minitest-around-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-around.


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

%files         -n gem-minitest-around-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-minitest-around-devel
%doc README.md


%changelog
* Sun Jul 18 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0
