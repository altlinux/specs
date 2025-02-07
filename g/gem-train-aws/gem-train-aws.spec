%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname train-aws

Name:          gem-train-aws
Version:       0.2.43
Release:       alt1
Summary:       AWS API Transport for Train
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/inspec/train-aws
Vcs:           https://github.com/inspec/train-aws.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(train-core) >= 3.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(chefstyle) >= 0
BuildRequires: gem(aws-sdk-resources) >= 3.0
BuildConflicts: gem(aws-sdk-resources) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(aws-sdk-resources) >= 3.0
Conflicts:     gem(aws-sdk-resources) >= 4
Provides:      gem(train-aws) = 0.2.43


%description
Allows applications using Train to speak to AWS; handles authentication,
cacheing, and SDK dependency management.


%if_enabled    doc
%package       -n gem-train-aws-doc
Version:       0.2.43
Release:       alt1
Summary:       AWS API Transport for Train documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-aws
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-aws) = 0.2.43

%description   -n gem-train-aws-doc
AWS API Transport for Train documentation files.

Allows applications using Train to speak to AWS; handles authentication,
cacheing, and SDK dependency management.

%description   -n gem-train-aws-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-aws.
%endif


%if_enabled    devel
%package       -n gem-train-aws-devel
Version:       0.2.43
Release:       alt1
Summary:       AWS API Transport for Train development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-aws
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-aws) = 0.2.43
Requires:      gem(train-core) >= 3.0
Requires:      gem(pry) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(m) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(chefstyle) >= 0
Conflicts:     gem(train-core) >= 4

%description   -n gem-train-aws-devel
AWS API Transport for Train development package.

Allows applications using Train to speak to AWS; handles authentication,
cacheing, and SDK dependency management.

%description   -n gem-train-aws-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета train-aws.
%endif


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

%if_enabled    doc
%files         -n gem-train-aws-doc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-train-aws-devel
%endif


%changelog
* Mon Nov 11 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.43-alt1
- ^ 0.2.25 -> 0.2.43

* Wed Feb 15 2023 Pavel Skrylev <majioa@altlinux.org> 0.2.25-alt1
- ^ 0.2.16 -> 0.2.25

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.16-alt1
- + packaged gem with Ruby Policy 2.0
