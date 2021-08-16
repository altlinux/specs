Name:          gapic-generator-ruby
Version:       20210605
Release:       alt1
Summary:       Generate Ruby gRPC client libraries from Protocol Buffer definitions
License:       Apache-2.0 or MIT
Group:         Other
Url:           https://github.com/googleapis/gapic-generator-ruby
Vcs:           https://github.com/googleapis/gapic-generator-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(faraday) >= 1.3 gem(faraday) < 2
BuildRequires: gem(googleapis-common-protos) >= 1.3.11 gem(googleapis-common-protos) < 2.0
BuildRequires: gem(googleapis-common-protos-types) >= 1.0.6 gem(googleapis-common-protos-types) < 2.0
BuildRequires: gem(googleauth) >= 0.16.2 gem(googleauth) < 2.0
BuildRequires: gem(google-protobuf) >= 3.14 gem(google-protobuf) < 4
BuildRequires: gem(grpc) >= 1.36 gem(grpc) < 2
BuildRequires: gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
BuildRequires: gem(google-style) >= 1.25.1 gem(google-style) < 1.26
BuildRequires: gem(minitest) >= 5.14 gem(minitest) < 6
BuildRequires: gem(minitest-autotest) >= 1.0 gem(minitest-autotest) < 2
BuildRequires: gem(minitest-focus) >= 1.1 gem(minitest-focus) < 2
BuildRequires: gem(minitest-rg) >= 5.2 gem(minitest-rg) < 6
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14
BuildRequires: gem(redcarpet) >= 3.0 gem(redcarpet) < 4
BuildRequires: gem(yard) >= 0.9 gem(yard) < 1
BuildRequires: gem(actionpack) >= 5.2 gem(actionpack) < 7
BuildRequires: gem(protobuf) >= 3.8 gem(protobuf) < 4
BuildRequires: gem(grpc-tools) >= 1.36.0 gem(grpc-tools) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findreq_skiplist %_libexecdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %_libexecdir/**/*
%ruby_use_gem_dependency grpc-tools >= 1.36.0,grpc-tools < 2
%ruby_use_gem_dependency actionpack >= 5.0,actionpack < 7
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_ignore_names rainbow_bundler_test,syscall_rubocop_bundler_test,shared,snippets,/v1,/google-cloud-,/my_plugin,/showcase,/garbage,/testing
Requires:      gem(gapic-common) >= 0
Requires:      gem(gapic-generator) >= 0
Requires:      gem(gapic-generator-ads) >= 0
Requires:      gem(gapic-generator-cloud) >= 0
Requires:      gem(rake) >= 12.0 gem(rake) < 14


%description
Create Ruby clients from a protocol buffer description of an API.

Note This project is a preview. Please try it out and let us know what you
think, but there are currently no guarantees of stability or support.


%package       -n gem-gapic-common
Version:       0.4.1
Release:       alt1
Summary:       Common code for GAPIC-generated API clients
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday) >= 1.3 gem(faraday) < 2
Requires:      gem(googleapis-common-protos) >= 1.3.11 gem(googleapis-common-protos) < 2.0
Requires:      gem(googleapis-common-protos-types) >= 1.0.6 gem(googleapis-common-protos-types) < 2.0
Requires:      gem(googleauth) >= 0.16.2 gem(googleauth) < 2.0
Requires:      gem(google-protobuf) >= 3.14 gem(google-protobuf) < 4
Requires:      gem(grpc) >= 1.36 gem(grpc) < 2
Provides:      gem(gapic-common) = 0.4.1

%description   -n gem-gapic-common
Common code for GAPIC-generated API clients.


%package       -n gem-gapic-common-doc
Version:       0.4.1
Release:       alt1
Summary:       Common code for GAPIC-generated API clients documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gapic-common
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gapic-common) = 0.4.1

%description   -n gem-gapic-common-doc
Common code for GAPIC-generated API clients documentation files.

%description   -n gem-gapic-common-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gapic-common.


%package       -n gem-gapic-common-devel
Version:       0.4.1
Release:       alt1
Summary:       Common code for GAPIC-generated API clients development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gapic-common
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) = 0.4.1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-style) >= 1.25.1 gem(google-style) < 1.26
Requires:      gem(minitest) >= 5.14 gem(minitest) < 6
Requires:      gem(minitest-autotest) >= 1.0 gem(minitest-autotest) < 2
Requires:      gem(minitest-focus) >= 1.1 gem(minitest-focus) < 2
Requires:      gem(minitest-rg) >= 5.2 gem(minitest-rg) < 6
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(redcarpet) >= 3.0 gem(redcarpet) < 4
Requires:      gem(yard) >= 0.9 gem(yard) < 1

