%define        gemname rocco

Name:          gem-rocco
Version:       0.8.2
Release:       alt1
Summary:       Docco in Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://rtomayko.github.com/rocco/
Vcs:           https://github.com/rtomayko/rocco.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(mustache) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(redcarpet) >= 0
Requires:      gem(mustache) >= 0
Provides:      gem(rocco) = 0.8.2


%description
Rocco is  a quick-and-dirty,  literate-programming-style documentation
generator for Ruby.


%package       -n rocco
Version:       0.8.2
Release:       alt1
Summary:       Docco in Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rocco
Group:         Other
BuildArch:     noarch

Requires:      gem(rocco) = 0.8.2

%description   -n rocco
Docco in Ruby executable(s).

Rocco is  a quick-and-dirty,  literate-programming-style documentation
generator for Ruby.

%description   -n rocco -l ru_RU.UTF-8
Исполнямка для самоцвета rocco.


%package       -n gem-rocco-doc
Version:       0.8.2
Release:       alt1
Summary:       Docco in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rocco
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rocco) = 0.8.2

%description   -n gem-rocco-doc
Docco in Ruby documentation files.

Rocco is  a quick-and-dirty,  literate-programming-style documentation
generator for Ruby.

%description   -n gem-rocco-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rocco.


%package       -n gem-rocco-devel
Version:       0.8.2
Release:       alt1
Summary:       Docco in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rocco
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rocco) = 0.8.2

%description   -n gem-rocco-devel
Docco in Ruby development package.

Rocco is  a quick-and-dirty,  literate-programming-style documentation
generator for Ruby.

%description   -n gem-rocco-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rocco.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n rocco
%doc README
%_bindir/rocco

%files         -n gem-rocco-doc
%doc README
%ruby_gemdocdir

%files         -n gem-rocco-devel
%doc README


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.8.2-alt1
- + packaged gem with Ruby Policy 2.0
