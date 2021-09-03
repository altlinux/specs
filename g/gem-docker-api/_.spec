%define        gemname docker-api

Name:          gem-docker-api
Version:       2.2.0
Release:       alt1
Summary:       A lightweight Ruby client for the Docker Remote API
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/swipely/docker-api
Vcs:           https://github.com/swipely/docker-api.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(excon) >= 0.47.0
BuildRequires: gem(multi_json) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rspec-its) >= 0
BuildRequires: gem(cane) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(single_cov) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(parallel) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(excon) >= 0.47.0
Requires:      gem(multi_json) >= 0
Provides:      gem(docker-api) = 2.2.0


%description
This gem provides an object-oriented interface to the Docker Engine API. Every
method listed there is implemented. At the time of this writing, docker-api is
meant to interface with Docker version 1.4.*

If you're interested in using Docker to package your apps, we recommend the
dockly gem. Dockly provides a simple DSL for describing Docker containers that
install as Debian packages and are controlled by upstart scripts.


%package       -n gem-docker-api-doc
Version:       2.2.0
Release:       alt1
Summary:       A lightweight Ruby client for the Docker Remote API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета docker-api
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(docker-api) = 2.2.0

%description   -n gem-docker-api-doc
A lightweight Ruby client for the Docker Remote API documentation
files.

This gem provides an object-oriented interface to the Docker Engine API. Every
method listed there is implemented. At the time of this writing, docker-api is
meant to interface with Docker version 1.4.*

If you're interested in using Docker to package your apps, we recommend the
dockly gem. Dockly provides a simple DSL for describing Docker containers that
install as Debian packages and are controlled by upstart scripts.

%description   -n gem-docker-api-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета docker-api.


%package       -n gem-docker-api-devel
Version:       2.2.0
Release:       alt1
Summary:       A lightweight Ruby client for the Docker Remote API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета docker-api
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(docker-api) = 2.2.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rspec-its) >= 0
Requires:      gem(cane) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(single_cov) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(parallel) >= 0

%description   -n gem-docker-api-devel
A lightweight Ruby client for the Docker Remote API development
package.

This gem provides an object-oriented interface to the Docker Engine API. Every
method listed there is implemented. At the time of this writing, docker-api is
meant to interface with Docker version 1.4.*

If you're interested in using Docker to package your apps, we recommend the
dockly gem. Dockly provides a simple DSL for describing Docker containers that
install as Debian packages and are controlled by upstart scripts.

%description   -n gem-docker-api-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета docker-api.


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

%files         -n gem-docker-api-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-docker-api-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- ^ 1.34.2 -> 2.2.0

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.34.2-alt1.1
- ! spec according to changelog rules

* Sat Aug 10 2019 Pavel Skrylev <majioa@altlinux.org> 1.34.2-alt1
- + packaged gem with usage Ruby Policy 2.0
