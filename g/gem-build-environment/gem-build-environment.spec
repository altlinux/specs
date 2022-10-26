%define        gemname build-environment

Name:          gem-build-environment
Version:       1.13.0
Release:       alt1
Summary:       A nested hash data structure for controlling build environments
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/build-environment
Vcs:           https://github.com/ioquatix/build-environment.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(covered) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rspec) >= 3.4 gem(rspec) < 4
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(build-environment) = 1.13.0

%description
A nested hash data structure for controlling build environments.


%package       -n gem-build-environment-doc
Version:       1.13.0
Release:       alt1
Summary:       A nested hash data structure for controlling build environments documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета build-environment
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(build-environment) = 1.13.0

%description   -n gem-build-environment-doc
A nested hash data structure for controlling build environments documentation
files.

%description   -n gem-build-environment-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета build-environment.


%package       -n gem-build-environment-devel
Version:       1.13.0
Release:       alt1
Summary:       A nested hash data structure for controlling build environments development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета build-environment
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(build-environment) = 1.13.0
Requires:      gem(covered) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rspec) >= 3.4 gem(rspec) < 4
Requires:      gem(rake) >= 0

%description   -n gem-build-environment-devel
A nested hash data structure for controlling build environments development
package.

%description   -n gem-build-environment-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета build-environment.


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

%files         -n gem-build-environment-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-build-environment-devel
%doc README.md


%changelog
* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- + packaged gem with Ruby Policy 2.0
