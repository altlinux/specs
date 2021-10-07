%define        gemname ae

Name:          gem-ae
Version:       1.8.2
Release:       alt1
Summary:       Assertive Expressive
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/rubyworks/ae
Vcs:           https://github.com/rubyworks/ae.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ansi) >= 0
# BuildRequires: gem(detroit) >= 0
# BuildRequires: gem(qed) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ansi) >= 0
Provides:      gem(ae) = 1.8.2


%description
Assertive Expressive is an assertions library specifically designed for reuse by
other test frameworks.


%package       -n gem-ae-doc
Version:       1.8.2
Release:       alt1
Summary:       Assertive Expressive documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ae
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ae) = 1.8.2

%description   -n gem-ae-doc
Assertive Expressive documentation files.

Assertive Expressive is an assertions library specifically designed for reuse by
other test frameworks.

%description   -n gem-ae-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ae.


%package       -n gem-ae-devel
Version:       1.8.2
Release:       alt1
Summary:       Assertive Expressive development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ae
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ae) = 1.8.2
# Requires:      gem(detroit) >= 0
# Requires:      gem(qed) >= 0

%description   -n gem-ae-devel
Assertive Expressive development package.

Assertive Expressive is an assertions library specifically designed for reuse by
other test frameworks.

%description   -n gem-ae-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ae.


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

%files         -n gem-ae-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ae-devel
%doc README.md


%changelog
* Sat Sep 11 2021 Pavel Skrylev <majioa@altlinux.org> 1.8.2-alt1
- + packaged gem with Ruby Policy 2.0
