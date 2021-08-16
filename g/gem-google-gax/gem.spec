%define        gemname google-gax

Name:          gem-google-gax
Version:       1.8.1
Release:       alt1
Summary:       Aids the development of APIs for clients and servers based on GRPC and Google APIs conventions
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           https://github.com/googleapis/gax-ruby
Vcs:           https://github.com/googleapis/gax-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(googleauth) >= 0.9 gem(googleauth) < 1
BuildRequires: gem(grpc) >= 1.24 gem(grpc) < 2
BuildRequires: gem(googleapis-common-protos) >= 1.3.9 gem(googleapis-common-protos) < 2.0
BuildRequires: gem(google-protobuf) >= 3.9 gem(google-protobuf) < 4
BuildRequires: gem(rly) >= 0.2.3 gem(rly) < 0.3
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(rubocop) >= 0.49.0 gem(rubocop) < 2
BuildRequires: gem(simplecov) >= 0.9 gem(simplecov) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(googleauth) >= 0.9 gem(googleauth) < 1
Requires:      gem(grpc) >= 1.24 gem(grpc) < 2
Requires:      gem(googleapis-common-protos) >= 1.3.9 gem(googleapis-common-protos) < 2.0
Requires:      gem(google-protobuf) >= 3.9 gem(google-protobuf) < 4
Requires:      gem(rly) >= 0.2.3 gem(rly) < 0.3
Provides:      gem(google-gax) = 1.8.1


%description
Google API Extensions


%package       -n gem-google-gax-doc
Version:       1.8.1
Release:       alt1
Summary:       Aids the development of APIs for clients and servers based on GRPC and Google APIs conventions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-gax
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-gax) = 1.8.1

%description   -n gem-google-gax-doc
Aids the development of APIs for clients and servers based on GRPC and Google
APIs conventions documentation files.

Google API Extensions

%description   -n gem-google-gax-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-gax.


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

%files         -n gem-google-gax-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Jun 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.8.1-alt1
- + packaged gem with Ruby Policy 2.0
