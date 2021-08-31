%define        gemname mustermann

Name:          gem-mustermann
Version:       1.1.1
Release:       alt1.1
Summary:       The Amazing Mustermann
License:       MIT
Group:         Development/Ruby
Url:           http://sinatrarb.com/mustermann/
Vcs:           https://github.com/sinatra/mustermann.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ruby2_keywords) >= 0.0.1 gem(ruby2_keywords) < 0.1
BuildRequires: gem(hansi) >= 0.2.0 gem(hansi) < 0.3
BuildRequires: gem(ruby2_keywords) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names ruby-mustermann,support
Requires:      gem(ruby2_keywords) >= 0.0.1 gem(ruby2_keywords) < 0.1
Obsoletes:     ruby-mustermann < %EVR
Provides:      ruby-mustermann = %EVR
Provides:      gem(mustermann) = 1.1.1


%description
Mustermann is your personal string matching expert.


%package       -n gem-mustermann-contrib
Version:       1.1.1
Release:       alt1.1
Summary:       A meta gem depending on all other official mustermann gems
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mustermann) = 1.1.1
Requires:      gem(hansi) >= 0.2.0 gem(hansi) < 0.3
Provides:      gem(mustermann-contrib) = 1.1.1

%description   -n gem-mustermann-contrib
A meta gem depending on all other official mustermann gems.

Mustermann is your personal string matching expert.


%package       -n gem-mustermann-contrib-doc
Version:       1.1.1
Release:       alt1.1
Summary:       A meta gem depending on all other official mustermann gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mustermann-contrib
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mustermann-contrib) = 1.1.1

%description   -n gem-mustermann-contrib-doc
A meta gem depending on all other official mustermann gems documentation
files.

Mustermann is your personal string matching expert.

%description   -n gem-mustermann-contrib-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mustermann-contrib.


%package       -n gem-mustermann-contrib-devel
Version:       1.1.1
Release:       alt1.1
Summary:       A meta gem depending on all other official mustermann gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mustermann-contrib
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mustermann-contrib) = 1.1.1

%description   -n gem-mustermann-contrib-devel
A meta gem depending on all other official mustermann gems development
package.

Mustermann is your personal string matching expert.

%description   -n gem-mustermann-contrib-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mustermann-contrib.


%package       -n gem-mustermann-doc
Version:       1.1.1
Release:       alt1.1
Summary:       The Amazing Mustermann documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mustermann
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mustermann) = 1.1.1

%description   -n gem-mustermann-doc
The Amazing Mustermann documentation files.

Mustermann is your personal string matching expert.

%description   -n gem-mustermann-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mustermann.


%package       -n gem-mustermann-devel
Version:       1.1.1
Release:       alt1.1
Summary:       The Amazing Mustermann development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mustermann
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mustermann) = 1.1.1

%description   -n gem-mustermann-devel
The Amazing Mustermann development package.

Mustermann is your personal string matching expert.

%description   -n gem-mustermann-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mustermann.


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

%files         -n gem-mustermann-contrib
%doc README.md
%ruby_gemspecdir/mustermann-contrib-1.1.1.gemspec
%ruby_gemslibdir/mustermann-contrib-1.1.1

%files         -n gem-mustermann-contrib-doc
%doc README.md
%ruby_gemsdocdir/mustermann-contrib-1.1.1

%files         -n gem-mustermann-contrib-devel
%doc README.md

%files         -n gem-mustermann-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mustermann-devel
%doc README.md


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1.1
- ! spec

* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with usage Ruby Policy 2.0
