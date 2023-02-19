Name:          gapic-generator-ruby
Version:       20230125
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions
License:       Apache-2.0
Group:         Other
Url:           https://github.com/googleapis/gapic-generator-ruby
Vcs:           https://github.com/googleapis/gapic-generator-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(minitest) >= 5.16
BuildRequires: gem(minitest-autotest) >= 1.0
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(minitest-rg) >= 5.2
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(redcarpet) >= 3.0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(google-cloud-core) >= 1.5
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(faraday) >= 1.9
BuildRequires: gem(faraday-retry) >= 1.0
BuildRequires: gem(googleapis-common-protos) >= 1.3.12
BuildRequires: gem(googleapis-common-protos-types) >= 1.3.1
BuildRequires: gem(googleauth) >= 1.0
BuildRequires: gem(google-protobuf) >= 3.14
BuildRequires: gem(grpc) >= 1.36
BuildRequires: gem(google-style) >= 1.26.1
BuildRequires: gem(minitest-focus) >= 1.0
BuildRequires: gem(actionpack) >= 5.2
BuildRequires: gem(protobuf) >= 3.8
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-autotest) >= 2
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(minitest-rg) >= 6
BuildConflicts: gem(redcarpet) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(google-cloud-core) >= 2
BuildConflicts: gem(google-style) >= 2
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(faraday-retry) >= 3
BuildConflicts: gem(googleapis-common-protos) >= 2
BuildConflicts: gem(googleapis-common-protos-types) >= 2
BuildConflicts: gem(googleauth) >= 2
BuildConflicts: gem(google-protobuf) >= 4
BuildConflicts: gem(grpc) >= 2
BuildConflicts: gem(actionpack) >= 7
BuildConflicts: gem(protobuf) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_use_gem_dependency actionpack >= 6.1.1,actionpack < 7
%ruby_use_gem_dependency google-style >= 1.26.1,google-style < 2
%ruby_ignore_names snippets,(?-mix:google),(?-mix:grafeas),gapic-generator-my_plugin
Requires:      gem(gapic-common) >= 0
Requires:      gem(gapic-generator) >= 0
Requires:      gem(gapic-generator-ads) >= 0
Requires:      gem(gapic-generator-cloud) >= 0
Requires:      gem(rake) >= 13.0
Provides:      ruby-gapic-generator-ruby


%description
Create Ruby clients from a protocol buffer description of an API.

Note This project is a preview. Please try it out and let us know what you
think, but there are currently no guarantees of stability or support.

Note This project is a preview. Please try it out and let us know what you
think, but there are currently no guarantees of stability or support.


%package       -n gem-gapic
Version:       0.1.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(gapic) = 0.1.0

%description   -n gem-gapic
Core namespace for Google generated API client tools


%package       -n gem-gapic-doc
Version:       0.1.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gapic
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gapic) = 0.1.0

%description   -n gem-gapic-doc
Generate Ruby gRPC client libraries from Protocol Buffer definitions
documentation files.

Core namespace for Google generated API client tools

%description   -n gem-gapic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gapic.


%package       -n gem-gapic-devel
Version:       0.1.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gapic
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic) = 0.1.0
Requires:      gem(google-style) >= 1.25.1
Requires:      gem(minitest) >= 5.16
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(minitest-rg) >= 5.2
Requires:      gem(rake) >= 12.0
Requires:      gem(redcarpet) >= 3.0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(google-style) >= 2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(minitest-rg) >= 6
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-gapic-devel
Generate Ruby gRPC client libraries from Protocol Buffer definitions development
package.

Core namespace for Google generated API client tools

%description   -n gem-gapic-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gapic.


%package       -n gem-gapic-common
Version:       0.16.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday) >= 1.9
Requires:      gem(faraday-retry) >= 1.0
Requires:      gem(googleapis-common-protos) >= 1.3.12
Requires:      gem(googleapis-common-protos-types) >= 1.3.1
Requires:      gem(googleauth) >= 1.0
Requires:      gem(google-protobuf) >= 3.14
Requires:      gem(grpc) >= 1.36
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(faraday-retry) >= 3
Conflicts:     gem(googleapis-common-protos) >= 2
Conflicts:     gem(googleapis-common-protos-types) >= 2
Conflicts:     gem(googleauth) >= 2
Conflicts:     gem(google-protobuf) >= 4
Conflicts:     gem(grpc) >= 2
Provides:      gem(gapic-common) = 0.16.0

%description   -n gem-gapic-common
Common code for GAPIC-generated API clients.


%package       -n gem-gapic-common-doc
Version:       0.16.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gapic-common
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gapic-common) = 0.16.0

%description   -n gem-gapic-common-doc
Generate Ruby gRPC client libraries from Protocol Buffer definitions
documentation files.

