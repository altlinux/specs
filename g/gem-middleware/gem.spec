%define        gemname middleware

Name:          gem-middleware
Version:       0.1.0
Release:       alt1
Summary:       Generalized implementation of the middleware abstraction for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mitchellh/middleware
Vcs:           https://github.com/mitchellh/middleware.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(middleware) = 0.1.0


%description
Generalized implementation of the middleware abstraction for Ruby.


%package       -n gem-middleware-doc
Version:       0.1.0
Release:       alt1
Summary:       Generalized implementation of the middleware abstraction for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета middleware
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(middleware) = 0.1.0

%description   -n gem-middleware-doc
Generalized implementation of the middleware abstraction for Ruby documentation
files.

Generalized implementation of the middleware abstraction for Ruby.

%description   -n gem-middleware-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета middleware.


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

%files         -n gem-middleware-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Jun 07 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- + packaged gem with Ruby Policy 2.0
