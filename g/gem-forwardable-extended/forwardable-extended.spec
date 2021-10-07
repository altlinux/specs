%define        gemname forwardable-extended

Name:          gem-forwardable-extended
Version:       2.6.0
Release:       alt1.1
Summary:       Forwardable with hash, and instance variable extensions
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/envygeeks/forwardable-extended
Vcs:           https://github.com/envygeeks/forwardable-extended.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(forwardable-extended) = 2.6.0


%description
Forwardable with hash, and instance variable extensions.


%package       -n gem-forwardable-extended-doc
Version:       2.6.0
Release:       alt1.1
Summary:       Forwardable with hash, and instance variable extensions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета forwardable-extended
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(forwardable-extended) = 2.6.0

%description   -n gem-forwardable-extended-doc
Forwardable with hash, and instance variable extensions documentation files.

%description   -n gem-forwardable-extended-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета forwardable-extended.


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

%files         -n gem-forwardable-extended-doc
%ruby_gemdocdir


%changelog
* Tue Sep 14 2021 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1.1
- ! spec

* Tue Mar 16 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 2.6.0-alt1
- initial build
