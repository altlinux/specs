%define        gemname corefoundation

Name:          gem-corefoundation
Version:       0.3.14
Release:       alt1
Summary:       Ruby wrapper for macOS Core Foundation framework
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/chef/corefoundation
Vcs:           https://github.com/chef/corefoundation.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ffi) >= 1.15.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(chefstyle) >= 2.2.2
BuildRequires: gem(yard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
Requires:      gem(ffi) >= 1.15.0
Provides:      gem(corefoundation) = 0.3.14


%description
Ruby wrapper for macOS Core Foundation framework.


%package       -n gem-corefoundation-doc
Version:       0.3.14
Release:       alt1
Summary:       Ruby wrapper for macOS Core Foundation framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета corefoundation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(corefoundation) = 0.3.14

%description   -n gem-corefoundation-doc
Ruby wrapper for macOS Core Foundation framework documentation files.

%description   -n gem-corefoundation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета corefoundation.


%package       -n gem-corefoundation-devel
Version:       0.3.14
Release:       alt1
Summary:       Ruby wrapper for macOS Core Foundation framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета corefoundation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(corefoundation) = 0.3.14
Requires:      gem(rspec) >= 3.0
Requires:      gem(rake) >= 0
Requires:      gem(chefstyle) >= 2.2.2
Requires:      gem(yard) >= 0

%description   -n gem-corefoundation-devel
Ruby wrapper for macOS Core Foundation framework development package.

%description   -n gem-corefoundation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета corefoundation.


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

%files         -n gem-corefoundation-doc
%ruby_gemdocdir

%files         -n gem-corefoundation-devel


%changelog
* Thu Apr 21 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.14-alt1
- + packaged gem with Ruby Policy 2.0
