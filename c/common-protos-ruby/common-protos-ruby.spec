# vim: set ft=spec: -*- rpm-spec -*-
Name:          common-protos-ruby
Version:       20230122
Release:       alt1
Summary:       Ruby protocol buffer classes generated
License:       Apache-2.0
Group:         Other
Url:           https://github.com/googleapis/common-protos-ruby
Vcs:           https://github.com/googleapis/common-protos-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(google-protobuf) >= 3.14
BuildRequires: gem(grpc) >= 1.27
BuildConflicts: gem(google-protobuf) >= 4
BuildConflicts: gem(grpc) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      ruby-common-protos-ruby = %EVR


%description
This repository is a home for the protocol buffer types which are common
dependencies throughout the Google API ecosystem, generated for Ruby. The
protobuf definitions for these generated Ruby classes are provided in the API
Common Protos repository.


%package       -n gem-grpc-google-iam-v1
Version:       1.2.0
Release:       alt1
Summary:       Ruby protocol buffer classes generated
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(googleapis-common-protos) >= 1.3.12
Requires:      gem(google-protobuf) >= 3.14
Requires:      gem(grpc) >= 1.27
Conflicts:     gem(googleapis-common-protos) >= 2.0
Conflicts:     gem(google-protobuf) >= 4
Conflicts:     gem(grpc) >= 2
Provides:      gem(grpc-google-iam-v1) = 1.2.0

%description   -n gem-grpc-google-iam-v1
Common protos and gRPC services for Google IAM.


%package       -n grpc-google-iam-v1-doc
Version:       1.2.0
Release:       alt1
Summary:       Ruby protocol buffer classes generated documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета grpc-google-iam-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(grpc-google-iam-v1) = 1.2.0

%description   -n grpc-google-iam-v1-doc
Ruby protocol buffer classes generated documentation files.

Common protos and gRPC services for Google IAM.

%description   -n grpc-google-iam-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета grpc-google-iam-v1.


%package       -n grpc-google-iam-v1-devel
Version:       1.2.0
Release:       alt1
Summary:       Ruby protocol buffer classes generated development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета grpc-google-iam-v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(grpc-google-iam-v1) = 1.2.0

%description   -n grpc-google-iam-v1-devel
Ruby protocol buffer classes generated development package.

Common protos and gRPC services for Google IAM.

%description   -n grpc-google-iam-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета grpc-google-iam-v1.


%package       -n gem-google-cloud-common
Version:       1.1.0
Release:       alt1
Summary:       Common protocol buffer types used in Google Cloud APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-protobuf) >= 3.14
Requires:      gem(googleapis-common-protos-types) >= 1.2
Conflicts:     gem(google-protobuf) >= 4
Conflicts:     gem(googleapis-common-protos-types) >= 2
Provides:      gem(google-cloud-common) = 1.1.0

%description   -n gem-google-cloud-common
Common protocol buffer types used by Google Cloud APIs


%package       -n google-cloud-common-doc
Version:       1.1.0
Release:       alt1
Summary:       Common protocol buffer types used in Google Cloud APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-common
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-common) = 1.1.0

%description   -n google-cloud-common-doc
Common protocol buffer types used in Google Cloud APIs documentation
files.

Common protocol buffer types used by Google Cloud APIs

%description   -n google-cloud-common-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-common.


%package       -n google-cloud-common-devel
Version:       1.1.0
Release:       alt1
Summary:       Common protocol buffer types used in Google Cloud APIs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-cloud-common
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-common) = 1.1.0

%description   -n google-cloud-common-devel
Common protocol buffer types used in Google Cloud APIs development
package.

Common protocol buffer types used by Google Cloud APIs

%description   -n google-cloud-common-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-cloud-common.


%package       -n gem-google-apps-script-type
Version:       0.1.0
Release:       alt1
Summary:       Common protocol buffer types used by Google Apps Script related client libraries
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(googleapis-common-protos-types) >= 1.4
Requires:      gem(google-protobuf) >= 3.14
Conflicts:     gem(googleapis-common-protos-types) >= 2
Conflicts:     gem(google-protobuf) >= 4
Provides:      gem(google-apps-script-type) = 0.1.0

%description   -n gem-google-apps-script-type
Common protocol buffer types used by Google Apps Script related client libraries


%package       -n google-apps-script-type-doc
Version:       0.1.0
Release:       alt1
Summary:       Common protocol buffer types used by Google Apps Script related client libraries documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apps-script-type
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apps-script-type) = 0.1.0

%description   -n google-apps-script-type-doc
Common protocol buffer types used by Google Apps Script related client libraries
documentation files.

%description   -n google-apps-script-type-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apps-script-type.


%package       -n google-apps-script-type-devel
Version:       0.1.0
Release:       alt1
Summary:       Common protocol buffer types used by Google Apps Script related client libraries development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apps-script-type
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apps-script-type) = 0.1.0

%description   -n google-apps-script-type-devel
Common protocol buffer types used by Google Apps Script related client libraries
development package.

%description   -n google-apps-script-type-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apps-script-type.


%package       -n gem-googleapis-common-protos
Version:       1.4.0
Release:       alt1
Summary:       Ruby protocol buffer classes generated
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(googleapis-common-protos-types) >= 1.2
Requires:      gem(google-protobuf) >= 3.14
Requires:      gem(grpc) >= 1.27
Conflicts:     gem(googleapis-common-protos-types) >= 2
Conflicts:     gem(google-protobuf) >= 4
Conflicts:     gem(grpc) >= 2
Provides:      gem(googleapis-common-protos) = 1.4.0

