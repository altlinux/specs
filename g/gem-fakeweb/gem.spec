%define        gemname fakeweb

Name:          gem-fakeweb
Version:       1.3.0
Release:       alt1
Summary:       A tool for faking responses to HTTP requests
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/chrisk/fakeweb
Vcs:           https://github.com/chrisk/fakeweb.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(mocha) >= 0.9.5 gem(mocha) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_ignore_names samuel
Provides:      gem(fakeweb) = 1.3.0


%description
FakeWeb is a helper for faking web requests in Ruby. It works at a global level,
without modifying code or writing extensive stubs.


%package       -n gem-fakeweb-doc
Version:       1.3.0
Release:       alt1
Summary:       A tool for faking responses to HTTP requests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fakeweb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fakeweb) = 1.3.0

%description   -n gem-fakeweb-doc
A tool for faking responses to HTTP requests documentation files.

FakeWeb is a helper for faking web requests in Ruby. It works at a global level,
without modifying code or writing extensive stubs.

%description   -n gem-fakeweb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fakeweb.


%package       -n gem-fakeweb-devel
Version:       1.3.0
Release:       alt1
Summary:       A tool for faking responses to HTTP requests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fakeweb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fakeweb) = 1.3.0
Requires:      gem(mocha) >= 0.9.5 gem(mocha) < 2

%description   -n gem-fakeweb-devel
A tool for faking responses to HTTP requests development package.

FakeWeb is a helper for faking web requests in Ruby. It works at a global level,
without modifying code or writing extensive stubs.

%description   -n gem-fakeweb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fakeweb.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-fakeweb-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-fakeweb-devel
%doc README.rdoc


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- + packaged gem with Ruby Policy 2.0
