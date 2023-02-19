%define        gemname childlabor

Name:          gem-childlabor
Version:       0.0.3
Release:       alt1
Summary:       Put your children to work
License:       Unlicense
Group:         Development/Ruby
Url:           https://rubygems.org/gems/childlabor
Vcs:           git://git.altlinux.org/gears/g/gem-childlabor.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(childlabor) = 0.0.3


%description
ChildLabor is a gem that helps manage child processes.


%package       -n gem-childlabor-doc
Version:       0.0.3
Release:       alt1
Summary:       Put your children to work documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета childlabor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(childlabor) = 0.0.3

%description   -n gem-childlabor-doc
Put your children to work documentation files.

ChildLabor is a gem that helps manage child processes.

%description   -n gem-childlabor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета childlabor.


%package       -n gem-childlabor-devel
Version:       0.0.3
Release:       alt1
Summary:       Put your children to work development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета childlabor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(childlabor) = 0.0.3
Requires:      gem(rspec) >= 0

%description   -n gem-childlabor-devel
Put your children to work development package.

ChildLabor is a gem that helps manage child processes.

%description   -n gem-childlabor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета childlabor.


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

%files         -n gem-childlabor-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-childlabor-devel
%doc README.md


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.3-alt1
- + packaged gem with Ruby Policy 2.0