%description   -n gem-googleapis-common-protos
Common gRPC and protocol buffer classes used in Google APIs.


%package       -n googleapis-common-protos-doc
Version:       1.4.0
Release:       alt1
Summary:       Ruby protocol buffer classes generated documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета googleapis-common-protos
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(googleapis-common-protos) = 1.4.0

%description   -n googleapis-common-protos-doc
Ruby protocol buffer classes generated documentation files.

Common gRPC and protocol buffer classes used in Google APIs.

%description   -n googleapis-common-protos-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета googleapis-common-protos.


%package       -n googleapis-common-protos-devel
Version:       1.4.0
Release:       alt1
Summary:       Ruby protocol buffer classes generated development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета googleapis-common-protos
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(googleapis-common-protos) = 1.4.0

%description   -n googleapis-common-protos-devel
Ruby protocol buffer classes generated development package.

Common gRPC and protocol buffer classes used in Google APIs.

%description   -n googleapis-common-protos-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета googleapis-common-protos.


%package       -n gem-googleapis-common-protos-types
Version:       1.5.0
Release:       alt1
Summary:       Ruby protocol buffer classes generated
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-protobuf) >= 3.14
Conflicts:     gem(google-protobuf) >= 4
Provides:      gem(googleapis-common-protos-types) = 1.5.0

%description   -n gem-googleapis-common-protos-types
Common protocol buffer types used by Google APIs


%package       -n googleapis-common-protos-types-doc
Version:       1.5.0
Release:       alt1
Summary:       Ruby protocol buffer classes generated documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета googleapis-common-protos-types
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(googleapis-common-protos-types) = 1.5.0

%description   -n googleapis-common-protos-types-doc
Ruby protocol buffer classes generated documentation files.

Common protocol buffer types used by Google APIs

%description   -n googleapis-common-protos-types-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета googleapis-common-protos-types.


%package       -n googleapis-common-protos-types-devel
Version:       1.5.0
Release:       alt1
Summary:       Ruby protocol buffer classes generated development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета googleapis-common-protos-types
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(googleapis-common-protos-types) = 1.5.0

%description   -n googleapis-common-protos-types-devel
Ruby protocol buffer classes generated development package.

Common protocol buffer types used by Google APIs

%description   -n googleapis-common-protos-types-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета googleapis-common-protos-types.


%package       -n common-protos-ruby-devel
Version:       20230122
Release:       alt1
Summary:       Ruby protocol buffer classes generated development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета common-protos-ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      common-protos-ruby = %EVR
Requires:      gem(googleapis-common-protos) >= 0
Requires:      gem(googleapis-common-protos-types) >= 0
Requires:      gem(grpc-google-iam-v1) >= 0

%description   -n common-protos-ruby-devel
Ruby protocol buffer classes generated development package.

This repository is a home for the protocol buffer types which are common
dependencies throughout the Google API ecosystem, generated for Ruby. The
protobuf definitions for these generated Ruby classes are provided in the API
Common Protos repository.

%description   -n common-protos-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета common-protos-ruby.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files

%files         -n gem-grpc-google-iam-v1
%doc README.md
%ruby_gemspecdir/grpc-google-iam-v1-1.2.0.gemspec
%ruby_gemslibdir/grpc-google-iam-v1-1.2.0

%files         -n grpc-google-iam-v1-doc
%doc README.md
%ruby_gemsdocdir/grpc-google-iam-v1-1.2.0

%files         -n grpc-google-iam-v1-devel
%doc README.md

%files         -n gem-google-cloud-common
%doc README.md
%ruby_gemspecdir/google-cloud-common-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-common-1.1.0

%files         -n google-cloud-common-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-common-1.1.0

%files         -n google-cloud-common-devel
%doc README.md

%files         -n gem-google-apps-script-type
%doc README.md
%ruby_gemspecdir/google-apps-script-type-0.1.0.gemspec
%ruby_gemslibdir/google-apps-script-type-0.1.0

%files         -n google-apps-script-type-doc
%doc README.md
%ruby_gemsdocdir/google-apps-script-type-0.1.0

%files         -n google-apps-script-type-devel
%doc README.md

%files         -n gem-googleapis-common-protos
%doc README.md
%ruby_gemspecdir/googleapis-common-protos-1.4.0.gemspec
%ruby_gemslibdir/googleapis-common-protos-1.4.0

%files         -n googleapis-common-protos-doc
%doc README.md
%ruby_gemsdocdir/googleapis-common-protos-1.4.0

%files         -n googleapis-common-protos-devel
%doc README.md

%files         -n gem-googleapis-common-protos-types
%doc README.md
%ruby_gemspecdir/googleapis-common-protos-types-1.5.0.gemspec
%ruby_gemslibdir/googleapis-common-protos-types-1.5.0

%files         -n googleapis-common-protos-types-doc
%doc README.md
%ruby_gemsdocdir/googleapis-common-protos-types-1.5.0

%files         -n googleapis-common-protos-types-devel
%doc README.md

%files         -n common-protos-ruby-devel


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 20230122-alt1
- ^ 20210531 -> 20230122

* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 20210531-alt1
- + packaged gem with Ruby Policy 2.0