Common code for GAPIC-generated API clients.

%description   -n gem-gapic-common-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gapic-common.


%package       -n gem-gapic-common-devel
Version:       0.16.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gapic-common
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) = 0.16.0
Requires:      gem(google-cloud-core) >= 1.5
Requires:      gem(google-style) >= 1.26.0
Requires:      gem(minitest) >= 5.16
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(minitest-rg) >= 5.2
Requires:      gem(pry) >= 0.13.1
Requires:      gem(rake) >= 12.0
Requires:      gem(redcarpet) >= 3.0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(google-cloud-core) >= 2
Conflicts:     gem(google-style) >= 2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(minitest-rg) >= 6
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-gapic-common-devel
Generate Ruby gRPC client libraries from Protocol Buffer definitions development
package.

Common code for GAPIC-generated API clients.

%description   -n gem-gapic-common-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gapic-common.


%package       -n gem-gapic-generator
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionpack) >= 5.2
Requires:      gem(protobuf) >= 3.8
Conflicts:     gem(actionpack) >= 7
Conflicts:     gem(protobuf) >= 4
Provides:      gem(gapic-generator) = 0.20.0

%description   -n gem-gapic-generator
An API Client Generator for Ruby in Ruby!


%package       -n gapic-generator
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gapic-generator
Group:         Other
BuildArch:     noarch

Requires:      gem(gapic-generator) = 0.20.0

%description   -n gapic-generator
Generate Ruby gRPC client libraries from Protocol Buffer definitions
executable(s).

An API Client Generator for Ruby in Ruby!

%description   -n gapic-generator -l ru_RU.UTF-8
Исполнямка для самоцвета gapic-generator.


%package       -n gem-gapic-generator-doc
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gapic-generator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gapic-generator) = 0.20.0

%description   -n gem-gapic-generator-doc
Generate Ruby gRPC client libraries from Protocol Buffer definitions
documentation files.

An API Client Generator for Ruby in Ruby!

%description   -n gem-gapic-generator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gapic-generator.


%package       -n gem-gapic-generator-devel
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gapic-generator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-generator) = 0.20.0
Requires:      gem(google-style) >= 1.26.1
Requires:      gem(minitest) >= 5.16
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-focus) >= 1.0
Requires:      gem(pry) >= 0.13.1
Requires:      gem(rake) >= 13.0
Requires:      gem(redcarpet) >= 3.0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(google-style) >= 2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-gapic-generator-devel
Generate Ruby gRPC client libraries from Protocol Buffer definitions development
package.

An API Client Generator for Ruby in Ruby!

%description   -n gem-gapic-generator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gapic-generator.


%package       -n gem-gapic-generator-ads
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionpack) >= 5.2
Requires:      gem(gapic-generator) = 0.20.0
Requires:      gem(protobuf) >= 3.8
Conflicts:     gem(actionpack) >= 7
Conflicts:     gem(protobuf) >= 4
Provides:      gem(gapic-generator-ads) = 0.20.0

%description   -n gem-gapic-generator-ads
An API Client Generator for Ruby in Ruby!


%package       -n protoc-gen-ruby-ads
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gapic-generator-ads
Group:         Other
BuildArch:     noarch

Requires:      gem(gapic-generator-ads) = 0.20.0

%description   -n protoc-gen-ruby-ads
Generate Ruby gRPC client libraries from Protocol Buffer definitions
executable(s).

An API Client Generator for Ruby in Ruby!

%description   -n protoc-gen-ruby-ads -l ru_RU.UTF-8
Исполнямка для самоцвета gapic-generator-ads.


%package       -n gem-gapic-generator-ads-doc
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gapic-generator-ads
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gapic-generator-ads) = 0.20.0

%description   -n gem-gapic-generator-ads-doc
Generate Ruby gRPC client libraries from Protocol Buffer definitions
documentation files.

An API Client Generator for Ruby in Ruby!

%description   -n gem-gapic-generator-ads-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gapic-generator-ads.


%package       -n gem-gapic-generator-ads-devel
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gapic-generator-ads
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-generator-ads) = 0.20.0
Requires:      gem(google-style) >= 1.26.1
Requires:      gem(minitest) >= 5.16
Requires:      gem(minitest-focus) >= 1.0
Requires:      gem(rake) >= 13.0
Conflicts:     gem(google-style) >= 2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-focus) >= 2

%description   -n gem-gapic-generator-ads-devel
Generate Ruby gRPC client libraries from Protocol Buffer definitions development
package.

An API Client Generator for Ruby in Ruby!

%description   -n gem-gapic-generator-ads-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gapic-generator-ads.


