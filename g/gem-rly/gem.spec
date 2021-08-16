%define        gemname rly

Name:          gem-rly
Version:       0.2.3
Release:       alt1
Summary:       A simple ruby implementation of lex and yacc, based on Python's ply
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/farcaller/rly
Vcs:           https://github.com/farcaller/rly.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rly) = 0.2.3


%description
A simple ruby implementation of lex and yacc, based on Python's ply


%package       -n gem-rly-doc
Version:       0.2.3
Release:       alt1
Summary:       A simple ruby implementation of lex and yacc, based on Python's ply documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rly
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rly) = 0.2.3

%description   -n gem-rly-doc
A simple ruby implementation of lex and yacc, based on Python's ply
documentation files.

A simple ruby implementation of lex and yacc, based on Python's ply

%description   -n gem-rly-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rly.


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

%files         -n gem-rly-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Jun 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt1
- + packaged gem with Ruby Policy 2.0
