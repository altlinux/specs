%define        gemname artifactory

Name:          gem-artifactory
Version:       3.0.15
Release:       alt1
Summary:       A simple, lightweight Ruby client for interacting with the Artifactory API
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/artifactory-client
Vcs:           https://github.com/chef/artifactory-client.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-artifactory-client < %EVR
Provides:      ruby-artifactory-client = %EVR
Provides:      gem(artifactory) = 3.0.15


%description
A Ruby client and interface to the Artifactory API. The majority of API
endpoints are only exposed for Artifactory Pro customers! As such, many of the
resources and actions exposed by this gem also require Artifactory Pro.

The Artifactory gem offers a convienent interface for managing various parts of
the Artifactory API.


%package       -n gem-artifactory-doc
Version:       3.0.15
Release:       alt1
Summary:       A simple, lightweight Ruby client for interacting with the Artifactory API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета artifactory
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(artifactory) = 3.0.15

%description   -n gem-artifactory-doc
A simple, lightweight Ruby client for interacting with the Artifactory API
documentation files.

A Ruby client and interface to the Artifactory API. The majority of API
endpoints are only exposed for Artifactory Pro customers! As such, many of the
resources and actions exposed by this gem also require Artifactory Pro.

The Artifactory gem offers a convienent interface for managing various parts of
the Artifactory API.

%description   -n gem-artifactory-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета artifactory.


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

%files         -n gem-artifactory-doc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.15-alt1
- ^ 3.0.1 -> 3.0.15

* Mon Jun 24 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt2
- Fix spec

* Thu Jun 13 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- Bump to 3.0.1
- Use Ruby Policy 2.0
- Fix lost provides (closes #36888)

* Mon Jan 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.0.0-alt1
- version fixed 3.0.0

* Tue Dec 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.8.6-alt1
- Initial build for Sisyphus
