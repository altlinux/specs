%define        gemname yard-doctest

Name:          gem-yard-doctest
Version:       0.1.17
Release:       alt1
Summary:       Doctests from YARD examples
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/p0deje/yard-doctest
Vcs:           https://github.com/p0deje/yard-doctest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(aruba) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(relish) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(minitest) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(yard) >= 0
Requires:      gem(minitest) >= 0
Provides:      gem(yard-doctest) = 0.1.17


%description
Execute YARD examples as tests


%package       -n gem-yard-doctest-doc
Version:       0.1.17
Release:       alt1
Summary:       Doctests from YARD examples documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yard-doctest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yard-doctest) = 0.1.17

%description   -n gem-yard-doctest-doc
Doctests from YARD examples documentation files.

Execute YARD examples as tests

%description   -n gem-yard-doctest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yard-doctest.


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

%files         -n gem-yard-doctest-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.17-alt1
- + packaged gem with Ruby Policy 2.0
