%define        gemname facterdb

Name:          gem-facterdb
Version:       1.19.0
Release:       alt1
Summary:       A Database of OS facts provided by Facter
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/voxpupuli/facterdb
Vcs:           https://github.com/voxpupuli/facterdb.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(facter) < 5.0.0
BuildRequires: gem(jgrep) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names facts
Requires:      gem(facter) < 5.0.0
Requires:      gem(jgrep) >= 0
Provides:      gem(facterdb) = 1.19.0


%description
Contains facts from many Facter version on many Operating Systems


%package       -n facterdb
Version:       1.19.0
Release:       alt1
Summary:       A Database of OS facts provided by Facter executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета facterdb
Group:         Other
BuildArch:     noarch

Requires:      gem(facterdb) = 1.19.0

%description   -n facterdb
A Database of OS facts provided by Facter executable(s).

Contains facts from many Facter version on many Operating Systems

%description   -n facterdb -l ru_RU.UTF-8
Исполнямка для самоцвета facterdb.


%package       -n gem-facterdb-doc
Version:       1.19.0
Release:       alt1
Summary:       A Database of OS facts provided by Facter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета facterdb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(facterdb) = 1.19.0

%description   -n gem-facterdb-doc
A Database of OS facts provided by Facter documentation files.

Contains facts from many Facter version on many Operating Systems

%description   -n gem-facterdb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета facterdb.


%package       -n gem-facterdb-devel
Version:       1.19.0
Release:       alt1
Summary:       A Database of OS facts provided by Facter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета facterdb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(facterdb) = 1.19.0
Requires:      gem(coveralls) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-facterdb-devel
A Database of OS facts provided by Facter development package.

Contains facts from many Facter version on many Operating Systems

%description   -n gem-facterdb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета facterdb.


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

%files         -n facterdb
%doc README.md
%_bindir/facterdb

%files         -n gem-facterdb-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-facterdb-devel
%doc README.md


%changelog
* Thu Sep 15 2022 Pavel Skrylev <majioa@altlinux.org> 1.19.0-alt1
- + packaged gem with Ruby Policy 2.0
