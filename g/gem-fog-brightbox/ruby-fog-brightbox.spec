%define        gemname fog-brightbox

Name:          gem-fog-brightbox
Version:       1.4.1
Release:       alt1
Summary:       Brightbox Cloud support for the fog gem
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-brightbox
Vcs:           https://github.com/fog/fog-brightbox.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 1.45 gem(fog-core) < 3.0
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(dry-inflector) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(shindo) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(yard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fog-core) >= 1.45 gem(fog-core) < 3.0
Requires:      gem(fog-json) >= 0
Requires:      gem(dry-inflector) >= 0
Obsoletes:     ruby-fog-brightbox < %EVR
Provides:      ruby-fog-brightbox = %EVR
Provides:      gem(fog-brightbox) = 1.4.1

%description
Brightbox Cloud module for fog (The Ruby cloud services library). This gem is a
module for the fog gem that allows you to manage resources in the Brightbox
Cloud. It is included by the main fog metagem but can used as an independent
library in other applications.

This includes support for the following services:
* Compute
 * Images
 * Load Balancers
 * SQL Cloud instances

Currently all services are grouped within compute but will be moved to their
own sections when standardisation of fog progresses.


%package       -n gem-fog-brightbox-doc
Version:       1.4.1
Release:       alt1
Summary:       Brightbox Cloud support for the fog gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-brightbox
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-brightbox) = 1.4.1

%description   -n gem-fog-brightbox-doc
Brightbox Cloud support for the fog gem documentation files.

Brightbox Cloud module for fog (The Ruby cloud services library). This gem is a
module for the fog gem that allows you to manage resources in the Brightbox
Cloud. It is included by the main fog metagem but can used as an independent
library in other applications.

This includes support for the following services:
* Compute
 * Images
 * Load Balancers
 * SQL Cloud instances

Currently all services are grouped within compute but will be moved to their
own sections when standardisation of fog progresses.

%description   -n gem-fog-brightbox-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-brightbox.


%package       -n gem-fog-brightbox-devel
Version:       1.4.1
Release:       alt1
Summary:       Brightbox Cloud support for the fog gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-brightbox
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-brightbox) = 1.4.1
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(shindo) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(yard) >= 0

%description   -n gem-fog-brightbox-devel
Brightbox Cloud support for the fog gem development package.

Brightbox Cloud module for fog (The Ruby cloud services library). This gem is a
module for the fog gem that allows you to manage resources in the Brightbox
Cloud. It is included by the main fog metagem but can used as an independent
library in other applications.

This includes support for the following services:
* Compute
 * Images
 * Load Balancers
 * SQL Cloud instances

Currently all services are grouped within compute but will be moved to their
own sections when standardisation of fog progresses.

%description   -n gem-fog-brightbox-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-brightbox.


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

%files         -n gem-fog-brightbox-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-brightbox-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- ^ 1.0.0 -> 1.4.1

* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Use Ruby Policy 2.0
- Bump to 1.0.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
