%define        gemname mize

Name:          gem-mize
Version:       0.4.0
Release:       alt1
Summary:       Library that provides memoziation for methods and functions
License:       MIT
Group:         Development/Ruby
Url:           http://flori.github.com/mize
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(gem_hadar) >= 1.10.0 gem(gem_hadar) < 2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(protocol) >= 2.0 gem(protocol) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency gem_hadar >= 1.11.0,gem_hadar < 2
Requires:      gem(protocol) >= 2.0 gem(protocol) < 3
Provides:      gem(mize) = 0.4.0


%description
Library that provides memoziation for methods and functions for Ruby.


%package       -n gem-mize-doc
Version:       0.4.0
Release:       alt1
Summary:       Library that provides memoziation for methods and functions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mize
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mize) = 0.4.0

%description   -n gem-mize-doc
Library that provides memoziation for methods and functions documentation
files.

Library that provides memoziation for methods and functions for Ruby.

%description   -n gem-mize-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mize.


%package       -n gem-mize-devel
Version:       0.4.0
Release:       alt1
Summary:       Library that provides memoziation for methods and functions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mize
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mize) = 0.4.0
Requires:      gem(gem_hadar) >= 1.10.0 gem(gem_hadar) < 2
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(yard) >= 0

%description   -n gem-mize-devel
Library that provides memoziation for methods and functions development
package.

Library that provides memoziation for methods and functions for Ruby.

%description   -n gem-mize-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mize.


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

%files         -n gem-mize-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mize-devel
%doc README.md


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with Ruby Policy 2.0
