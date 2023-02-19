# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname packnga

Name:          gem-packnga
Version:       1.0.4.1
Release:       alt0.1
Summary:       A utility library to package i18n-ed library
License:       LGPLv2
Group:         Development/Ruby
Url:           http://ranguba.org/packnga/
Vcs:           https://github.com/ranguba/packnga.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-notify) >= 0
BuildRequires: gem(test-unit-rr) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(RedCloth) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(gettext) >= 3.1.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 0
Requires:      gem(yard) >= 0.9
Requires:      gem(gettext) >= 3.1.3
Provides:      gem(packnga) = 1.0.4.1

%ruby_use_gem_version packnga:1.0.4.1

%description
A utility library to package i18n-ed library.

Packnga is a library to translate to many languages by YARD.


%package       -n gem-packnga-doc
Version:       1.0.4.1
Release:       alt0.1
Summary:       A utility library to package i18n-ed library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета packnga
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(packnga) = 1.0.4.1

%description   -n gem-packnga-doc
A utility library to package i18n-ed library documentation files.

%description   -n gem-packnga-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета packnga.


%package       -n gem-packnga-devel
Version:       1.0.4.1
Release:       alt0.1
Summary:       A utility library to package i18n-ed library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета packnga
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(packnga) = 1.0.4.1
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-notify) >= 0
Requires:      gem(test-unit-rr) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(RedCloth) >= 0

%description   -n gem-packnga-devel
A utility library to package i18n-ed library development package.

%description   -n gem-packnga-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета packnga.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.textile
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-packnga-doc
%doc README.textile
%ruby_gemdocdir

%files         -n gem-packnga-devel
%doc README.textile


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.4.1-alt0.1
- ^ 1.0.4 -> 1.0.4[1]

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt1
- + packaged gem with usage Ruby Policy 2.0
