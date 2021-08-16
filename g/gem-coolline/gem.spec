%define        gemname coolline

Name:          gem-coolline
Version:       0.5.0
Release:       alt1
Summary:       Sounds like readline, smells like readline, but isn't readline
License:       Zlib
Group:         Development/Ruby
Url:           http://github.com/Mon-Ouie/coolline
Vcs:           https://github.com/mon-ouie/coolline.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(unicode_utils) >= 1.4 gem(unicode_utils) < 2
BuildRequires: gem(riot) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(unicode_utils) >= 1.4 gem(unicode_utils) < 2
Provides:      gem(coolline) = 0.5.0


%description
A readline-like library that allows to change how the input is displayed.


%package       -n gem-coolline-doc
Version:       0.5.0
Release:       alt1
Summary:       Sounds like readline, smells like readline, but isn't readline documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета coolline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(coolline) = 0.5.0

%description   -n gem-coolline-doc
Sounds like readline, smells like readline, but isn't readline documentation
files.

A readline-like library that allows to change how the input is displayed.

%description   -n gem-coolline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета coolline.


%package       -n gem-coolline-devel
Version:       0.5.0
Release:       alt1
Summary:       Sounds like readline, smells like readline, but isn't readline development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета coolline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(coolline) = 0.5.0
Requires:      gem(riot) >= 0

%description   -n gem-coolline-devel
Sounds like readline, smells like readline, but isn't readline development
package.

A readline-like library that allows to change how the input is displayed.

%description   -n gem-coolline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета coolline.


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

%files         -n gem-coolline-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-coolline-devel
%doc README.md


%changelog
* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0