%description   -n gem-gapic-common-devel
Common code for GAPIC-generated API clients development package.

%description   -n gem-gapic-common-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gapic-common.


%package       -n gem-gapic-generator
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionpack) >= 5.2 gem(actionpack) < 7
Requires:      gem(protobuf) >= 3.8 gem(protobuf) < 4
Provides:      gem(gapic-generator) = 0.7.5

%description   -n gem-gapic-generator
An API Client Generator for Ruby in Ruby!


%package       -n gapic-generator
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gapic-generator
Group:         Other
BuildArch:     noarch

Requires:      gem(gapic-generator) = 0.7.5

%description   -n gapic-generator
An API Client Generator for Ruby in Ruby executable(s).

%description   -n gapic-generator -l ru_RU.UTF-8
Исполнямка для самоцвета gapic-generator.


%package       -n gem-gapic-generator-doc
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gapic-generator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gapic-generator) = 0.7.5

%description   -n gem-gapic-generator-doc
An API Client Generator for Ruby in Ruby documentation files.

%description   -n gem-gapic-generator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gapic-generator.


%package       -n gem-gapic-generator-devel
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gapic-generator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-generator) = 0.7.5
Requires:      gem(google-style) >= 1.25.1 gem(google-style) < 1.26
Requires:      gem(grpc-tools) >= 1.36.0 gem(grpc-tools) < 2
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(minitest-autotest) >= 1.0 gem(minitest-autotest) < 2
Requires:      gem(minitest-focus) >= 1.0 gem(minitest-focus) < 2
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(redcarpet) >= 3.0 gem(redcarpet) < 4
Requires:      gem(yard) >= 0.9 gem(yard) < 1

%description   -n gem-gapic-generator-devel
An API Client Generator for Ruby in Ruby development package.

%description   -n gem-gapic-generator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gapic-generator.


%package       -n gem-gapic-generator-ads
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionpack) >= 5.2 gem(actionpack) < 7
Requires:      gem(gapic-generator) = 0.7.5
Requires:      gem(protobuf) >= 3.8 gem(protobuf) < 4
Provides:      gem(gapic-generator-ads) = 0.7.5

%description   -n gem-gapic-generator-ads
An API Client Generator for Ruby in Ruby!


%package       -n protoc-gen-ruby-ads
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gapic-generator-ads
Group:         Other
BuildArch:     noarch

Requires:      gem(gapic-generator-ads) = 0.7.5

%description   -n protoc-gen-ruby-ads
An API Client Generator for Ruby in Ruby executable(s).

%description   -n protoc-gen-ruby-ads -l ru_RU.UTF-8
Исполнямка для самоцвета gapic-generator-ads.


%package       -n gem-gapic-generator-ads-doc
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gapic-generator-ads
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gapic-generator-ads) = 0.7.5

%description   -n gem-gapic-generator-ads-doc
An API Client Generator for Ruby in Ruby documentation files.

%description   -n gem-gapic-generator-ads-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gapic-generator-ads.


%package       -n gem-gapic-generator-ads-devel
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gapic-generator-ads
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-generator-ads) = 0.7.5
Requires:      gem(google-style) >= 1.25.1 gem(google-style) < 1.26
Requires:      gem(grpc-tools) >= 1.36.0 gem(grpc-tools) < 2
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(minitest-focus) >= 1.0 gem(minitest-focus) < 2
Requires:      gem(rake) >= 12.0 gem(rake) < 14

%description   -n gem-gapic-generator-ads-devel
An API Client Generator for Ruby in Ruby development package.

%description   -n gem-gapic-generator-ads-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gapic-generator-ads.


%package       -n gem-gapic
Version:       0.0.1
Release:       alt1
Summary:       Core namespace for Google generated API client tools
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(gapic) = 0.0.1

%description   -n gem-gapic
Core namespace for Google generated API client tools


%package       -n gem-gapic-doc
Version:       0.0.1
Release:       alt1
Summary:       Core namespace for Google generated API client tools documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gapic
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gapic) = 0.0.1

%description   -n gem-gapic-doc
Core namespace for Google generated API client tools documentation files.

%description   -n gem-gapic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gapic.


%package       -n gem-gapic-devel
Version:       0.0.1
Release:       alt1
Summary:       Core namespace for Google generated API client tools development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gapic
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic) = 0.0.1
Requires:      gem(google-style) >= 1.25.1 gem(google-style) < 1.26
Requires:      gem(minitest) >= 5.11 gem(minitest) < 6
Requires:      gem(minitest-autotest) >= 1.0 gem(minitest-autotest) < 2
Requires:      gem(minitest-focus) >= 1.1 gem(minitest-focus) < 2
Requires:      gem(minitest-rg) >= 5.2 gem(minitest-rg) < 6
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(redcarpet) >= 3.0 gem(redcarpet) < 4
Requires:      gem(yard) >= 0.9 gem(yard) < 1

