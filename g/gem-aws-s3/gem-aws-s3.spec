%define        _unpackaged_files_terminate_build 1
%define        gemname aws-s3

Name:          gem-aws-s3
Version:       0.6.3.79
Release:       alt1
Summary:       Client library for Amazon's Simple Storage Service's REST API
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/marcel/aws-s3
Vcs:           https://github.com/marcel/aws-s3.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         0.6.3.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(xml-simple) >= 0
BuildRequires: gem(builder) >= 0
BuildRequires: gem(mime-types) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(xml-simple) >= 0
Requires:      gem(builder) >= 0
Requires:      gem(mime-types) >= 0
Provides:      gem(aws-s3) = 0.6.3.79

%ruby_bindir_to %ruby_bindir

%description
Client library for Amazon's Simple Storage Service's REST API


%package       -n s3sh
Version:       0.6.3.79
Release:       alt1
Summary:       Client library for Amazon's Simple Storage Service's REST API executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета aws-s3
Group:         Other
BuildArch:     noarch

Requires:      gem(aws-s3) = 0.6.3.79

%description   -n s3sh
Client library for Amazon's Simple Storage Service's REST API executable(s).

%description   -n s3sh -l ru_RU.UTF-8
Исполнямка для самоцвета aws-s3.


%package       -n gem-aws-s3-doc
Version:       0.6.3.79
Release:       alt1
Summary:       Client library for Amazon's Simple Storage Service's REST API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aws-s3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(aws-s3) = 0.6.3.79

%description   -n gem-aws-s3-doc
Client library for Amazon's Simple Storage Service's REST API documentation
files.

%description   -n gem-aws-s3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aws-s3.


%package       -n gem-aws-s3-devel
Version:       0.6.3.79
Release:       alt1
Summary:       Client library for Amazon's Simple Storage Service's REST API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aws-s3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(aws-s3) = 0.6.3.79

%description   -n gem-aws-s3-devel
Client library for Amazon's Simple Storage Service's REST API development
package.

%description   -n gem-aws-s3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aws-s3.


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n s3sh
%doc README.rdoc
%ruby_bindir/s3sh

%files         -n gem-aws-s3-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-aws-s3-devel
%doc README.rdoc


%changelog
* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 0.6.3.79-alt1
- + packaged gem with Ruby Policy 2.0
