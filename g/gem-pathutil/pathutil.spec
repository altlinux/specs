%define        gemname pathutil

Name:          gem-pathutil
Version:       0.16.2
Release:       alt1.1
Summary:       Almost like Pathname but just a little less insane
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/envygeeks/pathutil.git
Vcs:           https://github.com/envygeeks/pathutil.git.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(forwardable-extended) >= 2.6 gem(forwardable-extended) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(forwardable-extended) >= 2.6 gem(forwardable-extended) < 3
Provides:      gem(pathutil) = 0.16.2


%description
Like Pathname but a little less insane.


%package       -n gem-pathutil-doc
Version:       0.16.2
Release:       alt1.1
Summary:       Almost like Pathname but just a little less insane documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pathutil
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pathutil) = 0.16.2

%description   -n gem-pathutil-doc
Almost like Pathname but just a little less insane documentation files.

Like Pathname but a little less insane.

%description   -n gem-pathutil-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pathutil.


%package       -n gem-pathutil-devel
Version:       0.16.2
Release:       alt1.1
Summary:       Almost like Pathname but just a little less insane development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pathutil
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pathutil) = 0.16.2

%description   -n gem-pathutil-devel
Almost like Pathname but just a little less insane development package.

Like Pathname but a little less insane.

%description   -n gem-pathutil-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pathutil.


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

%files         -n gem-pathutil-doc
%ruby_gemdocdir

%files         -n gem-pathutil-devel


%changelog
* Tue Sep 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.16.2-alt1.1
- ! spec

* Fri Mar 19 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.16.2-alt1
- initial build
