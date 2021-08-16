%define        gemname plist

Name:          gem-plist
Version:       3.6.0
Release:       alt1
Summary:       All-purpose Property List manipulation library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bleything/plist
Vcs:           https://github.com/bleything/plist.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.14 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.5 gem(rake) < 14
BuildRequires: gem(test-unit) >= 1.2 gem(test-unit) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
Obsoletes:     ruby-plist < %EVR
Provides:      ruby-plist = %EVR
Provides:      gem(plist) = 3.6.0


%description
Plist is a library to manipulate Property List files, also known as plists. It
can parse plist files into native Ruby data structures as well as generating new
plist files from your Ruby objects.


%package       -n gem-plist-doc
Version:       3.6.0
Release:       alt1
Summary:       All-purpose Property List manipulation library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета plist
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(plist) = 3.6.0

%description   -n gem-plist-doc
All-purpose Property List manipulation library for Ruby documentation
files.

Plist is a library to manipulate Property List files, also known as plists. It
can parse plist files into native Ruby data structures as well as generating new
plist files from your Ruby objects.

%description   -n gem-plist-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета plist.


%package       -n gem-plist-devel
Version:       3.6.0
Release:       alt1
Summary:       All-purpose Property List manipulation library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета plist
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(plist) = 3.6.0
Requires:      gem(bundler) >= 1.14 gem(bundler) < 3
Requires:      gem(rake) >= 10.5 gem(rake) < 14
Requires:      gem(test-unit) >= 1.2 gem(test-unit) < 4

%description   -n gem-plist-devel
All-purpose Property List manipulation library for Ruby development
package.

Plist is a library to manipulate Property List files, also known as plists. It
can parse plist files into native Ruby data structures as well as generating new
plist files from your Ruby objects.

%description   -n gem-plist-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета plist.


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

%files         -n gem-plist-doc
%ruby_gemdocdir

%files         -n gem-plist-devel


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt1
- ^ 3.4.0 -> 3.6.0

* Wed Jul 18 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Return to Sisyphus
