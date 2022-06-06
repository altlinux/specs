%define        gemname rvm

Name:          gem-rvm
Version:       1.11.3.9
Release:       alt1
Summary:       RVM Ruby Gem Library
License:       MIT
Group:         Development/Ruby
Url:           http://rvm.io/
Vcs:           https://github.com/rvm/rvm-gem.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rvm) = 1.11.3.9


%description
RVM ~ Ruby Environment Manager ~ Ruby Gem Library.


%package       -n gem-rvm-doc
Version:       1.11.3.9
Release:       alt1
Summary:       RVM Ruby Gem Library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rvm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rvm) = 1.11.3.9

%description   -n gem-rvm-doc
RVM Ruby Gem Library documentation files.

RVM ~ Ruby Environment Manager ~ Ruby Gem Library.

%description   -n gem-rvm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rvm.


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

%files         -n gem-rvm-doc
%ruby_gemdocdir


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.11.3.9-alt1
- + packaged gem with Ruby Policy 2.0
