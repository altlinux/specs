%define        gemname fog-radosgw

Name:          gem-fog-radosgw
Version:       0.0.5
Release:       alt1.1
Summary:       Fog backend for provisioning Ceph Radosgw - the Swift and S3 compatible REST API for Ceph
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-radosgw
Vcs:           https://github.com/fog/fog-radosgw.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(fog-xml) >= 0.0.1
BuildRequires: gem(fog-core) >= 1.21.0 gem(fog-core) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(shindo) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency fog-core >= 2.2.4,fog-core < 3
Requires:      gem(fog-json) >= 0
Requires:      gem(fog-xml) >= 0.0.1
Requires:      gem(fog-core) >= 1.21.0 gem(fog-core) < 3
Obsoletes:     ruby-fog-radosgw < %EVR
Provides:      ruby-fog-radosgw = %EVR
Provides:      gem(fog-radosgw) = 0.0.5


%description
Fog backend for provisioning Ceph Radosgw - the Swift and S3 compatible REST API
for Ceph. Currently, the gem only supports the S3 API, not Swift. Based on the
Riak CS backend.


%package       -n gem-fog-radosgw-doc
Version:       0.0.5
Release:       alt1.1
Summary:       Fog backend for provisioning Ceph Radosgw - the Swift and S3 compatible REST API for Ceph documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-radosgw
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-radosgw) = 0.0.5

%description   -n gem-fog-radosgw-doc
Fog backend for provisioning Ceph Radosgw - the Swift and S3 compatible REST API
for Ceph documentation files.

Fog backend for provisioning Ceph Radosgw - the Swift and S3 compatible REST API
for Ceph. Currently, the gem only supports the S3 API, not Swift. Based on the
Riak CS backend.

%description   -n gem-fog-radosgw-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-radosgw.


%package       -n gem-fog-radosgw-devel
Version:       0.0.5
Release:       alt1.1
Summary:       Fog backend for provisioning Ceph Radosgw - the Swift and S3 compatible REST API for Ceph development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-radosgw
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-radosgw) = 0.0.5
Requires:      gem(rake) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(shindo) >= 0

%description   -n gem-fog-radosgw-devel
Fog backend for provisioning Ceph Radosgw - the Swift and S3 compatible REST API
for Ceph development package.

Fog backend for provisioning Ceph Radosgw - the Swift and S3 compatible REST API
for Ceph. Currently, the gem only supports the S3 API, not Swift. Based on the
Riak CS backend.

%description   -n gem-fog-radosgw-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-radosgw.


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

%files         -n gem-fog-radosgw-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-radosgw-devel
%doc README.md


%changelog
* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.5-alt1.1
- ! spec

* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus
