%define        gemname singleton

Name:          gem-singleton
Version:       0.1.1
Release:       alt1
Summary:       The Singleton module implements the Singleton pattern
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/singleton
Vcs:           https://github.com/ruby/singleton.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(singleton) = 0.1.1


%description
The Singleton module implements the Singleton pattern.


%package       -n gem-singleton-doc
Version:       0.1.1
Release:       alt1
Summary:       The Singleton module implements the Singleton pattern documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета singleton
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(singleton) = 0.1.1

%description   -n gem-singleton-doc
The Singleton module implements the Singleton pattern documentation files.

%description   -n gem-singleton-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета singleton.


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

%files         -n gem-singleton-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Oct 04 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt1
- + packaged gem with Ruby Policy 2.0
