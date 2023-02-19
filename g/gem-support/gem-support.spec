%define        gemname support

Name:          gem-support
Version:       0.18
Release:       alt1
Summary:       test gem
License:       Unlicense
Group:         Development/Ruby
Url:           git://git.altlinux.org/gears/g/gem-support.git
Vcs:           git://git.altlinux.org/gears/g/gem-support.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(support) = 0.18


%description
test gem


%package       -n gem-support-doc
Version:       0.18
Release:       alt1
Summary:       test gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета support
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(support) = 0.18

%description   -n gem-support-doc
test gem documentation files.

%description   -n gem-support-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета support.


%package       -n gem-support-devel
Version:       0.18
Release:       alt1
Summary:       test gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета support
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(support) = 0.18

%description   -n gem-support-devel
test gem development package.

%description   -n gem-support-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета support.


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

%files         -n gem-support-doc
%ruby_gemdocdir

%files         -n gem-support-devel


%changelog
* Sun Feb 05 2023 Pavel Skrylev <majioa@altlinux.org> 0.18-alt1
- + packaged gem with Ruby Policy 2.0
