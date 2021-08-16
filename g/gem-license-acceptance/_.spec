%define        gemname license-acceptance

Name:          gem-license-acceptance
Version:       2.1.20
Release:       alt1
Summary:       Chef Software libraries for accepting usage license
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/license-acceptance/
Vcs:           https://github.com/chef/license-acceptance.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(pastel) >= 0.7 gem(pastel) < 1
BuildRequires: gem(tomlrb) >= 1.2 gem(tomlrb) < 3.0
BuildRequires: gem(tty-box) >= 0.6 gem(tty-box) < 1
BuildRequires: gem(tty-prompt) >= 0.20 gem(tty-prompt) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(pastel) >= 0.7 gem(pastel) < 1
Requires:      gem(tomlrb) >= 1.2 gem(tomlrb) < 3.0
Requires:      gem(tty-box) >= 0.6 gem(tty-box) < 1
Requires:      gem(tty-prompt) >= 0.20 gem(tty-prompt) < 1
Provides:      gem(license-acceptance) = 2.1.20


%description
Chef Software libraries for accepting usage license.

This repo consists of a few parts:

* A specification for the acceptance of the new Chef EULA - The Trademark page
contains useful information, especially for users who have questions about
building an open source fork of Chef Software products.
* A Ruby library used for accepting the license
* A Golang library intended to be used by a Habitat package for accepting the
license


%package       -n gem-license-acceptance-doc
Version:       2.1.20
Release:       alt1
Summary:       Chef Software libraries for accepting usage license documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета license-acceptance
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(license-acceptance) = 2.1.20

%description   -n gem-license-acceptance-doc
Chef Software libraries for accepting usage license documentation
files.

This repo consists of a few parts:

* A specification for the acceptance of the new Chef EULA - The Trademark page
contains useful information, especially for users who have questions about
building an open source fork of Chef Software products.
* A Ruby library used for accepting the license
* A Golang library intended to be used by a Habitat package for accepting the
license

%description   -n gem-license-acceptance-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета license-acceptance.


%package       -n gem-license-acceptance-devel
Version:       2.1.20
Release:       alt1
Summary:       Chef Software libraries for accepting usage license development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета license-acceptance
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(license-acceptance) = 2.1.20

%description   -n gem-license-acceptance-devel
Chef Software libraries for accepting usage license development
package.

This repo consists of a few parts:

* A specification for the acceptance of the new Chef EULA - The Trademark page
contains useful information, especially for users who have questions about
building an open source fork of Chef Software products.
* A Ruby library used for accepting the license
* A Golang library intended to be used by a Habitat package for accepting the
license

%description   -n gem-license-acceptance-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета license-acceptance.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-license-acceptance-doc
%ruby_gemdocdir

%files         -n gem-license-acceptance-devel


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.20-alt1
- ^ 1.0.13 -> 2.1.20

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.13-alt1.1
- ! spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.13-alt1
- + packaged gem with usage Ruby Policy 2.0
