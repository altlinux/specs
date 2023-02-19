%define        gemname ipaddr_extensions

Name:          gem-ipaddr-extensions
Version:       1.0.2
Release:       alt1
Summary:       A small gem that adds extra functionality to Rubys IPAddr class
License:       Unlicense
Group:         Development/Ruby
Url:           http://github.com/jamesotron/IPAddrExtensions
Vcs:           https://github.com/jamesotron/ipaddrextensions.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(ipaddr_extensions) = 1.0.2


%description
A small gem that adds extra functionality to Rubys IPAddr class


%package       -n gem-ipaddr-extensions-doc
Version:       1.0.2
Release:       alt1
Summary:       A small gem that adds extra functionality to Rubys IPAddr class documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ipaddr_extensions
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ipaddr_extensions) = 1.0.2

%description   -n gem-ipaddr-extensions-doc
A small gem that adds extra functionality to Rubys IPAddr class documentation
files.

%description   -n gem-ipaddr-extensions-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ipaddr_extensions.


%package       -n gem-ipaddr-extensions-devel
Version:       1.0.2
Release:       alt1
Summary:       A small gem that adds extra functionality to Rubys IPAddr class development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ipaddr_extensions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ipaddr_extensions) = 1.0.2
Requires:      gem(rake) >= 0

%description   -n gem-ipaddr-extensions-devel
A small gem that adds extra functionality to Rubys IPAddr class development
package.

%description   -n gem-ipaddr-extensions-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ipaddr_extensions.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-ipaddr-extensions-doc
%doc README
%ruby_gemdocdir

%files         -n gem-ipaddr-extensions-devel
%doc README


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
