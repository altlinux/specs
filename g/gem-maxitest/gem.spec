%define        gemname maxitest

Name:          gem-maxitest
Version:       3.6.0
Release:       alt1
Summary:       Minitest + all the features you always wanted
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/grosser/maxitest
Vcs:           https://github.com/grosser/maxitest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.0.0 gem(minitest) < 6
BuildRequires: gem(bump) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(wwtd) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(minitest) >= 5.0.0 gem(minitest) < 6
Provides:      gem(maxitest) = 3.6.0

%description
Minitest + all the features you always wanted.


%package       -n mtest
Version:       3.6.0
Release:       alt1
Summary:       Minitest + all the features you always wanted executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета maxitest
Group:         Other
BuildArch:     noarch

Requires:      gem(maxitest) = 3.6.0

%description   -n mtest
Minitest + all the features you always wanted executable(s).

%description   -n mtest -l ru_RU.UTF-8
Исполнямка для самоцвета maxitest.


%package       -n gem-maxitest-doc
Version:       3.6.0
Release:       alt1
Summary:       Minitest + all the features you always wanted documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета maxitest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(maxitest) = 3.6.0

%description   -n gem-maxitest-doc
Minitest + all the features you always wanted documentation files.

%description   -n gem-maxitest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета maxitest.


%package       -n gem-maxitest-devel
Version:       3.6.0
Release:       alt1
Summary:       Minitest + all the features you always wanted development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета maxitest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(maxitest) = 3.6.0
Requires:      gem(bump) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(wwtd) >= 0

%description   -n gem-maxitest-devel
Minitest + all the features you always wanted development package.

%description   -n gem-maxitest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета maxitest.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc Readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n mtest
%doc Readme.md
%_bindir/mtest

%files         -n gem-maxitest-doc
%doc Readme.md
%ruby_gemdocdir

%files         -n gem-maxitest-devel
%doc Readme.md


%changelog
* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt1
- + packaged gem with Ruby Policy 2.0
