Name:          common-protos-ruby
Version:       20210531
Release:       alt1
Summary:       Ruby protocol buffer classes generated
License:       Apache-2.0
Group:         Other
Url:           https://github.com/googleapis/common-protos-ruby
Vcs:           https://github.com/googleapis/common-protos-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(google-protobuf) >= 3.14 gem(google-protobuf) < 4
# BuildRequires: gem(grpc) >= 1.27 gem(grpc) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names common-protos-ruby

%description
This repository is a home for the protocol buffer types which are common
dependencies throughout the Google API ecosystem, generated for Ruby. The
protobuf definitions for these generated Ruby classes are provided in the API
Common Protos repository.


%package       -n gem-googleapis-common-protos-types
Version:       1.0.6
Release:       alt1
Summary:       Common protobuf types used in Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-protobuf) >= 3.14 gem(google-protobuf) < 4
Provides:      gem(googleapis-common-protos-types) = 1.0.6

%description   -n gem-googleapis-common-protos-types
Common protocol buffer types used by Google APIs


%package       -n googleapis-common-protos-types-doc
Version:       1.0.6
Release:       alt1
Summary:       Common protobuf types used in Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета googleapis-common-protos-types
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(googleapis-common-protos-types) = 1.0.6

%description   -n googleapis-common-protos-types-doc
Common protobuf types used in Google APIs documentation files.

Common protocol buffer types used by Google APIs

%description   -n googleapis-common-protos-types-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета googleapis-common-protos-types.


%package       -n gem-grpc-google-iam-v1
Version:       0.6.11
Release:       alt1
Summary:       Common protos and gRPC services for Google IAM
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(googleapis-common-protos) >= 1.3.11 gem(googleapis-common-protos) < 2.0
Requires:      gem(google-protobuf) >= 3.14 gem(google-protobuf) < 4
Requires:      gem(grpc) >= 1.27 gem(grpc) < 2
Provides:      gem(grpc-google-iam-v1) = 0.6.11

%description   -n gem-grpc-google-iam-v1
Common protos and gRPC services for Google IAM.


%package       -n grpc-google-iam-v1-doc
Version:       0.6.11
Release:       alt1
Summary:       Common protos and gRPC services for Google IAM documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета grpc-google-iam-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(grpc-google-iam-v1) = 0.6.11

%description   -n grpc-google-iam-v1-doc
Common protos and gRPC services for Google IAM documentation files.

%description   -n grpc-google-iam-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета grpc-google-iam-v1.


%package       -n gem-googleapis-common-protos
Version:       1.3.11
Release:       alt1
Summary:       Common gRPC and protocol buffer classes used in Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(googleapis-common-protos-types) >= 1.0.6 gem(googleapis-common-protos-types) < 2.0
Requires:      gem(google-protobuf) >= 3.14 gem(google-protobuf) < 4
Requires:      gem(grpc) >= 1.27 gem(grpc) < 2
Provides:      gem(googleapis-common-protos) = 1.3.11

%description   -n gem-googleapis-common-protos
Common gRPC and protocol buffer classes used in Google APIs.


%package       -n googleapis-common-protos-doc
Version:       1.3.11
Release:       alt1
Summary:       Common gRPC and protocol buffer classes used in Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета googleapis-common-protos
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(googleapis-common-protos) = 1.3.11

%description   -n googleapis-common-protos-doc
Common gRPC and protocol buffer classes used in Google APIs documentation files.

%description   -n googleapis-common-protos-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета googleapis-common-protos.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files

%files         -n gem-googleapis-common-protos-types
%doc README.md
%ruby_gemspecdir/googleapis-common-protos-types-1.0.6.gemspec
%ruby_gemslibdir/googleapis-common-protos-types-1.0.6

%files         -n googleapis-common-protos-types-doc
%doc README.md
%ruby_gemsdocdir/googleapis-common-protos-types-1.0.6

%files         -n gem-grpc-google-iam-v1
%doc README.md
%ruby_gemspecdir/grpc-google-iam-v1-0.6.11.gemspec
%ruby_gemslibdir/grpc-google-iam-v1-0.6.11

%files         -n grpc-google-iam-v1-doc
%doc README.md
%ruby_gemsdocdir/grpc-google-iam-v1-0.6.11

%files         -n gem-googleapis-common-protos
%doc README.md
%ruby_gemspecdir/googleapis-common-protos-1.3.11.gemspec
%ruby_gemslibdir/googleapis-common-protos-1.3.11

%files         -n googleapis-common-protos-doc
%doc README.md
%ruby_gemsdocdir/googleapis-common-protos-1.3.11


%changelog
* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 20210531-alt1
- + packaged gem with Ruby Policy 2.0
