%define        gemname rr

Name:          gem-rr
Version:       3.0.4
Release:       alt1
Summary:       test double framework that features a rich selection of double techniques and a terse syntax
License:       MIT
Group:         Development/Ruby
Url:           https://rr.github.io/rr
Vcs:           https://github.com/rr/rr.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
# BuildRequires: gem(test-unit-rr) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rr) = 3.0.4


%description
RR is a test double framework that features a rich selection of double
techniques and a terse syntax.


%package       -n gem-rr-doc
Version:       3.0.4
Release:       alt1
Summary:       test double framework that features a rich selection of double techniques and a terse syntax documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rr
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rr) = 3.0.4

%description   -n gem-rr-doc
test double framework that features a rich selection of double
techniques and a terse syntax documentation files.

RR is a test double framework that features a rich selection of double
techniques and a terse syntax.

%description   -n gem-rr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rr.


%package       -n gem-rr-devel
Version:       3.0.4
Release:       alt1
Summary:       test double framework that features a rich selection of double techniques and a terse syntax development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rr
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rr) = 3.0.4
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
# Requires:      gem(test-unit-rr) >= 0

%description   -n gem-rr-devel
test double framework that features a rich selection of double
techniques and a terse syntax development package.

RR is a test double framework that features a rich selection of double
techniques and a terse syntax.

%description   -n gem-rr-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rr.


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

%files         -n gem-rr-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rr-devel
%doc README.md


%changelog
* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.4-alt1
- + packaged gem with Ruby Policy 2.0