%package       -n gem-gapic-generator-cloud
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionpack) >= 5.2
Requires:      gem(gapic-generator) = 0.20.0
Requires:      gem(google-style) >= 1.26.1
Requires:      gem(protobuf) >= 3.8
Conflicts:     gem(actionpack) >= 7
Conflicts:     gem(google-style) >= 2
Conflicts:     gem(protobuf) >= 4
Provides:      gem(gapic-generator-cloud) = 0.20.0

%description   -n gem-gapic-generator-cloud
An API Client Generator for Ruby in Ruby!


%package       -n gapic-generator-cloud
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gapic-generator-cloud
Group:         Other
BuildArch:     noarch

Requires:      gem(gapic-generator-cloud) = 0.20.0

%description   -n gapic-generator-cloud
Generate Ruby gRPC client libraries from Protocol Buffer definitions
executable(s).

An API Client Generator for Ruby in Ruby!

%description   -n gapic-generator-cloud -l ru_RU.UTF-8
Исполнямка для самоцвета gapic-generator-cloud.


%package       -n gem-gapic-generator-cloud-doc
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gapic-generator-cloud
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gapic-generator-cloud) = 0.20.0

%description   -n gem-gapic-generator-cloud-doc
Generate Ruby gRPC client libraries from Protocol Buffer definitions
documentation files.

An API Client Generator for Ruby in Ruby!

%description   -n gem-gapic-generator-cloud-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gapic-generator-cloud.


%package       -n gem-gapic-generator-cloud-devel
Version:       0.20.0
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gapic-generator-cloud
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-generator-cloud) = 0.20.0
Requires:      gem(minitest) >= 5.16
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-focus) >= 1.0
Requires:      gem(pry) >= 0.13.1
Requires:      gem(rake) >= 13.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2

%description   -n gem-gapic-generator-cloud-devel
Generate Ruby gRPC client libraries from Protocol Buffer definitions development
package.

An API Client Generator for Ruby in Ruby!

%description   -n gem-gapic-generator-cloud-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gapic-generator-cloud.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files         -n gem-gapic
%doc README.md
%ruby_gemspecdir/gapic-0.1.0.gemspec
%ruby_gemslibdir/gapic-0.1.0

%files         -n gem-gapic-doc
%doc README.md
%ruby_gemsdocdir/gapic-0.1.0

%files         -n gem-gapic-devel
%doc README.md

%files         -n gem-gapic-common
%doc README.md
%ruby_gemspecdir/gapic-common-0.16.0.gemspec
%ruby_gemslibdir/gapic-common-0.16.0

%files         -n gem-gapic-common-doc
%doc README.md
%ruby_gemsdocdir/gapic-common-0.16.0

%files         -n gem-gapic-common-devel
%doc README.md

%files         -n gem-gapic-generator
%doc README.md
%ruby_gemspecdir/gapic-generator-0.20.0.gemspec
%ruby_gemslibdir/gapic-generator-0.20.0

%files         -n gapic-generator
%doc README.md
%_bindir/gapic-generator
%_bindir/protoc-gen-ruby_gapic

%files         -n gem-gapic-generator-doc
%doc README.md
%ruby_gemsdocdir/gapic-generator-0.20.0

%files         -n gem-gapic-generator-devel
%doc README.md

%files         -n gem-gapic-generator-ads
%doc README.md
%ruby_gemspecdir/gapic-generator-ads-0.20.0.gemspec
%ruby_gemslibdir/gapic-generator-ads-0.20.0

%files         -n protoc-gen-ruby-ads
%doc README.md
%_bindir/protoc-gen-ruby_ads

%files         -n gem-gapic-generator-ads-doc
%doc README.md
%ruby_gemsdocdir/gapic-generator-ads-0.20.0

%files         -n gem-gapic-generator-ads-devel
%doc README.md

%files         -n gem-gapic-generator-cloud
%doc README.md
%ruby_gemspecdir/gapic-generator-cloud-0.20.0.gemspec
%ruby_gemslibdir/gapic-generator-cloud-0.20.0

%files         -n gapic-generator-cloud
%doc README.md
%_bindir/protoc-gen-ruby_cloud
%_bindir/ruby-cloud-docker-entrypoint

%files         -n gem-gapic-generator-cloud-doc
%doc README.md
%ruby_gemsdocdir/gapic-generator-cloud-0.20.0

%files         -n gem-gapic-generator-cloud-devel
%doc README.md


%changelog
* Wed Jan 25 2023 Pavel Skrylev <majioa@altlinux.org> 20230125-alt1
- ^ 20210605 -> 20230125

* Wed Oct 19 2022 Pavel Skrylev <majioa@altlinux.org> 20210605-alt1.1
- !build deps to novel gems

* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 20210605-alt1
- + packaged gem with Ruby Policy 2.0
