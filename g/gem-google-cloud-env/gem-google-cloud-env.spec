%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname google-cloud-env

Name:          gem-google-cloud-env
Version:       2.3.1
Release:       alt1
Summary:       Google Cloud Platform hosting environment information
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/googleapis/google-cloud-ruby/tree/master/google-cloud-env
Vcs:           https://github.com/googleapis/google-cloud-ruby.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(autotest-suffix) >= 1.1
BuildRequires: gem(base64) >= 0.2
BuildRequires: gem(faraday) >= 1.0
BuildRequires: gem(google-style) >= 1.31.0
BuildRequires: gem(minitest) >= 5.16
BuildRequires: gem(minitest-autotest) >= 1.0
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(minitest-rg) >= 5.2
BuildRequires: gem(redcarpet) >= 3.0
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(autotest-suffix) >= 2
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(google-style) >= 1.32
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-autotest) >= 2
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(minitest-rg) >= 6
BuildConflicts: gem(redcarpet) >= 4
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
Requires:      ruby >= 3.1
Requires:      gem(base64) >= 0.2
Requires:      gem(faraday) >= 1.0
Conflicts:     gem(base64) >= 1
Conflicts:     gem(faraday) >= 3
Provides:      gem(google-cloud-env) = 2.3.1

%description
google-cloud-env provides information on the Google Cloud Platform hosting
environment. Applications can use this library to determine hosting context
information such as the project ID, whether App Engine is running, what tags are
set on the VM instance, and much more.


%if_enabled    doc
%package       -n gem-google-cloud-env-doc
Version:       2.3.1
Release:       alt1
Summary:       Google Cloud Platform hosting environment information documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-env
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-env) = 2.3.1

%description   -n gem-google-cloud-env-doc
Google Cloud Platform hosting environment information documentation
files.

google-cloud-env provides information on the Google Cloud Platform hosting
environment. Applications can use this library to determine hosting context
information such as the project ID, whether App Engine is running, what tags are
set on the VM instance, and much more.

%description   -n gem-google-cloud-env-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-env.
%endif


%if_enabled    devel
%package       -n gem-google-cloud-env-devel
Version:       2.3.1
Release:       alt1
Summary:       Google Cloud Platform hosting environment information development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-cloud-env
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-env) = 2.3.1
Requires:      gem(autotest-suffix) >= 1.1
Requires:      gem(base64) >= 0.2
Requires:      gem(faraday) >= 1.0
Requires:      gem(google-style) >= 1.31.0
Requires:      gem(minitest) >= 5.16
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(minitest-rg) >= 5.2
Requires:      gem(redcarpet) >= 3.0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(autotest-suffix) >= 2
Conflicts:     gem(base64) >= 1
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(google-style) >= 1.32
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(minitest-rg) >= 6
Conflicts:     gem(redcarpet) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-google-cloud-env-devel
Google Cloud Platform hosting environment information development
package.

google-cloud-env provides information on the Google Cloud Platform hosting
environment. Applications can use this library to determine hosting context
information such as the project ID, whether App Engine is running, what tags are
set on the VM instance, and much more.

%description   -n gem-google-cloud-env-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-cloud-env.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-google-cloud-env-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-google-cloud-env-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%endif


%changelog
* Fri Oct 31 2025 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt1
- ^ 1.6.0 -> 2.3.1

* Sun Oct 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- ^ 1.5.0 -> 1.6.0

* Tue Jun 08 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- + packaged gem with Ruby Policy 2.0
