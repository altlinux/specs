%define        gemname wwtd

Name:          gem-wwtd
Version:       1.4.1
Release:       alt1
Summary:       Travis simulator so you do not need to wait for the build
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/grosser/wwtd
Vcs:           https://github.com/grosser/wwtd.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(wwtd) = 1.4.1

%description
WWTD: Travis simulator - faster + no more waiting for build emails. Reads your
.travis.yml and runs what Travis would run (using rvm, rbenv, or chruby). No
more waiting for build emails!


%package       -n wwtd
Version:       1.4.1
Release:       alt1
Summary:       Travis simulator so you do not need to wait for the build executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета wwtd
Group:         Other
BuildArch:     noarch

Requires:      gem(wwtd) = 1.4.1

%description   -n wwtd
Travis simulator so you do not need to wait for the build executable(s).

WWTD: Travis simulator - faster + no more waiting for build emails. Reads your
.travis.yml and runs what Travis would run (using rvm, rbenv, or chruby). No
more waiting for build emails!

%description   -n wwtd -l ru_RU.UTF-8
Исполнямка для самоцвета wwtd.


%package       -n gem-wwtd-doc
Version:       1.4.1
Release:       alt1
Summary:       Travis simulator so you do not need to wait for the build documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета wwtd
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(wwtd) = 1.4.1

%description   -n gem-wwtd-doc
Travis simulator so you do not need to wait for the build documentation files.

WWTD: Travis simulator - faster + no more waiting for build emails. Reads your
.travis.yml and runs what Travis would run (using rvm, rbenv, or chruby). No
more waiting for build emails!

%description   -n gem-wwtd-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета wwtd.


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

%files         -n wwtd
%_bindir/wwtd

%files         -n gem-wwtd-doc
%ruby_gemdocdir


%changelog
* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- + packaged gem with Ruby Policy 2.0
