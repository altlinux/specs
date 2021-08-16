%define        gemname fog-google

Name:          gem-fog-google
Epoch:         1
Version:       1.13.0
Release:       alt1
Summary:       Fog for Google Cloud Platform
Summary(ru_RU.UTF-8): Туман для Гугловой облачной платформы
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-google
Vcs:           https://github.com/fog/fog-google.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-core) >= 2.0 gem(fog-core) <= 3
BuildRequires: gem(fog-json) >= 1.2 gem(fog-json) < 2
BuildRequires: gem(fog-xml) >= 0.1.0 gem(fog-xml) < 0.2
BuildRequires: gem(google-api-client) >= 0.53 gem(google-api-client) <= 1
BuildRequires: gem(google-cloud-env) >= 1.2 gem(google-cloud-env) < 2
BuildRequires: gem(pry) >= 0
BuildRequires: gem(retriable) >= 0
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(shindo) >= 0
BuildRequires: gem(vcr) >= 0
BuildRequires: gem(webmock) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency fog-core ~> 2.0
%ruby_use_gem_dependency google-api-client ~> 0.53
Requires:      gem(fog-core) >= 2.0 gem(fog-core) <= 3
Requires:      gem(fog-json) >= 1.2 gem(fog-json) < 2
Requires:      gem(fog-xml) >= 0.1.0 gem(fog-xml) < 0.2
Requires:      gem(google-api-client) >= 0.53 gem(google-api-client) <= 1
Requires:      gem(google-cloud-env) >= 1.2 gem(google-cloud-env) < 2
Obsoletes:     ruby-fog-google < %EVR
Provides:      ruby-fog-google = %EVR
Provides:      gem(fog-google) = 1.13.0


%description
There are two ways to access Google Cloud Storage. The old S3 API and the new
JSON API. Fog::Storage::Google will automatically direct you to the appropriate
API based on the credentials you provide it.

* The XML API is almost identical to S3. Use Google's interoperability keys to
access it.
* The new JSON API is faster and uses auth similarly to the rest of the Google
Cloud APIs using a service account private key.


%package       -n gem-fog-google-doc
Version:       1.13.0
Release:       alt1
Summary:       Fog for Google Cloud Platform documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-google
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-google) = 1.13.0

%description   -n gem-fog-google-doc
Fog for Google Cloud Platform documentation files.

There are two ways to access Google Cloud Storage. The old S3 API and the new
JSON API. Fog::Storage::Google will automatically direct you to the appropriate
API based on the credentials you provide it.

* The XML API is almost identical to S3. Use Google's interoperability keys to
access it.
* The new JSON API is faster and uses auth similarly to the rest of the Google
Cloud APIs using a service account private key.

%description   -n gem-fog-google-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-google.


%package       -n gem-fog-google-devel
Version:       1.13.0
Release:       alt1
Summary:       Fog for Google Cloud Platform development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-google
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-google) = 1.13.0
Requires:      gem(pry) >= 0
Requires:      gem(retriable) >= 0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-reporters) >= 0
Requires:      gem(shindo) >= 0
Requires:      gem(vcr) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(fog-core) >= 2.0 gem(fog-core) < 3
Requires:      gem(google-api-client) >= 0.24 gem(google-api-client) < 1

%description   -n gem-fog-google-devel
Fog for Google Cloud Platform development package.

There are two ways to access Google Cloud Storage. The old S3 API and the new
JSON API. Fog::Storage::Google will automatically direct you to the appropriate
API based on the credentials you provide it.

* The XML API is almost identical to S3. Use Google's interoperability keys to
access it.
* The new JSON API is faster and uses auth similarly to the rest of the Google
Cloud APIs using a service account private key.

%description   -n gem-fog-google-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-google.


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

%files         -n gem-fog-google-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-google-devel
%doc README.md


%changelog
* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 1:1.13.0-alt1
- ^ 1.9.1 -> 1.13.0

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.9.1-alt1
- Bump to 1.9.1

* Fri Mar 08 2019 Pavel Skrylev <majioa@altlinux.org> 1:1.8.2-alt1
- Bump to 1.8.2;
- Use Ruby Policy 2.0.

* Tue Nov 13 2018 Pavel Skrylev <majioa@altlinux.org> 1:1.8.1-alt1
- Bump to 1.8.1.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.0.9-alt1
- Use old version for fog.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.
- Package as gem.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt1
- Initial build for Sisyphus