%description   -n gem-gapic-devel
Core namespace for Google generated API client tools development package.

%description   -n gem-gapic-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gapic.


%package       -n gem-gapic-generator-cloud
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionpack) >= 5.2 gem(actionpack) < 7
Requires:      gem(gapic-generator) = 0.7.5
Requires:      gem(google-style) >= 1.25.1 gem(google-style) < 1.26
Requires:      gem(protobuf) >= 3.8 gem(protobuf) < 4
Provides:      gem(gapic-generator-cloud) = 0.7.5

%description   -n gem-gapic-generator-cloud
An API Client Generator for Ruby in Ruby!

%package       -n gapic-generator-cloud
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gapic-generator-cloud
Group:         Other
BuildArch:     noarch

Requires:      gem(gapic-generator-cloud) = 0.7.5

%description   -n gapic-generator-cloud
An API Client Generator for Ruby in Ruby executable(s).

%description   -n gapic-generator-cloud -l ru_RU.UTF-8
Исполнямка для самоцвета gapic-generator-cloud.


%package       -n gem-gapic-generator-cloud-doc
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gapic-generator-cloud
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gapic-generator-cloud) = 0.7.5

%description   -n gem-gapic-generator-cloud-doc
An API Client Generator for Ruby in Ruby documentation files.

%description   -n gem-gapic-generator-cloud-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gapic-generator-cloud.


%package       -n gem-gapic-generator-cloud-devel
Version:       0.7.5
Release:       alt1
Summary:       An API Client Generator for Ruby in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gapic-generator-cloud
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-generator-cloud) = 0.7.5
Requires:      gem(grpc-tools) >= 1.36.0 gem(grpc-tools) < 2
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(minitest-autotest) >= 1.0 gem(minitest-autotest) < 2
Requires:      gem(minitest-focus) >= 1.0 gem(minitest-focus) < 2
Requires:      gem(rake) >= 12.0 gem(rake) < 14

%description   -n gem-gapic-generator-cloud-devel
An API Client Generator for Ruby in Ruby development package.

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

%files
%_libexecdir/gapic-generator-ruby

%files         -n gem-gapic-common
%doc README.md
%ruby_gemspecdir/gapic-common-0.4.1.gemspec
%ruby_gemslibdir/gapic-common-0.4.1

%files         -n gem-gapic-common-doc
%doc README.md
%ruby_gemsdocdir/gapic-common-0.4.1

%files         -n gem-gapic-common-devel
%doc README.md

%files         -n gem-gapic-generator
%doc README.md
%ruby_gemspecdir/gapic-generator-0.7.5.gemspec
%ruby_gemslibdir/gapic-generator-0.7.5

%files         -n gapic-generator
%doc README.md
%_bindir/gapic-generator
%_bindir/protoc-gen-ruby_gapic

%files         -n gem-gapic-generator-doc
%doc README.md
%ruby_gemsdocdir/gapic-generator-0.7.5

%files         -n gem-gapic-generator-devel
%doc README.md

%files         -n gem-gapic-generator-ads
%doc README.md
%ruby_gemspecdir/gapic-generator-ads-0.7.5.gemspec
%ruby_gemslibdir/gapic-generator-ads-0.7.5

%files         -n protoc-gen-ruby-ads
%doc README.md
%_bindir/protoc-gen-ruby_ads

%files         -n gem-gapic-generator-ads-doc
%doc README.md
%ruby_gemsdocdir/gapic-generator-ads-0.7.5

%files         -n gem-gapic-generator-ads-devel
%doc README.md

%files         -n gem-gapic
%doc README.md
%ruby_gemspecdir/gapic-0.0.1.gemspec
%ruby_gemslibdir/gapic-0.0.1

%files         -n gem-gapic-doc
%doc README.md
%ruby_gemsdocdir/gapic-0.0.1

%files         -n gem-gapic-devel
%doc README.md

%files         -n gem-gapic-generator-cloud
%doc README.md
%ruby_gemspecdir/gapic-generator-cloud-0.7.5.gemspec
%ruby_gemslibdir/gapic-generator-cloud-0.7.5

%files         -n gapic-generator-cloud
%doc README.md
%_bindir/protoc-gen-ruby_cloud
%_bindir/ruby-cloud-docker-entrypoint

%files         -n gem-gapic-generator-cloud-doc
%doc README.md
%ruby_gemsdocdir/gapic-generator-cloud-0.7.5

%files         -n gem-gapic-generator-cloud-devel
%doc README.md


%changelog
* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 20210605-alt1
- + packaged gem with Ruby Policy 2.0
