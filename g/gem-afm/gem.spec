%define        gemname afm

Name:          gem-afm
Version:       0.2.2
Release:       alt1
Summary:       reading Adobe Font Metrics (afm) files
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/halfbyte/afm
Vcs:           https://github.com/halfbyte/afm.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 10.3 gem(rake) < 14
BuildRequires: gem(rdoc) >= 4.1 gem(rdoc) < 7
BuildRequires: gem(minitest) >= 5.3 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Provides:      gem(afm) = 0.2.2


%description
a simple library to read afm files and use the data conveniently


%package       -n gem-afm-doc
Version:       0.2.2
Release:       alt1
Summary:       reading Adobe Font Metrics (afm) files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета afm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(afm) = 0.2.2

%description   -n gem-afm-doc
reading Adobe Font Metrics (afm) files documentation files.

a simple library to read afm files and use the data conveniently

%description   -n gem-afm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета afm.


%package       -n gem-afm-devel
Version:       0.2.2
Release:       alt1
Summary:       reading Adobe Font Metrics (afm) files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета afm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(afm) = 0.2.2
Requires:      gem(rake) >= 10.3 gem(rake) < 14
Requires:      gem(rdoc) >= 4.1 gem(rdoc) < 7
Requires:      gem(minitest) >= 5.3 gem(minitest) < 6

%description   -n gem-afm-devel
reading Adobe Font Metrics (afm) files development package.

a simple library to read afm files and use the data conveniently

%description   -n gem-afm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета afm.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-afm-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-afm-devel
%doc README.rdoc


%changelog
* Sun Sep 12 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt1
- + packaged gem with Ruby Policy 2.0
