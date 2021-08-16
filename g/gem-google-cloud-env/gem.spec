%define        gemname google-cloud-env

Name:          gem-google-cloud-env
Version:       1.5.0
Release:       alt1
Summary:       Google Cloud Platform hosting environment information
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/googleapis/google-cloud-ruby/tree/master/google-cloud-env
Vcs:           https://github.com/googleapis/google-cloud-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(faraday) >= 0.17.3 gem(faraday) < 2.0
BuildRequires: gem(minitest) >= 5.10 gem(minitest) < 6
BuildRequires: gem(simplecov) >= 0.9 gem(simplecov) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(faraday) >= 0.17.3 gem(faraday) < 2.0
Provides:      gem(google-cloud-env) = 1.5.0


%description
google-cloud-env provides information on the Google Cloud Platform hosting
environment. Applications can use this library to determine hosting context
information such as the project ID, whether App Engine is running, what tags are
set on the VM instance, and much more.


%package       -n gem-google-cloud-env-doc
Version:       1.5.0
Release:       alt1
Summary:       Google Cloud Platform hosting environment information documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-env
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-env) = 1.5.0

%description   -n gem-google-cloud-env-doc
Google Cloud Platform hosting environment information documentation
files.

google-cloud-env provides information on the Google Cloud Platform hosting
environment. Applications can use this library to determine hosting context
information such as the project ID, whether App Engine is running, what tags are
set on the VM instance, and much more.

%description   -n gem-google-cloud-env-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-env.


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

%files         -n gem-google-cloud-env-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Jun 08 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- + packaged gem with Ruby Policy 2.0
