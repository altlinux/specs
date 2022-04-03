%define        gemname date

Name:          gem-date
Version:       3.2.2
Release:       alt1
Summary:       A subclass of Object includes Comparable module for handling dates
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/date
Vcs:           https://github.com/ruby/date.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(date) = 3.2.2


%description
A subclass of Object includes Comparable module for handling dates.


%package       -n gem-date-doc
Version:       3.2.2
Release:       alt1
Summary:       A subclass of Object includes Comparable module for handling dates documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета date
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(date) = 3.2.2

%description   -n gem-date-doc
A subclass of Object includes Comparable module for handling dates documentation
files.

%description   -n gem-date-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета date.


%package       -n gem-date-devel
Version:       3.2.2
Release:       alt1
Summary:       A subclass of Object includes Comparable module for handling dates development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета date
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(date) = 3.2.2

%description   -n gem-date-devel
A subclass of Object includes Comparable module for handling dates development
package.

%description   -n gem-date-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета date.


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
%ruby_gemextdir

%files         -n gem-date-doc
%ruby_gemdocdir

%files         -n gem-date-devel
%ruby_includedir/*


%changelog
* Mon Apr 04 2022 Pavel Skrylev <majioa@altlinux.org> 3.2.2-alt1
- + packaged gem with Ruby Policy 2.0
