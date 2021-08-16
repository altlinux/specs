%define        gemname contracts

Name:          gem-contracts
Version:       0.16.1
Release:       alt1
Summary:       Contracts for Ruby
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/egonSchiele/contracts.ruby
Vcs:           https://github.com/egonschiele/contracts.ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(contracts) = 0.16.1


%description
This library provides contracts for Ruby. Contracts let you clearly express how
your code behaves, and free you from writing tons of boilerplate, defensive
code.


%package       -n gem-contracts-doc
Version:       0.16.1
Release:       alt1
Summary:       Contracts for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета contracts
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(contracts) = 0.16.1

%description   -n gem-contracts-doc
Contracts for Ruby documentation files.

This library provides contracts for Ruby. Contracts let you clearly express how
your code behaves, and free you from writing tons of boilerplate, defensive
code.

%description   -n gem-contracts-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета contracts.


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

%files         -n gem-contracts-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.16.1-alt1
- + packaged gem with Ruby Policy 2.0
