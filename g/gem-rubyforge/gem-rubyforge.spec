# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname rubyforge

Name:          gem-rubyforge
Version:       2.0.4
Release:       alt1.1
Summary:       A script which automates a limited set of rubyforge operations
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/devrandom/rubyforge
Vcs:           https://github.com/devrandom/rubyforge.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         hoe-setup.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(json_pure) >= 1.1.7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(json_pure) >= 1.1.7
Provides:      gem(rubyforge) = 2.0.4


%description
A script which automates a limited set of rubyforge operations.


%package       -n rubyforge
Version:       2.0.4
Release:       alt1.1
Summary:       A script which automates a limited set of rubyforge operations executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rubyforge
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubyforge) = 2.0.4

%description   -n rubyforge
A script which automates a limited set of rubyforge operations executable(s).

%description   -n rubyforge -l ru_RU.UTF-8
Исполнямка для самоцвета rubyforge.


%package       -n gem-rubyforge-doc
Version:       2.0.4
Release:       alt1.1
Summary:       A script which automates a limited set of rubyforge operations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubyforge
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubyforge) = 2.0.4

%description   -n gem-rubyforge-doc
A script which automates a limited set of rubyforge operations documentation
files.

%description   -n gem-rubyforge-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubyforge.


%package       -n gem-rubyforge-devel
Version:       2.0.4
Release:       alt1.1
Summary:       A script which automates a limited set of rubyforge operations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubyforge
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubyforge) = 2.0.4

%description   -n gem-rubyforge-devel
A script which automates a limited set of rubyforge operations development
package.

%description   -n gem-rubyforge-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubyforge.


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
%doc README.txt
%ruby_gemspec
%ruby_gemlibdir

%files         -n rubyforge
%doc README.txt
%_bindir/rubyforge

%files         -n gem-rubyforge-doc
%doc README.txt
%ruby_gemdocdir

%files         -n gem-rubyforge-devel
%doc README.txt


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 2.0.4-alt1.1
- ! of closing build deps under check condition

* Mon Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.4-alt1
- + packaged gem with usage Ruby Policy 2.0
